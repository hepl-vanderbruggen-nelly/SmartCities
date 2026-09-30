#Dossier GPIO

## Description du projet
Ce script en MicroPython permet de contrôler une **LED** (branchée sur la broche 16 en sortie) à l'aide d'un **bouton-poussoir** (branché sur la broche 18 en entrée). 

### Fonctionnement :
- **Compteur de modes (`val`) :** À chaque pression sur le bouton-poussoir, la variable `val` augmente de 1. Lorsqu'elle atteint 4, elle revient à 0 (ce qui éteint tout et réinitialise le cycle).
- **Gestion du temps :** Le code utilise `time.ticks_ms()` pour mesurer le temps qui s'écoule sans bloquer le programme.
- **Anti-rebond :** Une petite boucle d'attente (`time.sleep_ms(10)`) est intégrée lors de l'appui pour éviter les lectures parasites.

### Les différents états :
- **`val == 0` :** La LED est éteinte.
- **`val == 1` :** Clignotement lent (alternance toutes les secondes).
- **`val == 2` :** Clignotement moyen (alternance toutes les 500 ms).
- **`val == 3` :** Clignotement rapide (alternance toutes les 250 ms).

##Code source :


import machine
import time
 
led = machine.Pin(16, machine.Pin.OUT)
button = machine.Pin(18, machine.Pin.IN)
 
val = 0
tempsfrequenc1 = 0
led.value(0)
 
while True:
    tempsboucle = time.ticks_ms()
 
    if button.value() == 1:
        val = val + 1
        print("Nombre d'appuis :", val)
        tempsfrequenc1 = time.ticks_ms()

        while button.value() == 1:
            time.sleep_ms(10)

    if val >= 4:
        val = 0

    if val == 1:
        if tempsboucle - tempsfrequenc1 > 2000:
            led.value(0)
            tempsfrequenc1 = time.ticks_ms()
        if tempsboucle - tempsfrequenc1 > 1000:
            led.value(1)

    elif val == 2:
        if tempsboucle - tempsfrequenc1 > 500:
            led.value(0)
            tempsfrequenc1 = time.ticks_ms()
        if tempsboucle - tempsfrequenc1 > 250:
            led.value(1)

    elif val == 3:
        led.value(0)
