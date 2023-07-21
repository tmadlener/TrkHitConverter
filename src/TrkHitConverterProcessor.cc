#include "TrkHitConverterProcessor.h"

#include "marlin/VerbosityLevels.h"

#include <EVENT/Track.h>
#include <EVENT/TrackerHitPlane.h>
#include <IMPL/LCCollectionVec.h>
#include <IMPL/TrackImpl.h>
#include <IMPL/TrackStateImpl.h>
#include <IMPL/TrackerHitImpl.h>
#include <UTIL/LCIterator.h>

#include "lcio.h"

#include <map>
#include <memory>
#include <utility>
#include <vector>

using HitMap = std::map<const EVENT::TrackerHit *, IMPL::TrackerHitImpl *>;
using TrackMap = std::map<const EVENT::Track *, IMPL::TrackImpl *>;

TrkHitConverterProcessor aConverter;

TrkHitConverterProcessor::TrkHitConverterProcessor()
    : marlin::Processor("TrkHitConverterProcessor") {
  _description =
      "Processor to convert TrackerHitPlanes to TrackerHits in order "
      "to make them more easily convertible to EDM4hep. It also produces new "
      "track collections to which the tracks are attached";

  registerProcessorParameter(
      "InputHitCollections",
      "Name of the input TrackerHitPlane collections to convert",
      m_inputHitCollNames, std::vector<std::string>{});

  registerProcessorParameter("InputTrackCollections",
                             "Name of the input track collections to which the "
                             "new tracker hits should be attached",
                             m_inputTrackCollNames, std::vector<std::string>{});

  registerProcessorParameter(
      "OutputNameSuffix",
      "suffix that will be appended to the individual output collections",
      m_outputSuffix, std::string("_plainHits"));
}

void TrkHitConverterProcessor::init() { printParameters(); }

auto convertHits(const EVENT::LCCollection *inputHits, HitMap &hitMap) {
  std::vector<IMPL::TrackerHitImpl *> outputHits;
  outputHits.reserve(inputHits->getNumberOfElements());

  LCIterator<EVENT::TrackerHitPlane> it(inputHits);
  while (const auto *hit = it.next()) {
    auto newHit = new IMPL::TrackerHitImpl();
    newHit->setCellID0(hit->getCellID0());
    newHit->setCellID1(hit->getCellID1());
    newHit->setPosition(hit->getPosition());
    newHit->setCovMatrix(hit->getCovMatrix());
    newHit->setEDep(hit->getEDep());
    newHit->setEDepError(hit->getEDepError());
    newHit->setTime(hit->getTime());
    newHit->setType(hit->getType());
    newHit->setQuality(hit->getQuality());

    outputHits.emplace_back(newHit);
    hitMap.emplace(hit, newHit);
  }

  return outputHits;
}

auto convertTracks(const EVENT::LCCollection *inputTracks, TrackMap &trackMap) {
  std::vector<IMPL::TrackImpl *> outputTracks;
  outputTracks.reserve(inputTracks->getNumberOfElements());

  LCIterator<EVENT::Track> it(inputTracks);
  while (const auto *track = it.next()) {
    auto newTrack = new IMPL::TrackImpl();

    // taken from EDM4hep2LcioConv
    // The Type of the Tracks need to be set bitwise in LCIO since the
    // setType(int) function is private for the LCIO TrackImpl and only a
    // setTypeBit(bitnumber) function can be used to set the Type bit by bit.
    const int type = track->getType();
    for (auto i = 0u; i < sizeof(int) * 8; i++) {
      newTrack->setTypeBit(i, type & (1 << i));
    }

    newTrack->setD0(track->getD0());
    newTrack->setPhi(track->getPhi());
    newTrack->setOmega(track->getOmega());
    newTrack->setZ0(track->getZ0());
    newTrack->setTanLambda(track->getTanLambda());
    newTrack->setCovMatrix(track->getCovMatrix());
    newTrack->setReferencePoint(track->getReferencePoint());
    newTrack->setChi2(track->getChi2());
    newTrack->setNdf(track->getNdf());
    newTrack->setdEdx(track->getdEdx());
    newTrack->setdEdxError(track->getdEdxError());
    newTrack->setRadiusOfInnermostHit(track->getRadiusOfInnermostHit());
    newTrack->subdetectorHitNumbers() = track->getSubdetectorHitNumbers();

    for (const auto *trackState : track->getTrackStates()) {
      newTrack->addTrackState(
          new IMPL::TrackStateImpl(*dynamic_cast<const IMPL::TrackStateImpl *>(
              trackState))); // full copy
    }

    outputTracks.emplace_back(newTrack);
    trackMap.emplace(track, newTrack);
  }

  return outputTracks;
}

