# Electrical Hardware

## Contents

| File / Folder | Description |
|---------------|-------------|
| `wiring_diagram.md` | Breadboard wiring instructions |
| `bom.csv` | Bill of Materials |

---

## Wiring Diagram

See `wiring_diagram.md` for step-by-step breadboard connections.

## Bill of Materials

See `bom.csv` for the full component list with part numbers and quantities.

## Notes

- All logic runs at 3.3 V – do **not** connect 5 V signals directly to the XIAO ESP32-S3.
- Place a 330 Ω current-limiting resistor in series with the LED.
- Use a ULN2003 driver board (or equivalent Darlington array) between the ESP32-S3 and the stepper motor coils.
