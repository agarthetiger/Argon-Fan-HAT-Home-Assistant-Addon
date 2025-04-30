import time
import sys
import os
import json

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

from waveshare_pwm_fan_hat import PwmFanHat

logging.basicConfig(level=logging.INFO)

pfh = PwmFanHat.PwmFanHat()

f = open("/data/options.json", "r")
config = json.load(f)
fan_temp = config["fan_temp"]
delta_temp = config["delta_temp"]
sleep_duration = config["sleep_duration"]
f.close()

try:
    while(1):
        pfh.update(
            fan_temp=fan_temp,
            delta_temp=delta_temp,
            sleep_duration=sleep_duration
        )
        time.sleep(1)

# except IOError as e:
#     oled.Closebus()
#     print(e)

# except KeyboardInterrupt:
#     print("ctrl + c:")
#     oled.Closebus()

except KeyboardInterrupt:
    print("ctrl + c:")
    pfh.fan_off()
