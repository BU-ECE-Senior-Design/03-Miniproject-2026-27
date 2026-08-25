# Enclosure Design Notes

## Requirements

1. **Dimensions** – Internal cavity ≥ 180 mm × 80 mm × 50 mm to accommodate:
   - Full-size breadboard (165 mm × 55 mm footprint)
   - XIAO ESP32-S3 module
   - ULN2003 driver board
   - Cable routing clearance

2. **Motor integration** – Mount the 28BYJ-48 stepper motor through a circular
   cutout (diameter 28 mm, shaft cutout 5 mm) on one face.  Four M3 mounting
   holes on a 35 mm bolt circle.

3. **Lid** – Removable top panel secured with four M3 × 8 mm pan-head screws
   into M3 heat-set inserts in the base.

4. **Ventilation** – Two 10 mm × 30 mm rectangular slots on opposite walls to
   allow passive airflow over the driver board.

5. **Cable entry** – A USB-C shaped slot (14 mm × 10 mm) centred on one short
   wall to accommodate the cable plug and strain-relief overmould.

6. **LED window** – 6 mm circular hole in the lid, aligned with the LED on the
   breadboard.

## Recommended Materials

| Option | Pros | Cons |
|--------|------|------|
| PLA (FDM 3-D print) | Low cost, easy to iterate | Lower impact resistance |
| PETG (FDM 3-D print) | Better temperature tolerance | Slightly harder to print |
| Laser-cut acrylic | Precise, transparent option | Requires assembly with fasteners |

## Fabrication Notes

- Wall thickness: **2 mm** minimum (3 mm recommended for rigidity).
- Layer height (if 3-D printed): 0.2 mm for structural parts.
- All internal edges that contact the PCB should be chamfered or have standoffs
  to avoid short circuits.
- Export final CAD in STEP and STL formats; include source files (`.f3d`,
  `.FCStd`, or equivalent).
