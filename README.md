# TrkHitConverter

A simple processor that converts `TrackerHitPlane`s into `TrackerHit`s such that
they can then be more easily converted to EDM4hep. This is necessary, since it
is not yet possible to attach `TrackerHitPlane`s to a `Track` in EDM4hep. The
processor takes collections of `TrackerHitPlane`s as well as `Track`s as input
and first converts all hits and tracks, before re-establishing the same
relations as in the input collections. The newly created collections are then
stored as ouputs with a configurable suffix. The MarlinWrapper config looks like
this (assuming MuonCollider default reco collection names):

```python
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
```

## Setup

Assuming that you are in an environment that roughly resembles a Key4hep one,
the following steps should do the trick to build and install the processor

```bash
mkdir build && cd build
cmake .. -GNinja -DCMAKE_INSTALL_PREFIX=../install
ninja install
```

Afterwards it is necessary to adjust the `MARLIN_DLL` path variable (assuming
you are still in the `build` directory and also that this is a Debian based
system. You might have to replace `lib` with `lib64` below, depending on where
the library is actually installed to)

```bash
export MARLIN_DLL=$(realpath ../install/lib/libTrkHitConverter.so):$MARLIN_DLL
```

## Example steering file
An example steering file, derived from the nominal reconstruction steering file
for the MuonCollider can be found in the `scripts` directory.
