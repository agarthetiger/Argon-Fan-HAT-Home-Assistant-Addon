class ArgonFanHat:



    def fan_set(self, pwm_percent):
        pwm.setServoPulse(0, pwm_percent)

    def set_fan_from_temp(self):
        temp = self.get_temp()

        if(temp > 40): # Default is 40 (degrees C)
            self.fan_set(20)
        elif(temp > 45):
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
