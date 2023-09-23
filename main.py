import time
from Lights import *
from Buzzer import *
from Displays import * 


time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

myled=Light(25, "Internal LED")
myled.on()
utime.sleep(5)
myled.off()

extled = DimLight(22, "Blue LED")
extled.on()
utime.sleep(1)
extled.setBrightness(100)
utime.sleep(1)
extled.off()
extled.upDown()

mybuzzer = PassiveBuzzer(16)
mybuzzer.beep()

mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
mydisplay.showText('I LOVE PYTHON!')