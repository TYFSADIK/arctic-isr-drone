# Arctic ISR Drone (build guide, status: planned)

Private research repo. A cold-weather Arctic ISR drone: Lepton thermal detection on a Hailo accelerator, georeferenced TAK markers, glove-friendly controls, and an honest spec-gap report.

Full write-up and phase plan: [`docs/project-page.md`](docs/project-page.md)

## What's here

| File | Purpose |
|---|---|
| `isr/thermal.py` | Radiometric hotspot detector and synthetic Arctic frames |
| `isr/georef.py` | Near-nadir georeferencing and error budget |
| `isr/cot.py` | CoT markers for ATAK |
| `isr/spec_gap.py` | Johnson-criteria detection, recognition, and identification ranges, rendered as a markdown spec-gap table |
| `isr/cold_ops.py` | Flight time vs temperature (placeholder curve) and glove UI layout checks |

## Quickstart

```bash
pip install -r requirements.txt
python demo.py && python -m unittest -v
```

## Phase checklist (from the build guide)
- [ ] Phase 0: SITL plus Gazebo with a thermal camera plugin, running the pipeline on simulated frames
- [ ] Phase 1: Lepton plus Hailo bench pipeline, measuring FPS and latency
- [ ] Phase 2: Cold rig. Replace `cold_ops.usable_capacity_fraction` with real data from `cold-soak-battery-rig`
- [ ] Phase 3: Flight with surveyed targets, reporting real detection range vs `spec_gap.max_range_m`
- [ ] Phase 4: Glove usability trials
- [ ] Phase 5: Publish the spec-gap table
