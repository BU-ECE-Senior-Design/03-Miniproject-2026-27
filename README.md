# 03-Miniproject-2026-27

A multi-disciplinary mini-project for a small team of EEs, CEs, and
MEs. The project programs a micro (Seeed XIAO ESP32-S3) using
MicroPython to drive a multicolor LED and a stepper motor, with two
buttons as input, and assembled on a breadboard. If MEs are on the
team, a custom enclosure is required.

---

## Team

| Role | Named Members |
|------|---------|
| Mechanical Engineering | |
| Electrical Engineering | |
| Computer Engineering | |

---

## Repository Structure

```
.
├── firmware/          # MicroPython source code for the XIAO ESP32-S3
├── hardware/
│   ├── electrical/    # Schematics, wiring diagrams, and BOM
│   └── mechanical/    # Enclosure CAD files and fabrication notes
└── docs/              # Project documentation and meeting notes
```

---

## Hardware

| Component | Notes |
|-----------|-------|
| Thing 1 | Thing 1 notes  |

---

## Getting Started

### Prerequisites
- Visit [Thonny.org](https://thonny.org) and install Thonny for your computer’s operating system
- Visit [MicroPython.org](https://micropython.org/download/ESP32_GENERIC_S3/) and select the appropriate bin file (currently v1.28.0)
- Open Thonny, go to tools > options > interpreter, and select MicroPython (ESP32). Click on install or update firmware, select your ESP32’s COM port, browse to your .bin file and click install.
- There are additional details here if you are having issues: https://wiki.seeedstudio.com/xiao_esp32s3_with_micropython/
- Find and open the test program (blink-seeed.py) program inside Thonny.  Run the test program to blink the on-board LED



---

## Contribution Workflow

1. Decompose the project into units to assign to each team member 
2. Create a branch from `main` named `<role>/<feature>` (e.g., `ce/stepper-driver`). Yes MEs too
3. Commit changes with descriptive messages
4. Open a pull request and request review from at least one other team member
5. Merge after approval
6. Follow the prompts in the assignment

---

