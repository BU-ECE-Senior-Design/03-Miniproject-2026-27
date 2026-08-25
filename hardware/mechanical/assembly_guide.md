# Enclosure Assembly Guide

## Tools Required
- Phillips-head screwdriver (PH1)
- M3 × 8 mm pan-head screws (×4)
- Soldering iron (for heat-set inserts, if 3-D printed)
- Double-sided foam tape

## Steps

### 1 – Prepare the base
1. Insert four M3 heat-set inserts into the base lid posts (if 3-D printed).
2. Sand any rough edges with 220-grit sandpaper.

### 2 – Mount the stepper motor
1. Pass the motor's output shaft through the circular cutout on the motor-face wall.
2. Secure with four M3 × 6 mm screws through the motor flange.
3. Route the motor cable through the internal cable channel.

### 3 – Mount the breadboard
1. Peel the backing from the breadboard's self-adhesive pad.
2. Press firmly onto the enclosure floor, aligned to the printed standoff outline.

### 4 – Install electronics
1. Seat the XIAO ESP32-S3 on the breadboard (top-left corner, pins facing inward).
2. Place the ULN2003 driver board and connect per the wiring diagram.
3. Route the USB-C cable through the cable-entry slot and connect to the XIAO.

### 5 – Close the enclosure
1. Verify all wires are clear of the lid perimeter.
2. Place the lid and align the four screw holes.
3. Insert and tighten M3 × 8 mm screws – finger-tight, then a ¼ turn.

### 6 – Verify operation
1. Connect USB-C power.
2. Confirm the LED blinks 3× on startup.
3. Confirm the stepper motor completes its 90° sweep.
