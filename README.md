![Action Shot](/assets/bb6.png)


[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?style=flat&logo=youtube&logoColor=red&labelColor=white&color=ffed53)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ) [![Instagram](https://img.shields.io/github/stars/veebch?style=flat&logo=github&logoColor=black&labelColor=white&color=ffed53)](https://www.instagram.com/v_e_e_b/)

# BB

This is a fictional use case that's a basic introduction to working with a microcontroller. It combines a microcontroller with a stepper motor and a simple Python program. Assembly is easy and build time is an hour or so (3d print time not included). 

## You'll need:
- Raspberry Pi Pico or other 2040 microcontroller
- Stepper Motor and Driver Board (we use the 28BYJ-48 and ULN2003)
- 6 wires, ideally with female dupont connectors at one end
- 3d Printed parts (optional case in the directory [3d](./3d))
- A burning desire to turn a thing at roughly predefined intervals

## Video 

An overview of the build and a demo of it in action:

[![YouTube](http://i.ytimg.com/vi/LisX4vcqEus/hqdefault.jpg)](https://www.youtube.com/watch?v=LisX4vcqEus)

# Building One

## Powering the unit

You can power this via a Lipo Battery or a Powerbank.

If you want to use a Lipo Battery then there is plenty of space in the case to house one. You'll need to use some extra hardware to do so (eg adafruit micro lipo) or use a microcontroller that is compatible with a battery (PicoLipo, Waveshare RP2040 Plus etc)

If you're powering this project from a powerbank then make sure it's in low current mode, otherwise it will switch off due to low current required to power the Microcontroller
## Assembly

Connect Pico to the driver board. For the ULN2003 this means connecting the power pins to VSYS and GND and GPIO 21,20,19 and 18 to IN1, IN2, IN3 and IN4 respectively. You can also see this in the thumbnail for the video. 

The motor is then connected to the board and you're done, simply attach the pico and driver board to the case and place the lid on top. You can also clip the 3d printed cover on top of the motor and then the plate which gets stuck to the wheel on the back of the parking badge (we used velcro for this). 

Now secure the body of the ticket to the lid of the case you made for the pico/board. This means when the motor turns, only the dial moves. 

## Installing Code on Pico

Download a `uf2` image from the [Pimoroni github repository](https://github.com/pimoroni/pimoroni-pico/releases) and install it on the Pico according to the instructions. You need to use the Pimoroni image to be able to use Pimoroni drivers for the light sensor.

Clone this repository to your computer using the commands (from a terminal):

```
cd ~
git clone https://github.com/veebch/bb.git
cd bb
```

Check the port of the pico with the port listing command:
```
python -m serial.tools.list_ports
```
Now, using the port path (in our case `/dev/ttyACM0`) copy the contents to the repository by installing [ampy](https://pypi.org/project/adafruit-ampy/) and using the commandGG:

```
ampy -p /dev/ttyACM0 put main.py
```
(*nb. make sure you are using the right port name, as shown in the port listing command above*)

Done! The required file should now be on the Pico. Next time you plug in the pico to USB power the script will autorun.
