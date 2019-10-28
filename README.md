# Moon buggy robot with proximity detection

![The finished robot](robot-finished.jpeg)

Code and instructions for moon buggy robot with proximity detection.

## You will need

Equipment:

- [STS Pi robot](https://shop.pimoroni.com/products/sts-pi)
- [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) or [Pi Zero W](https://shop.pimoroni.com/products/raspberry-pi-zero-w)
- [Explorer pHAT](https://shop.pimoroni.com/products/explorer-phat)
- [Pico HAT Hacker](https://shop.pimoroni.com/products/pico-hat-hacker)
- 2x [male 2x20 GPIO header](https://shop.pimoroni.com/products/colour-coded-gpio-headers)
- [Male--to--female jumper jerky](https://shop.pimoroni.com/products/jumper-jerky-junior?variant=1076482177)
- [Female--to--female jumper jerky](https://shop.pimoroni.com/products/jumper-jerky-junior?variant=1076482185)
- [Proximity sensor](https://shop.pimoroni.com/products/adafruit-vcnl4040-proximity-and-lux-sensor-stemma-qt)
- USB cylindrical battery (I got the [cheapest one from Amazon I could find](https://www.amazon.co.uk/gp/product/B07KY63Z3R/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1))
- Micro SD card

Tools:

- Soldering iron (or get solderless equivalent headers)
- Flat--tip screwdriver
- [Anti--static wrist strap](https://shop.pimoroni.com/products/anti-static-wrist-strap) (optional but recommended)
- [Double--sided adhesive pads](https://www.amazon.co.uk/Sellotape-Permanent-Double-Sided-Sticky/dp/B004OHT7LS/ref=sxbs_bbp_recs_sx_w_p_v1?keywords=adhesive+pads&pd_rd_i=B004OHT7LS&pd_rd_r=20044f5f-d219-4ed1-9727-8bbff4120d2b&pd_rd_w=4boMm&pd_rd_wg=e2PTD&pf_rd_p=e6692ec6-496f-4aae-9035-49021365f38d&pf_rd_r=439N9P4EHGCF90QT6NBB&qid=1572294758) or similar for mounting

Notes:

- I suggest the wrist strap because the Raspberry Pi seems to be more sensitive to static shocks than regular computer hardware and I've fried a couple of (quite expensive) camera modules and my Pi Zero's WiFi module.
Proceed without a static strap at your own risk.
- You need to connect to your raspberry pi from another computer, so if you opt for a Pi Zero without wifi you will also need to connect to your router with a network cable and a [micro USB to ethernet adaptor](https://shop.pimoroni.com/products/three-port-usb-hub-with-ethernet-and-microb-connector).

## Hardware setup

1. Solder a male header to your Pi Zero as normal
1. Solder a male header to the **OUTSIDE** of the Pico HAT Hacker (see photos)
1. Place the Pico HAT Hacker on the Pi Zero header and solder in place. Be sparing with the solder to allow enough room for the Explorer pHAT to attach.

![Pi Zero with header and Pico HAT Hacker with additional header](pi-header-pico.jpeg)

1. Solder the headers to the Explorer pHAT (ensuring the double row of headers faces **DOWN**)

![Explorer pHAT with headers](explorer-phat-headers.jpeg)

1. Fit the Explorer pHAT to the GPIO pins as normal and press down firmly for a snug fit.

![Pi Zero with headers and explorer pHAT](pi-explorer.jpeg)
![Pi Zero with headers and explorer pHAT side profile](pi-explorer-profile.jpeg)

1. Solder the header to the proximity sensor
1. Set up the STS robot chassis following the instructions given, or have a look at the [build video](https://youtu.be/jHn3ZiPG69w)
1. Stick the proximity sensor to the camera mount and install the mount on the STS chassis
1. Mount the assembled pi zero to the chassis (I just used the double--sided adhesive pads)

## Wiring

1. The two motors are labelled on the chassis. Wire motor one to (you've guessed it) `Motors 1` on the explorer pHAT, and motor two to `Motors 2`, using the male--to--female jumper jerky. The polarity is indicated on the bottom of the motors. I tend to use red wires for `+` and whatever other colour I have for `-`.

![Motor polarity](motor-polarity.jpeg)

1. Now using female--to--female jumper jerky wire the sensor to the Pico HAT Hacker header.
    1. `Vin` is `+` and goes to pin `2` or `4` (one of the red pins)
    1. `GND` is ground and goes to pin `6` (black)
    1. `SDA` goes to pin `3` (labelled `DA`)
    1. `SCL` goes to pin `5` (labelled `CL`)

You can use this [explorer pHAT pinout to help](https://pinout.xyz/pinout/explorer_phat).
In the following images:

- red is `5V`/`Vin`
- brown is `Ground`/`GND`
- yellow is `DA`/`SDA`
- orange is `CL`/`SCL`

![Proximity sensor - Pi wiring](sensor-wiring-pi.jpeg)
![Proximity sensor - sensor wiring](sensor-wiring.jpeg)

## Software

1. Connect your Pi to your network.
    1. If you're using a Zero W you can [follow this guide to connect to your wifi and enable ssh](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/)
    1. If you're using a non--W Zero you can connect your network adaptor to the pi via your micro--USB to ethernet adaptor
    1. Either way, you need to enable ssh by creating a blank file called `ssh` in the `boot` partition
1. Turn on your Pi and ssh in. Open a terminal (or terminal emulator) and type in `ssh pi@192.168.xxx.xxx` (you can get the full ip address from your network router's 'devices' page)
