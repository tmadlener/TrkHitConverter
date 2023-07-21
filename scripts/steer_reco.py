#!/usr/bin/env python3

from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *

algList = []
evtsvc = EventDataSvc()


CONSTANTS = {}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["muonGun_sim_v0A.slcio"]
algList.append(read)

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = INFO
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
    "Overlay": ["False"],
    "OverlayChoices": ["False", "BIB"],
    "Tracking": ["Truth"],
    "TrackingChoices": ["Truth", "Conformal"],
    "VertexUnconstrained": ["OFF"],
    "VertexUnconstrainedChoices": ["ON", "OFF"],
}

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {"HowOften": ["1"]}

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {"FileName": ["lctuple_muonGun"], "FileType": ["root"]}

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
    "DropCollectionNames": [],
    "DropCollectionTypes": ["SimCalorimeterHit", "SimTrackerHit"],
    "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
    "KeepCollectionNames": ["MCParticle_SiTracks_Refitted"],
    "LCIOOutputFile": ["pionGun_REC_w_plainhits.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"],
}

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
    "DD4hepXMLFile": ["$GEOMETRY/geometries/MuColl_10TeV_v0A/MuColl_10TeV_v0A.xml"],
    "EncodingStringParameterName": ["GlobalTrackerReadoutID"],
}

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexBarrelCollection"],
    "SimTrkHitRelCollection": ["VBTrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VBTrackerHits"],
    "UseTimeWindow": ["true"],
}

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexEndcapCollection"],
    "SimTrkHitRelCollection": ["VETrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VETrackerHits"],
    "UseTimeWindow": ["true"],
}

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = INFO
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["IBTrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IBTrackerHits"],
    "UseTimeWindow": ["true"],
}

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "InnerEndcapPlanarDigiProcessor"
)
InnerEndcapPlanarDigiProcessor.OutputLevel = INFO
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["IETrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IETrackerHits"],
    "UseTimeWindow": ["true"],
}

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["OBTrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OBTrackerHits"],
    "UseTimeWindow": ["true"],
}

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "OuterEndcapPlanarDigiProcessor"
)
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["OETrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OETrackerHits"],
    "UseTimeWindow": ["true"],
}

CKFTracking = MarlinProcessorWrapper("CKFTracking")
CKFTracking.OutputLevel = INFO
CKFTracking.ProcessorType = "ACTSSeededCKFTrackingProc"
CKFTracking.Parameters = {
    "CKF_Chi2CutOff": ["10"],
    "CKF_NumMeasurementsCutOff": ["1"],
    "MatFile": [
        "/opt/spack/opt/spack/linux-ubuntu22.04-x86_64/gcc-11.3.0/actstracking-1.1.0-vk7dd4tkm75atbkawti2mfozyujq6db2/share/ACTSTracking/data/material-maps.json"
    ],
    "PropagateBackward": ["False"],
    "RunCKF": ["True"],
    "SeedFinding_CollisionRegion": ["1"],
    "SeedFinding_DeltaRMax": ["80"],
    "SeedFinding_DeltaRMin": ["5"],
    "SeedFinding_ImpactMax": ["3"],
    "SeedFinding_MinPt": ["500"],
    "SeedFinding_RMax": ["150"],
    "SeedFinding_RadLengthPerSeed": ["0.1"],
    "SeedFinding_SigmaScattering": ["50"],
    "SeedingLayers": [
        "13",
        "2",
        "13",
        "6",
        "13",
        "10",
        "13",
        "14",
        "14",
        "2",
        "14",
        "6",
        "14",
        "10",
        "14",
        "14",
        "15",
        "2",
        "15",
        "6",
        "15",
        "10",
        "15",
        "14",
    ],
    "TGeoFile": [
        "/opt/spack/opt/spack/linux-ubuntu22.04-x86_64/gcc-11.3.0/actstracking-1.1.0-vk7dd4tkm75atbkawti2mfozyujq6db2/share/ACTSTracking/data/MuColl_v1.root"
    ],
    "TrackCollectionName": ["AllTracks"],
    "TrackerHitCollectionNames": [
        "VBTrackerHits",
        "IBTrackerHits",
        "OBTrackerHits",
        "VETrackerHits",
        "IETrackerHits",
        "OETrackerHits",
    ],
}

