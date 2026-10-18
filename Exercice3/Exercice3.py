from lcd1602 import LCD1602
from dht20 import DHT20
from machine import I2C, Pin, ADC, PWM
import time

buzzer = PWM(Pin(16))
RAS = ADC(0)
led = Pin(18, machine.Pin.OUT)
led.value(0)

i2c1 = I2C(1)
dht20 = DHT20(i2c1)

i2c0 = I2C(0, scl=Pin(9), sda=Pin(8))
d = LCD1602(i2c0, 2, 16)
d.display()
derniertemps = time.ticks_ms()

while True:
    tempsboucle = time.ticks_ms()
    
    raw = RAS.read_u16()
    tempconsigne = round(int((raw / 65535) * 20) + 15)
    alarm = tempconsigne + 3
    
    temper = round(dht20.dht20_temperature())
    humidity = round(dht20.dht20_humidity())
    
    print("Consigne:", tempconsigne, "| Ambiant:", temper, "| Alarm:", alarm)
    
    time.sleep(1)
    d.clear()
    d.setCursor(0, 0)
    d.print("Ambient :" + str(temper) + "°C")
    d.setCursor(0, 1)
    
    if temper > alarm:
        buzzer.freq(1000)
        buzzer.duty_u16(500) 
        d.setCursor(0, 1)
        d.print("ALARM")
        
        if tempsboucle - derniertemps > 1000:
            led.value(0)
            derniertemps = time.ticks_ms()
        if tempsboucle - derniertemps > 500:
            led.value(1)
            
    elif temper > tempconsigne:
        buzzer.duty_u16(0)    
        d.setCursor(0, 1)
        d.print("Set :" + str(tempconsigne) + "°C")
        
        if tempsboucle - derniertemps > 2000:
            led.value(0)
            derniertemps = time.ticks_ms()
        if tempsboucle - derniertemps > 1000:
            led.value(1)
            
    else:
        buzzer.duty_u16(0)    
        d.setCursor(0, 1)
        d.print("Set :" + str(tempconsigne) + "°C")
        led.value(0)          
            

        
