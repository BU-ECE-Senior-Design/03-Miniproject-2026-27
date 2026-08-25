"""
led.py – Simple LED driver for the Seeed XIAO ESP32-S3 (MicroPython).

Usage example::

    from led import LED
    led = LED(pin=21)
    led.on()
    led.off()
    led.toggle()
    led.blink(times=5, period_ms=500)
"""

from machine import Pin
import time


class LED:
    """Controls a single LED connected to a GPIO pin."""

    def __init__(self, pin: int, active_high: bool = True):
        """
        Initialise the LED driver.

        :param pin: GPIO pin number the LED anode (or cathode) is connected to.
        :param active_high: Set to True if the LED is on when the pin is HIGH
                            (common for direct drive); False for active-low.
        """
        self._pin = Pin(pin, Pin.OUT)
        self._active_high = active_high
        self.off()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def on(self) -> None:
        """Turn the LED on."""
        self._pin.value(1 if self._active_high else 0)

    def off(self) -> None:
        """Turn the LED off."""
        self._pin.value(0 if self._active_high else 1)

    def toggle(self) -> None:
        """Toggle the LED state."""
        self._pin.value(not self._pin.value())

    def blink(self, times: int = 3, period_ms: int = 500) -> None:
        """
        Blink the LED a fixed number of times.

        :param times: Number of on/off cycles.
        :param period_ms: Total period of one cycle in milliseconds.
        """
        half = period_ms // 2
        for _ in range(times):
            self.on()
            time.sleep_ms(half)
            self.off()
            time.sleep_ms(half)
