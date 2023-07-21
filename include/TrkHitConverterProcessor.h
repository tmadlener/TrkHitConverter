#ifndef TRKHITCONVERTER_TRKHITCONVERTERPROCESSOR_H
#define TRKHITCONVERTER_TRKHITCONVERTERPROCESSOR_H

#include "marlin/Processor.h"

#include <EVENT/LCEvent.h>

#include <string>
#include <vector>

class TrkHitConverterProcessor : public marlin::Processor {
public:
  TrkHitConverterProcessor();

  TrkHitConverterProcessor(const TrkHitConverterProcessor &) = delete;
  TrkHitConverterProcessor &
  operator=(const TrkHitConverterProcessor &) = delete;

  virtual marlin::Processor *newProcessor() {
    return new TrkHitConverterProcessor();
  }

  void init() override;
  void processEvent(EVENT::LCEvent *evt) override;

private:
  std::vector<std::string> m_inputHitCollNames{};
  std::vector<std::string> m_inputTrackCollNames{};
  std::string m_outputSuffix{};
};

#endif // TRKHITCONVERTER_TRKHITCONVERTERPROCESSOR_H
