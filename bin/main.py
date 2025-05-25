import logging
import os
import json
import sys
import time

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from argon_fan_hat import ArgonFanHat

logging.basicConfig(level=logging.INFO)

f = open("/data/options.json", "r")
config = json.load(f)
fan_on_temp = config["fan_on_temp"]
sleep_interval = config["sleep_interval"]
f.close()

version = "v0.0.5"
print(f"Starting Argon Fan HAT control AddOn ${version}")
afh = ArgonFanHat.ArgonFanHat(fan_on_temp)
print(f"Initialised Argon Fan HAT control AddOn ${version}")

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
