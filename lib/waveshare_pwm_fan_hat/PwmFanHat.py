import time
import socket
from PIL import Image,ImageDraw,ImageFont
from . import SSD1306
from . import PCA9685

# Initialize oled
oled = SSD1306.SSD1306()
oled.Init()
oled.ClearBlack()

pwm = PCA9685.PCA9685(0x40, debug=False)
pwm.setPWMFreq(80)
pwm.setServoPulse(0,100)

# Create blank image for drawing.
image1 = Image.new('1', (oled.width, oled.height), "WHITE")
draw = ImageDraw.Draw(image1)
font = ImageFont.load_default()
# dir_path = os.path.dirname(os.path.abspath(__file__))
# font = ImageFont.truetype(dir_path+'/Courier_New.ttf',13)

class PwmFanHat:

    def get_ip(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
        s.close()
        return ip

    def get_temp(self):
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = (int)(f.read() ) / 1000.0
        return temp

    def fan_off(self):
        pwm.setServoPulse(0,0)

    def update(self, fan_temp, delta_temp, sleep_duration):
        ip_address = self.get_ip()
        temp = self.get_temp()

        draw.rectangle((0,0,128,32), fill = 1)
        draw.text((0,0), "IP:", font=font, fill = 0)
        draw.text((20,0), ip_address, font=font, fill = 0)
        draw.text((0,16), "Temp(Celsius):", font=font, fill = 0)
        draw.text((85,16), str(temp), font=font, fill = 0)

        if(temp > 40):
            pwm.setServoPulse(0,40)
        elif(temp > 50):
            pwm.setServoPulse(0,50)
        elif(temp > 55):
            pwm.setServoPulse(0,75)
        elif(temp > 60):
            pwm.setServoPulse(0,90)
        elif(temp > 65):
            pwm.setServoPulse(0,100)
        else:
            pwm.setServoPulse(0,0)

        oled.ShowImage(oled.getbuffer(image1.rotate(180)))
        time.sleep(1)