TrackDeduper = MarlinProcessorWrapper("TrackDeduper")
TrackDeduper.OutputLevel = INFO
TrackDeduper.ProcessorType = "ACTSDuplicateRemoval"
TrackDeduper.Parameters = {
    "InputTrackCollectionName": ["AllTracks"],
    "OutputTrackCollectionName": ["SiTracks"],
}

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = INFO
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
    "DoCutsOnRedChi2Nhits": ["true"],
    "EnergyLossOn": ["true"],
    "InputRelationCollectionName": ["SiTrackRelations"],
    "InputTrackCollectionName": ["SiTracks"],
    "Max_Chi2_Incr": ["1.79769e+30"],
    "MinClustersOnTrackAfterFit": ["3"],
    "MultipleScatteringOn": ["true"],
    "NHitsCuts": ["1,2", "1", "3,4", "1", "5,6", "0"],
    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
    "OutputTrackCollectionName": ["SiTracks_Refitted"],
    "ReducedChi2Cut": ["3."],
    "ReferencePoint": ["-1"],
    "SmoothOn": ["false"],
    "extrapolateForward": ["true"],
}

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = INFO
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks_Refitted"],
    "TrackCollection": ["SiTracks_Refitted"],
    "TrackerHit2SimTrackerHitRelationName": [
        "VBTrackerHitsRelations",
        "IBTrackerHitsRelations",
        "OBTrackerHitsRelations",
        "VETrackerHitsRelations",
        "IETrackerHitsRelations",
        "OETrackerHitsRelations",
    ],
}

MyEcalBarrelDigi = MarlinProcessorWrapper("MyEcalBarrelDigi")
MyEcalBarrelDigi.OutputLevel = INFO
MyEcalBarrelDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0001575"],
    "inputHitCollections": ["ECalBarrelCollection"],
    "outputHitCollections": ["EcalBarrelCollectionDigi"],
    "outputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "threshold": ["0.002"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
}

MyEcalBarrelReco = MarlinProcessorWrapper("MyEcalBarrelReco")
MyEcalBarrelReco.OutputLevel = INFO
MyEcalBarrelReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["0.00641222630095"],
    "calibration_layergroups": ["50"],
    "inputHitCollections": ["EcalBarrelCollectionDigi"],
    "inputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["EcalBarrelCollectionRec"],
    "outputRelationCollections": ["EcalBarrelRelationsSimRec"],
}

MyEcalBarrelGapFiller = MarlinProcessorWrapper("MyEcalBarrelGapFiller")
MyEcalBarrelGapFiller.OutputLevel = INFO
MyEcalBarrelGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalBarrelGapFiller.Parameters = {
    "CellIDLayerString": ["layer"],
    "CellIDModuleString": ["module"],
    "CellIDStaveString": ["stave"],
    "applyInterModuleCorrection": ["false"],
    "expectedInterModuleDistance": ["7.0"],
    "inputHitCollection": ["EcalBarrelCollectionRec"],
    "outputHitCollection": ["EcalBarrelCollectionGapHits"],
}

MyEcalEndcapDigi = MarlinProcessorWrapper("MyEcalEndcapDigi")
MyEcalEndcapDigi.OutputLevel = INFO
MyEcalEndcapDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0001575"],
    "inputHitCollections": ["ECalEndcapCollection"],
    "outputHitCollections": ["EcalEndcapCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapRelationsSimDigi"],
    "threshold": ["0.002"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
}

MyEcalEndcapReco = MarlinProcessorWrapper("MyEcalEndcapReco")
MyEcalEndcapReco.OutputLevel = INFO
MyEcalEndcapReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["0.00641222630095"],
    "calibration_layergroups": ["50"],
    "inputHitCollections": ["EcalEndcapCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapCollectionRec"],
    "outputRelationCollections": ["EcalEndcapRelationsSimRec"],
}

MyEcalEndcapGapFiller = MarlinProcessorWrapper("MyEcalEndcapGapFiller")
MyEcalEndcapGapFiller.OutputLevel = INFO
MyEcalEndcapGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalEndcapGapFiller.Parameters = {
    "CellIDLayerString": ["layer"],
    "CellIDModuleString": ["module"],
    "CellIDStaveString": ["stave"],
    "applyInterModuleCorrection": ["false"],
    "expectedInterModuleDistance": ["7.0"],
    "inputHitCollection": ["EcalEndcapCollectionRec"],
    "outputHitCollection": ["EcalEndcapCollectionGapHits"],
}

