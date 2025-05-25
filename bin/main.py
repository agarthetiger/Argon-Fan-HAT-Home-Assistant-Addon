import logging
import os
import json
import sys
import time

version = "v0.0.7"

logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M",
    format="{asctime} - {levelname} - {message}",
    level=logging.DEBUG,
    style="{",
)

logging.info(f"Starting Argon Fan HAT control AddOn ${version}")

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from argon_fan_hat import ArgonFanHat

f = open("/data/options.json", "r")
config = json.load(f)
fan_on_temp = config["fan_on_temp"]
sleep_interval = config["sleep_interval"]
f.close()

afh = ArgonFanHat.ArgonFanHat(fan_on_temp)
logging.info(f"Initialised Argon Fan HAT control AddOn ${version}")

try:
    while(1):
        afh.set_fan_from_temp()
        time.sleep(sleep_interval)

# except IOError as e:
#     oled.Closebus()
#     print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    afh.fan_50()
