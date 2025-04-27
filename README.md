# Waveshare PWM Controlled Fan HAT Home-Assistant Addon (forked from fork of original)

_Note this fork is a work in progress, and is not yet ready for use._

Specifically for this PoE-HAT: <https://www.waveshare.com/wiki/Fan_HAT>

Home Assistant (HASS) Addon to support the Waveshare PWM Controlled Fan HAT

This is a fork of tgryphon fork, which fixed problems with reschix's original which started to throw errors after July 2023. Both those add-ons were for a different Waveshare HAT and don't work without some modification which I hope to make win this repo. 

Important: Enable I2C first to make this work. This can be done in a couple of ways, either as described at <https://www.home-assistant.io/common-tasks/os/#enable-i2c> or use the HassOS I2C Configurator from <https://github.com/adamoutler/HassOSConfigurator>.