MyHcalBarrelDigi = MarlinProcessorWrapper("MyHcalBarrelDigi")
MyHcalBarrelDigi.OutputLevel = INFO
MyHcalBarrelDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0004825"],
    "inputHitCollections": ["HCalBarrelCollection"],
    "outputHitCollections": ["HcalBarrelsCollectionDigi"],
    "outputRelationCollections": ["HcalBarrelsRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.002"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
}

MyHcalBarrelReco = MarlinProcessorWrapper("MyHcalBarrelReco")
MyHcalBarrelReco.OutputLevel = INFO
MyHcalBarrelReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["0.0231348530678"],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalBarrelsCollectionDigi"],
    "inputRelationCollections": ["HcalBarrelsRelationsSimDigi"],
    "outputHitCollections": ["HcalBarrelsCollectionRec"],
    "outputRelationCollections": ["HcalBarrelsRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
}

MyHcalEndcapDigi = MarlinProcessorWrapper("MyHcalEndcapDigi")
MyHcalEndcapDigi.OutputLevel = INFO
MyHcalEndcapDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0004825"],
    "inputHitCollections": ["HCalEndcapCollection"],
    "outputHitCollections": ["HcalEndcapsCollectionDigi"],
    "outputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.002"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
}

MyHcalEndcapReco = MarlinProcessorWrapper("MyHcalEndcapReco")
MyHcalEndcapReco.OutputLevel = INFO
MyHcalEndcapReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["0.0231348530678"],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalEndcapsCollectionDigi"],
    "inputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
    "outputHitCollections": ["HcalEndcapsCollectionRec"],
    "outputRelationCollections": ["HcalEndcapsRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
}

MyEcalBarrelSelector = MarlinProcessorWrapper("MyEcalBarrelSelector")
MyEcalBarrelSelector.OutputLevel = INFO
MyEcalBarrelSelector.ProcessorType = "CaloHitSelector"
MyEcalBarrelSelector.Parameters = {
    "CaloHitCollectionName": ["EcalBarrelCollectionRec"],
    "CaloRelationCollectionName": ["EcalBarrelRelationsSimRec"],
    "GoodHitCollection": ["EcalBarrelCollectionSel"],
    "GoodRelationCollection": ["EcalBarrelRelationsSimSel"],
    "Nlayers": ["50"],
    "Nsigma": ["3"],
}

MyEcalEndcapSelector = MarlinProcessorWrapper("MyEcalEndcapSelector")
MyEcalEndcapSelector.OutputLevel = INFO
MyEcalEndcapSelector.ProcessorType = "CaloHitSelector"
MyEcalEndcapSelector.Parameters = {
    "CaloHitCollectionName": ["EcalEndcapCollectionRec"],
    "CaloRelationCollectionName": ["EcalEndcapRelationsSimRec"],
    "GoodHitCollection": ["EcalEndcapCollectionSel"],
    "GoodRelationCollection": ["EcalEndcapRelationsSimSel"],
    "Nlayers": ["50"],
    "Nsigma": ["3"],
}

MyHcalBarrelSelector = MarlinProcessorWrapper("MyHcalBarrelSelector")
MyHcalBarrelSelector.OutputLevel = INFO
MyHcalBarrelSelector.ProcessorType = "CaloHitSelector"
MyHcalBarrelSelector.Parameters = {
    "CaloHitCollectionName": ["HcalBarrelsCollectionRec"],
    "CaloRelationCollectionName": ["HcalBarrelsRelationsSimRec"],
    "GoodHitCollection": ["HcalBarrelCollectionSel"],
    "GoodRelationCollection": ["HcalBarrelRelationsSimSel"],
    "Nlayers": ["75"],
    "Nsigma": ["3"],
}

