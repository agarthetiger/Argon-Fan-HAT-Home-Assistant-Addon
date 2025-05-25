# Argon Fan HAT Home-Assistant Addon

Home Assistant (HASS) Addon to fully support the Argon Fan HAT, for CPU temperature-based variable fan speed.

This is specifically for this HAT: <https://argon40.com/en-gb/products/argon-fan-hat>.

The fan speed varies based on the CPU temperature.

| CPU Temp (Centigrade) | Fan Speed (% of max speed) |
|------|-----|
| <40 C | 0% |
| 40 C | 20% |
| 45 C | 40% |
| 50 C | 50% |
| 55 C | 75% |
| 60 C | 90% |
| 65 C | 100% |

Important: This Fan HAT requires I2C enabled to make this work. This can be done in a couple of ways, either as described at <https://www.home-assistant.io/common-tasks/os/#enable-i2c> or use the HassOS I2C Configurator from <https://github.com/adamoutler/HassOSConfigurator>. Personally I've had success and found this easier with the HASS OS Configurator.
