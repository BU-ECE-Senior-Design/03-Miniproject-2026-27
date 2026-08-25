# Firmware – Seeed XIAO ESP32-S3 (MicroPython)

## Overview

| File | Purpose |
|------|---------|
| `main.py` | Entry point; runs at boot |
| `led.py` | LED driver class |
| `stepper.py` | Stepper motor driver class |

## MicroPython Setup

1. Download the latest MicroPython `.bin` for ESP32-S3 from  
   <https://micropython.org/download/ESP32_GENERIC_S3/>
2. Flash it with `esptool`:
   ```bash
   esptool.py --chip esp32s3 --port /dev/ttyUSB0 erase_flash
   esptool.py --chip esp32s3 --port /dev/ttyUSB0 write_flash -z 0x0 firmware.bin
   ```
3. Copy source files to the board:
   ```bash
   mpremote connect /dev/ttyUSB0 cp led.py :led.py
   mpremote connect /dev/ttyUSB0 cp stepper.py :stepper.py
   mpremote connect /dev/ttyUSB0 cp main.py :main.py
   ```
4. Reset the board – `main.py` runs automatically.

## Pin Assignments (defaults)

| Signal | GPIO |
|--------|------|
| LED | 21 |
| Stepper IN1 | 1 |
| Stepper IN2 | 2 |
| Stepper IN3 | 3 |
| Stepper IN4 | 4 |

Pin assignments can be changed in `main.py`.

## Module Reference

### `LED(pin, active_high=True)`
- `on()` / `off()` / `toggle()`
- `blink(times=3, period_ms=500)`

### `StepperMotor(pins, steps_per_rev=512, step_delay_ms=2, half_step=False)`
- `step(steps)` – move by an integer number of steps (negative = reverse)
- `move_degrees(degrees)` – rotate by a given angle