MyHcalEndcapSelector = MarlinProcessorWrapper("MyHcalEndcapSelector")
MyHcalEndcapSelector.OutputLevel = INFO
MyHcalEndcapSelector.ProcessorType = "CaloHitSelector"
MyHcalEndcapSelector.Parameters = {
    "CaloHitCollectionName": ["HcalEndcapsCollectionRec"],
    "CaloRelationCollectionName": ["HcalEndcapsRelationsSimRec"],
    "GoodHitCollection": ["HcalEndcapCollectionSel"],
    "GoodRelationCollection": ["HcalEndcapRelationsSimSel"],
    "Nlayers": ["75"],
    "Nsigma": ["3"],
}

DDMarlinPandora = MarlinProcessorWrapper("DDMarlinPandora")
DDMarlinPandora.OutputLevel = INFO
DDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
DDMarlinPandora.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "CreateGaps": ["false"],
    "CurvatureToMomentumFactor": ["0.00015"],
    "D0TrackCut": ["200"],
    "D0UnmatchedVertexTrackCut": ["5"],
    "DigitalMuonHits": ["0"],
    "ECalBarrelNormalVector": ["0", "0", "1"],
    "ECalCaloHitCollections": ["EcalBarrelCollectionSel", "EcalEndcapCollectionSel"],
    "ECalMipThreshold": ["0.5"],
    "ECalScMipThreshold": ["0"],
    "ECalScToEMGeVCalibration": ["1"],
    "ECalScToHadGeVCalibrationBarrel": ["1"],
    "ECalScToHadGeVCalibrationEndCap": ["1"],
    "ECalScToMipCalibration": ["1"],
    "ECalSiMipThreshold": ["0"],
    "ECalSiToEMGeVCalibration": ["1"],
    "ECalSiToHadGeVCalibrationBarrel": ["1"],
    "ECalSiToHadGeVCalibrationEndCap": ["1"],
    "ECalSiToMipCalibration": ["1"],
    "ECalToEMGeVCalibration": ["1.02373335516"],
    "ECalToHadGeVCalibrationBarrel": ["1.24223718397"],
    "ECalToHadGeVCalibrationEndCap": ["1.24223718397"],
    "ECalToMipCalibration": ["181.818"],
    "EMConstantTerm": ["0.01"],
    "EMStochasticTerm": ["0.17"],
    "FinalEnergyDensityBin": ["110."],
    "HCalBarrelNormalVector": ["0", "0", "1"],
    "HCalCaloHitCollections": ["HcalBarrelCollectionSel", "HcalEndcapCollectionSel"],
    "HCalMipThreshold": ["0.3"],
    "HCalToEMGeVCalibration": ["1.02373335516"],
    "HCalToHadGeVCalibration": ["1.01799349172"],
    "HCalToMipCalibration": ["40.8163"],
    "HadConstantTerm": ["0.03"],
    "HadStochasticTerm": ["0.6"],
    "InputEnergyCorrectionPoints": [],
    "KinkVertexCollections": ["KinkVertices"],
    "LayersFromEdgeMaxRearDistance": ["250"],
    "MCParticleCollections": ["MCParticle"],
    "MaxBarrelTrackerInnerRDistance": ["200"],
    "MaxClusterEnergyToApplySoftComp": ["2000."],
    "MaxHCalHitHadronicEnergy": ["1000000"],
    "MaxTrackHits": ["5000"],
    "MaxTrackSigmaPOverP": ["0.15"],
    "MinBarrelTrackerHitFractionOfExpected": ["0"],
    "MinCleanCorrectedHitEnergy": ["0.1"],
    "MinCleanHitEnergy": ["0.5"],
    "MinCleanHitEnergyFraction": ["0.01"],
    "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
    "MinFtdTrackHits": ["0"],
    "MinMomentumForTrackHitChecks": ["0"],
    "MinTpcHitFractionOfExpected": ["0"],
    "MinTrackECalDistanceFromIp": ["0"],
    "MinTrackHits": ["0"],
    "MuonBarrelBField": ["-1.34"],
    "MuonCaloHitCollections": [],
    "MuonEndCapBField": ["0.01"],
    "MuonHitEnergy": ["0.5"],
    "MuonToMipCalibration": ["19607.8"],
    "NEventsToSkip": ["0"],
    "NOuterSamplingLayers": ["3"],
    "OutputEnergyCorrectionPoints": [],
    "PFOCollectionName": ["PandoraPFOs"],
    "PandoraSettingsXmlFile": ["PandoraSettings/PandoraSettingsDefault.xml"],
    "ProngVertexCollections": ["ProngVertices"],
    "ReachesECalBarrelTrackerOuterDistance": ["-100"],
    "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
    "ReachesECalFtdZMaxDistance": ["1"],
    "ReachesECalMinFtdLayer": ["0"],
    "ReachesECalNBarrelTrackerHits": ["0"],
    "ReachesECalNFtdHits": ["0"],
    "RelCaloHitCollections": [
        "EcalBarrelRelationsSimSel",
        "EcalEndcapRelationsSimSel",
        "HcalBarrelRelationsSimSel",
        "HcalEndcapRelationsSimSel",
    ],
    "RelTrackCollections": ["SiTracks_Refitted_Relation"],
    "ShouldFormTrackRelationships": ["1"],
    "SoftwareCompensationEnergyDensityBins": [
        "0",
        "2.",
        "5.",
        "7.5",
        "9.5",
        "13.",
        "16.",
        "20.",
        "23.5",
        "28.",
        "33.",
        "40.",
        "50.",
        "75.",
        "100.",
    ],
    "SoftwareCompensationWeights": [
        "1.61741",
        "-0.00444385",
        "2.29683e-05",
        "-0.0731236",
        "-0.00157099",
        "-7.09546e-07",
        "0.868443",
        "1.0561",
        "-0.0238574",
    ],
    "SplitVertexCollections": ["SplitVertices"],
    "StartVertexAlgorithmName": ["PandoraPFANew"],
    "StartVertexCollectionName": ["PandoraStartVertices"],
    "StripSplittingOn": ["0"],
    "TrackCollections": ["SiTracks_Refitted"],
    "TrackCreatorName": ["DDTrackCreatorCLIC"],
    "TrackStateTolerance": ["0"],
    "TrackSystemName": ["DDKalTest"],
    "UnmatchedVertexTrackMaxEnergy": ["5"],
    "UseEcalScLayers": ["0"],
    "UseNonVertexTracks": ["1"],
    "UseOldTrackStateCalculation": ["0"],
    "UseUnmatchedNonVertexTracks": ["0"],
    "UseUnmatchedVertexTracks": ["1"],
    "V0VertexCollections": ["V0Vertices"],
    "YokeBarrelNormalVector": ["0", "0", "1"],
    "Z0TrackCut": ["200"],
    "Z0UnmatchedVertexTrackCut": ["5"],
    "ZCutForNonVertexTracks": ["250"],
}