/**
 * Convert a collection after getting it from the event using a passed in
 * conversion function. This handles all the boilerplate around potentially
 * non-existing collections in an event and returns a
 * vector<unique_ptr<LCCollectionVec>>
 */
template <typename ConvFuncT, typename MapT>
auto convertCollection(EVENT::LCEvent *evt, const std::string &name,
                       const char *lcioTypeName, MapT &objectMap,
                       ConvFuncT &&convFunc) {
  streamlog_out(DEBUG) << "Converting collection " << name << '\n';
  auto outputColl = std::make_unique<IMPL::LCCollectionVec>(lcioTypeName);
  try {
    const auto *inputColl = evt->getCollection(name);
    for (auto *elem : convFunc(inputColl, objectMap)) {
      outputColl->addElement(elem);
    }
  } catch (lcio::DataNotAvailableException &) {
    streamlog_out(DEBUG)
        << "Input collection not present. Filling an empty collection"
        << std::endl;
  }
  streamlog_out(DEBUG) << "converted " << outputColl->getNumberOfElements()
                       << " tracker hits\n";

  return outputColl;
}

void resolveHitRelations(TrackMap &trackMap, const HitMap &hitMap) {
  for (auto &[oldTrack, newTrack] : trackMap) {
    for (const auto *oldRelTrack : oldTrack->getTracks()) {
      if (const auto it = trackMap.find(oldRelTrack); it != trackMap.end()) {
        newTrack->addTrack(it->second);
      } else {
        streamlog_out(WARNING)
            << "Cannot add a related track to a converted track because the "
               "related track was not converted"
            << std::endl;
      }
    }

    for (const auto *oldRelHit : oldTrack->getTrackerHits()) {
      if (const auto it = hitMap.find(oldRelHit); it != hitMap.end()) {
        newTrack->addHit(it->second);
      } else {
        streamlog_out(WARNING)
            << "Cannot add a tracker hit to a converted track because the "
               "tracker hit was not converted"
            << std::endl;
      }
    }
  }
}

void TrkHitConverterProcessor::processEvent(EVENT::LCEvent *evt) {
  auto hitMap = HitMap{};
  std::vector<std::pair<std::unique_ptr<IMPL::LCCollectionVec>, std::string>>
      outputHitCollections{};
  for (const auto &collName : m_inputHitCollNames) {
    outputHitCollections.emplace_back(
        convertCollection(evt, collName, LCIO::TRACKERHIT, hitMap, convertHits),
        collName);
  }

  auto trackMap = TrackMap{};
  std::vector<std::pair<std::unique_ptr<IMPL::LCCollectionVec>, std::string>>
      outputTrkCollections{};
  for (const auto &collName : m_inputTrackCollNames) {
    outputTrkCollections.emplace_back(
        convertCollection(evt, collName, LCIO::TRACK, trackMap, convertTracks),
        collName);
  }

  // Add things to the event
  for (auto &[coll, name] : outputHitCollections) {
    evt->addCollection(coll.release(), name + m_outputSuffix);
  }
  for (auto &[coll, name] : outputTrkCollections) {
    evt->addCollection(coll.release(), name + m_outputSuffix);
  }
}
