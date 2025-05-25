from . import PCA9685

class ArgonFanHat:

    def __init__(self, fan_on_temp):
        self.fan_on_temp = fan_on_temp
        self.pwm = PCA9685.PCA9685(0x40, debug=False)
        self.pwm.setPWMFreq(80)
        self.fan_set(50)

    def get_temp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = (int)(f.read() ) / 1000.0
        return temp

    def fan_set(self, pwm_percent):
        self.pwm.setServoPulse(0, pwm_percent)

    def set_fan_from_temp(self):
        temp = self.get_temp()

        if(temp > self.fan_on_temp): # Default is 40 (degrees C)
            self.fan_set(40)
        elif(temp > 50):
            self.fan_set(50)
        elif(temp > 55):
            self.fan_set(75)
        elif(temp > 60):
            self.fan_set(90)
        elif(temp > 65):
            self.fan_set(100)
        else:
            self.fan_set(0)