FastJetProcessor = MarlinProcessorWrapper("FastJetProcessor")
FastJetProcessor.OutputLevel = INFO
FastJetProcessor.ProcessorType = "FastJetProcessor"
FastJetProcessor.Parameters = {
    "algorithm": ["antikt_algorithm", "0.4"],
    "clusteringMode": ["Inclusive", "5"],
    "jetOut": ["JetOut"],
    "recParticleIn": ["PandoraPFOs"],
    "recombinationScheme": ["E_scheme"],
}

OverlayFalse = MarlinProcessorWrapper("OverlayFalse")
OverlayFalse.OutputLevel = INFO
OverlayFalse.ProcessorType = "OverlayTimingGeneric"
OverlayFalse.Parameters = {
    "BackgroundFileNames": ["/dev/null"],
    "Collection_IntegrationTimes": [
        "VertexBarrelCollection",
        "-0.36",
        "0.48",
        "VertexEndcapCollection",
        "-0.36",
        "0.48",
        "InnerTrackerBarrelCollection",
        "-0.36",
        "0.48",
        "InnerTrackerEndcapCollection",
        "-0.36",
        "0.48",
        "OuterTrackerBarrelCollection",
        "-0.36",
        "0.48",
        "OuterTrackerEndcapCollection",
        "-0.36",
        "0.48",
        "ECalBarrelCollection",
        "-0.25",
        "10.",
        "ECalEndcapCollection",
        "-0.25",
        "10.",
        "HCalBarrelCollection",
        "-0.25",
        "10.",
        "HCalEndcapCollection",
        "-0.25",
        "10.",
        "YokeBarrelCollection",
        "-0.25",
        "10.",
        "YokeEndcapCollection",
        "-0.25",
        "10.",
    ],
    "Delta_t": ["10000"],
    "IntegrationTimeMin": ["-0.36"],
    "MCParticleCollectionName": ["MCParticle"],
    "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
    "MergeMCParticles": ["false"],
    "NBunchtrain": ["0"],
    "NumberBackground": ["0."],
    "PhysicsBX": ["1"],
    "Poisson_random_NOverlay": ["false"],
    "RandomBx": ["false"],
    "TPCDriftvelocity": ["0.05"],
}

