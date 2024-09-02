[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?style=flat&logo=youtube&logoColor=red&labelColor=white&color=ffed53)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ) [![Instagram](https://img.shields.io/github/stars/veebch?style=flat&logo=github&logoColor=black&labelColor=white&color=ffed53)](https://www.instagram.com/v_e_e_b/)

# BB

This is a fictional use case for a simple few lines of code, a microcontroller and a stepper motor.

## You'll need:
- Raspberry Pi Pico or other 2040 microcontroller
- Stepper Motor and Driver Board (we use the 28BYJ-48 and ULN2003)
- 6 wires, ideally with female dupont connectors at one end
- An application that requires turning a thing at roughly predefined intervals
- 3d Printed parts (optional case in [3d](./3d))

## Power

You can power this via a Lipo Battery or a Powerbank.

If you want to use a Lipo Battery then there is plenty of space in the case to house one. You'll need to use some extra hardware to do so (or use a microcontroller that is compatible with a battery (PicoLipo, Waveshare RP2040 Plus etc)

If you're powering this project from a powerbank then make sure it's in low current mode, otherwise it will switch off due to low current required to power the Microcontroller
