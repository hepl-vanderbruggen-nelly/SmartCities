# Dossier AD-PWM - Gestion d'un buzzer et d'un potentiomètre

## Description du projet
Ce script en MicroPython permet de jouer une mélodie (**« Frère Jacques »**) sur un **buzzer passif** (branché sur la broche PWM 27), tout en contrôlant dynamiquement le volume sonore en temps réel à l'aide d'un **potentiomètre / capteur d'angle rotatif** (branché sur l'entrée analogique ADC 0).

### Fonctionnement :
- **Entrée analogique (ADC) :** Le script lit en continu la valeur brute du potentiomètre via `RAS.read_u16()` sur une plage de 0 à 65535.
- **Mise à l'échelle du volume :** La valeur brute est convertie mathématiquement en un pourcentage plafonné à un maximum de 5000 (`int((raw / 65535) * 5000)`), ce qui permet d'obtenir un son propre et agréable sans saturer le buzzer.
- **Gestion des notes et du PWM :** Chaque fonction de note (`DO`, `RE`, `MI`, etc.) définit la fréquence correspondante du signal carré (`buzzer.freq()`) et actualise instantanément le rapport cyclique (`buzzer.duty_u16()`) pour prendre en compte les mouvements du potentiomètre à chaque note.
- **Les silences (`N`) :** Une fonction dédiée coupe le signal du buzzer (`duty_u16(0)`) pour marquer de brefs temps de pause entre les notes.

## Code source

```python
from machine import ADC, PWM, Pin
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
    vol = int((raw / 65535) * 5000)
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
