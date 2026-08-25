# 03-Miniproject-2026-27

A multi-disciplinary mini-project for a small team of EEs, CEs, and
MEs. The project programs a micro using MicroPython to maintain
timing, sense digital input, and move a mechanical actuator. The
components are assembled on a breadboard. If there are MEs on the
team, a custom enclosure is required.

See the assignment description for detail and prompts.

---

## Team

| Role | Named Members |
|------|---------|
| Mechanical Engineering | |
| Electrical Engineering | |
| Computer Engineering | |
| Biomedical Engineering | |

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
| Thing 2 | Thing 2 notes  |

---

## Getting Started with the micro

### Prerequisites
- Visit [Thonny.org](https://thonny.org) and install Thonny for your computer’s operating system
- Visit [MicroPython.org](https://micropython.org/download/ESP32_GENERIC_S3/) and select the appropriate bin file (currently v1.28.0)
- Open Thonny, go to tools > options > interpreter, and select MicroPython (ESP32). Click on install or update firmware, select your ESP32’s COM port, browse to your .bin file and click install.
- There are additional details here if you are having issues: https://wiki.seeedstudio.com/xiao_esp32s3_with_micropython/
- Find and open the test program (blink-seeed.py) program inside Thonny.  Run the test program to blink the on-board LED
- As of 9/1/26


---

## Team Responsibilities 
Any discipline can do any role here.

### Mechanical oriented
- Design the enclosure 
- Fabricate the enclosure (3-D print or laser-cut)
- Document the assembly process 

### Electrical oriented
- Produce the breadboard schematic
- Summarize the bill of materials
- Wire the circuit on the breadboard, verfify that the componets are assembled correctly, validate the voltage levels

### Computer oriented
- Design the software based on the required functionality
= Develop MicroPython code and firmware 
- Flash and test the firmware on the target micro
- Document the APIs for the system

## Deliverables

- [ ] Functional MicroPython firmware
- [ ] Completed breadboard assembly per schematic
- [ ] Fabricated and assembled enclosure (if MEs on team)
- [ ] Documentation in this repository
- [ ] Video recording demonstrating required function

## Contribution Workflow

We want each team member to contribute work products and to host these
including documentation in the repo with version control (software,
firmware, schematics, BOMs, CAD models, etc.) All can be managed in
the repo with version control.

1. Decompose the project into units to assign to each named team member 
2. Team members do the work and produce work artifiacts
3. Create a branch from `main` named `<role>/<feature>` (e.g., `me/case`) to capture work artifacts
3. Commit changes with descriptive messages
4. Open a pull request and request review from at least one other team member
5. Merge after approval
6. Follow the prompts in the assignment

---

