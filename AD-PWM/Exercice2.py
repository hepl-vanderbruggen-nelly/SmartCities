from machine import Pin, PWM, ADC
from time import sleep

RAS = ADC(0)  
buzzer = PWM(Pin(27))


def DO(time):
    global vol
    buzzer.freq(1046)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def RE(time):
    global vol
    buzzer.freq(1175)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def MI(time):
    global vol
    buzzer.freq(1318)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def FA(time):
    global vol
    buzzer.freq(1397)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def SO(time):
    global vol
    buzzer.freq(1568)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def LA(time):
    global vol
    buzzer.freq(1760)
    raw = RAS.read_u16()
    vol = int((raw / 65535)* 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def SI(time):
    global vol
    buzzer.freq(1967)
    raw = RAS.read_u16()
    vol = int((raw / 65535) * 5000) 
    buzzer.duty_u16(vol)
    sleep(time)


def N(time):
    buzzer.duty_u16(0)
    sleep(time)


while True:
    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)
    N(0.01)

    DO(0.25)
    RE(0.25)
    MI(0.25)
    DO(0.25)

    MI(0.25)
    FA(0.25)
    SO(0.5)

    MI(0.25)
    FA(0.25)
    SO(0.5)
    N(0.01)

    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)

    SO(0.125)
    LA(0.125)
    SO(0.125)
    FA(0.125)
    MI(0.25)
    DO(0.25)

    RE(0.25)
    SO(0.25)
    DO(0.5)
    N(0.01)

    RE(0.25)
    SO(0.25)
    DO(0.5)
    
    
    