"""
main.py – Entry point for the Seeed XIAO ESP32-S3 MicroPython firmware.

This script runs automatically at boot.  It demonstrates:
  • Blinking an LED connected to GPIO 21.
  • Rotating a stepper motor 90° forward and then 90° backward.

Pin assignments
---------------
LED       → GPIO 21 (change LED_PIN as needed)
Stepper   → GPIO 1, 2, 3, 4 (IN1–IN4 on the driver board)
"""

from led import LED
from stepper import StepperMotor

# ---------------------------------------------------------------------------
# Pin configuration – adjust to match your wiring
# ---------------------------------------------------------------------------
LED_PIN = 21
STEPPER_PINS = (1, 2, 3, 4)  # IN1, IN2, IN3, IN4

# ---------------------------------------------------------------------------
# Initialise peripherals
# ---------------------------------------------------------------------------
led = LED(pin=LED_PIN)
motor = StepperMotor(pins=STEPPER_PINS, steps_per_rev=512, step_delay_ms=2)

# ---------------------------------------------------------------------------
# Main routine
# ---------------------------------------------------------------------------
print("System ready.")

# Indicate startup with 3 quick blinks
led.blink(times=3, period_ms=300)

# Rotate the motor 90° forward …
print("Rotating 90° forward …")
led.on()
motor.move_degrees(90)
led.off()

# … and back again
print("Rotating 90° backward …")
led.on()
motor.move_degrees(-90)
led.off()

print("Done.")
