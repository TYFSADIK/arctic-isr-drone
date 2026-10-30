"""Run: python demo.py  -> spec-gap table, cold flight time, and one georeferenced TAK marker."""
from isr.cold_ops import flight_time_min
from isr.cot import cot_marker
from isr.georef import Pose, pixel_to_ground
from isr.spec_gap import markdown, table
from isr.thermal import find_hotspots, synthetic_frame

print(markdown(table({("person", "detect"): 500, ("person", "recognise"): 150, ("vehicle", "detect"): 1500})))
for t in (20, -10, -30):
    print(f"{t:>4} C: {flight_time_min(25, t):.1f} min unheated, {flight_time_min(25, t, heated=True):.1f} min heated")

pose = Pose(lat=69.117, lon=-105.06, agl_m=100, yaw_deg=0)   # Cambridge Bay area, example only
h = find_hotspots(synthetic_frame(people=((100, 40),), background_c=-28))[0]
lat, lon, gsd = pixel_to_ground(h.cx, h.cy, pose)
print(f"hotspot -> {lat:.6f},{lon:.6f}  GSD {gsd:.2f} m/px")
print(cot_marker(lat, lon, "ISR-1", f"thermal {h.peak_c:.0f}C")[:100], "...")
