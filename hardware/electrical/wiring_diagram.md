# Breadboard Wiring Guide

## Components
- Seeed XIAO ESP32-S3
- Full-size breadboard (830 tie points)
- LED (any colour) + 330 Ω resistor
- 28BYJ-48 stepper motor + ULN2003 driver board
- Jumper wires

---

## LED Circuit

```
ESP32-S3 GPIO21 ──── 330 Ω ──── LED anode (+)
                                LED cathode (−) ──── GND rail
```

1. Insert the LED into the breadboard (longer leg = anode).
2. Connect a 330 Ω resistor between GPIO21 and the LED anode.
3. Connect the LED cathode to the breadboard GND rail.
4. Connect the XIAO GND pin to the GND rail.

---

## Stepper Motor Circuit (ULN2003 driver board)

```
ESP32-S3 GPIO1 ──── IN1 (ULN2003)
ESP32-S3 GPIO2 ──── IN2 (ULN2003)
ESP32-S3 GPIO3 ──── IN3 (ULN2003)
ESP32-S3 GPIO4 ──── IN4 (ULN2003)

ULN2003 VCC ──── 5 V supply (external or USB 5 V)
ULN2003 GND ──── GND (shared with ESP32-S3)
28BYJ-48 connector ──── ULN2003 output header
```

> **Important:** The 28BYJ-48 requires ~5 V; use an external 5 V supply and
> share a common GND with the XIAO ESP32-S3.

---

## Power

- XIAO ESP32-S3 powered via USB-C.
- Stepper motor powered from the same USB 5 V bus or a separate 5 V/1 A supply.
- Do **not** draw stepper current through the XIAO 3.3 V regulator.