OverlayBIB = MarlinProcessorWrapper("OverlayBIB")
OverlayBIB.OutputLevel = INFO
OverlayBIB.ProcessorType = "OverlayTimingGeneric"
OverlayBIB.Parameters = {
    "AllowReusingBackgroundFiles": ["true"],
    "BackgroundFileNames": [
        "/data/BIB10TeV/BIB_sim_mm.slcio",
        "/data/BIB10TeV/BIB_sim_mp.slcio",
    ],
    "Collection_IntegrationTimes": [
        "VertexBarrelCollection",
        "-0.36",
        "0.48",
        "VertexEndcapCollection",
        "-0.36",
        "0.48",
        "InnerTrackerBarrelCollection",
        "-0.36",
        "0.48",
        "InnerTrackerEndcapCollection",
        "-0.36",
        "0.48",
        "OuterTrackerBarrelCollection",
        "-0.36",
        "0.48",
        "OuterTrackerEndcapCollection",
        "-0.36",
        "0.48",
        "ECalBarrelCollection",
        "-0.25",
        "10.",
        "ECalEndcapCollection",
        "-0.25",
        "10.",
        "HCalBarrelCollection",
        "-0.25",
        "10.",
        "HCalEndcapCollection",
        "-0.25",
        "10.",
        "YokeBarrelCollection",
        "-0.25",
        "10.",
        "YokeEndcapCollection",
        "-0.25",
        "10.",
    ],
    "Delta_t": ["10000"],
    "IntegrationTimeMin": ["-0.36"],
    "MCParticleCollectionName": ["MCParticle"],
    "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
    "MergeMCParticles": ["false"],
    "NBunchtrain": ["1"],
    "NumberBackground": ["1060"],
    "PhysicsBX": ["1"],
    "Poisson_random_NOverlay": ["false"],
    "RandomBx": ["false"],
    "StartBackgroundFileIndex": ["0"],
    "TPCDriftvelocity": ["0.05"],
}

TrkHitConverter = MarlinProcessorWrapper("TrkHitConverter")
TrkHitConverter.OutputLevel = INFO
TrkHitConverter.ProcessorType = "TrkHitConverterProcessor"
TrkHitConverter.Parameters = {
    "InputHitCollections": [
        "VETrackerHits",
        "OETrackerHit",
        "VBTrackerHits",
        "IETrackerHits",
        "OBTrackerHits",
        "IBTrackerHits",
    ],
    "InputTrackCollections": [
        "SiTracks_Refitted",
        "SiTracks",
        "AllTracks",
        "SeedTracks",
    ],
    "OutputNameSuffix": ["_plainHits"],
}


algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(Config)
algList.append(InitDD4hep)
# algList.append(OverlayBIB)  # Config.OverlayBIB
algList.append(OverlayFalse)  # Config.OverlayFalse
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(CKFTracking)
algList.append(TrackDeduper)
algList.append(Refit)
algList.append(MyTrackTruth)
algList.append(MyEcalBarrelDigi)
algList.append(MyEcalBarrelReco)
algList.append(MyEcalEndcapDigi)
algList.append(MyEcalEndcapReco)
algList.append(MyHcalBarrelDigi)
algList.append(MyHcalBarrelReco)
algList.append(MyHcalEndcapDigi)
algList.append(MyHcalEndcapReco)
# algList.append(MyEcalBarrelSelector)
# algList.append(MyEcalEndcapSelector)
# algList.append(MyHcalBarrelSelector)
# algList.append(MyHcalEndcapSelector)
# algList.append(DDMarlinPandora)
# algList.append(FastJetProcessor)
algList.append(TrkHitConverter)
algList.append(Output_REC)

from Configurables import ApplicationMgr

ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=10, ExtSvc=[evtsvc], OutputLevel=INFO
)
