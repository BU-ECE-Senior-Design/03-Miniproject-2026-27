"""
stepper.py – Unipolar/bipolar stepper motor driver for the Seeed XIAO ESP32-S3
             (MicroPython).

The driver supports full-step and half-step modes for a 4-wire stepper motor
(e.g., 28BYJ-48 with ULN2003 driver board or any 4-phase unipolar motor).

Usage example::

    from stepper import StepperMotor
    motor = StepperMotor(pins=(1, 2, 3, 4))
    motor.step(200)          # advance 200 steps forward
    motor.step(-100)         # reverse 100 steps
    motor.move_degrees(90)   # rotate 90 degrees (assumes 512 steps/rev)
"""

from machine import Pin
import time


# Full-step sequence (4 steps per electrical cycle)
_FULL_STEP_SEQ = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]

# Half-step sequence (8 steps per electrical cycle)
_HALF_STEP_SEQ = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1),
]


class StepperMotor:
    """
    Drives a 4-wire stepper motor using GPIO pins.

    :param pins: Tuple of 4 GPIO pin numbers (IN1, IN2, IN3, IN4).
    :param steps_per_rev: Number of full steps for one complete revolution.
                          Default is 512 (typical for 28BYJ-48 in full-step).
    :param step_delay_ms: Delay between steps in milliseconds.  Reduce for
                          higher speed; increase for more torque/reliability.
    :param half_step: Use half-step mode (smoother, 8 micro-steps per cycle).
    """

    def __init__(
        self,
        pins: tuple,
        steps_per_rev: int = 512,
        step_delay_ms: int = 2,
        half_step: bool = False,
    ):
        if len(pins) != 4:
            raise ValueError("Exactly 4 GPIO pin numbers are required.")
        self._pins = [Pin(p, Pin.OUT) for p in pins]
        self._steps_per_rev = steps_per_rev
        self._step_delay_ms = step_delay_ms
        self._sequence = _HALF_STEP_SEQ if half_step else _FULL_STEP_SEQ
        self._seq_len = len(self._sequence)
        self._position = 0  # current step index within the sequence
        self._release()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def step(self, steps: int) -> None:
        """
        Advance the motor by *steps* steps.

        Positive values move forward; negative values move in reverse.

        :param steps: Number of steps to move (may be negative).
        """
        direction = 1 if steps >= 0 else -1
        if steps == 0:
            return
        for _ in range(abs(steps)):
            self._position = (self._position + direction) % self._seq_len
            self._apply_step(self._position)
            time.sleep_ms(self._step_delay_ms)
        self._release()

    def move_degrees(self, degrees: float) -> None:
        """
        Rotate the motor shaft by a given angle in degrees.

        :param degrees: Angle to rotate (positive = forward, negative = reverse).
        """
        steps = int(round(degrees / 360.0 * self._steps_per_rev))
        self.step(steps)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _apply_step(self, index: int) -> None:
        for pin, value in zip(self._pins, self._sequence[index]):
            pin.value(value)

    def _release(self) -> None:
        """De-energise all coils to save power when idle."""
        for pin in self._pins:
            pin.value(0)
