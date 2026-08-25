# 03-Miniproject-2026-27

A multi-disciplinary mini-project for two mechanical engineers, two electrical engineers, and two computer engineers. The project programs a **Seeed XIAO ESP32-S3** using **MicroPython** to drive an LED and a stepper motor, assembled on a breadboard and housed in a custom enclosure.

---

## Team

| Role | Members |
|------|---------|
| Mechanical Engineering | ME-1, ME-2 |
| Electrical Engineering | EE-1, EE-2 |
| Computer Engineering | CE-1, CE-2 |

---

## Repository Structure

```
.
├── firmware/          # MicroPython source code for the XIAO ESP32-S3
│   ├── main.py        # Entry point – initialises LED and stepper motor
│   ├── led.py         # LED driver module
│   └── stepper.py     # Stepper motor driver module
├── hardware/
│   ├── electrical/    # Schematics, wiring diagrams, and BOM
│   └── mechanical/    # Enclosure CAD files and fabrication notes
└── docs/              # Project documentation and meeting notes
```

---

## Hardware

| Component | Notes |
|-----------|-------|
| Seeed XIAO ESP32-S3 | Main microcontroller |
| Breadboard | Prototyping platform |
| LED | Status indicator |
| Stepper motor | Actuation |
| Enclosure | Custom-built housing |

---

## Getting Started

### Prerequisites
- [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) or [Thonny IDE](https://thonny.org/) for flashing MicroPython
- MicroPython firmware for ESP32-S3 (see `firmware/README.md`)

### Flashing the firmware
```bash
# Copy all source files to the board
mpremote connect /dev/ttyUSB0 cp firmware/led.py :led.py
mpremote connect /dev/ttyUSB0 cp firmware/stepper.py :stepper.py
mpremote connect /dev/ttyUSB0 cp firmware/main.py :main.py
```

---

## Contribution Workflow

1. Create a branch from `main` named `<role>/<feature>` (e.g., `ce/stepper-driver`).
2. Commit changes with descriptive messages.
3. Open a pull request and request review from at least one other team member.
4. Merge after approval.

---

## License

This project is for educational purposes within Boston University ECE Senior Design.
