# Project Overview

## Goal

Design, build, and program an embedded system on a breadboard using the
**Seeed XIAO ESP32-S3** microcontroller. The system will:

1. Drive an **LED** (on/off, blink) via MicroPython.
2. Control a **stepper motor** (forward/reverse, angle-based movement).
3. Be housed in a custom **enclosure** designed by the mechanical sub-team.

## Team Responsibilities

### Mechanical Engineers (×2)
- Design the enclosure to satisfy the constraints in `hardware/mechanical/enclosure_notes.md`.
- Fabricate the enclosure (3-D print or laser-cut).
- Document the assembly process in `hardware/mechanical/assembly_guide.md`.

### Electrical Engineers (×2)
- Produce the breadboard wiring diagram (`hardware/electrical/wiring_diagram.md`).
- Maintain the bill of materials (`hardware/electrical/bom.csv`).
- Validate voltage levels and current budgets.

### Computer Engineers (×2)
- Develop and maintain MicroPython firmware in `firmware/`.
- Flash and test the firmware on the XIAO ESP32-S3.
- Document the API in `firmware/README.md`.

## Timeline (suggested)

| Week | Milestone |
|------|-----------|
| 1 | Kickoff, component ordering, repo structure agreed |
| 2 | Breadboard prototype assembled; LED blinking |
| 3 | Stepper motor controlled; enclosure design finalised |
| 4 | Enclosure fabricated; all sub-systems integrated |
| 5 | Final testing, documentation, demo |

## Deliverables

- [ ] Functional MicroPython firmware
- [ ] Completed breadboard assembly per wiring diagram
- [ ] Fabricated and assembled enclosure
- [ ] Full documentation in this repository
- [ ] Live demonstration to the class
