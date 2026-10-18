# Exercice 3 : Thermostat Intelligent avec Alarme

### 🎯 But de l'exercice
Ce code implémente un système de surveillance de température interactif (un thermostat intelligent). L'utilisateur peut régler une **température de consigne** (entre 15°C et 35°C) à l'aide d'un potentiomètre (capteur d'angle rotatif). Le système compare continuellement la température ambiante lue par le capteur DHT20 à cette consigne et réagit selon trois scénarios :
1. **Température normale** (Ambiante <= Consigne) : La LED est éteinte et l'écran affiche la consigne.
2. **Avertissement** (Ambiante > Consigne) : La LED clignote lentement (toutes les secondes).
3. **Alarme critique** (Ambiante > Consigne + 3°C) : Le buzzer émet un son continu, l'écran affiche "ALARM" et la LED clignote rapidement (toutes les demi-secondes).

---

### 🔌 Matériel et Connectique
* **Raspberry Pi Pico** (et son Grove Shield)
* **Buzzer** -> Broche `Pin 16`
* **LED** -> Broche `Pin 18`
* **Capteur d'angle rotatif (Potentiomètre)** -> Broche `ADC(0)` (souvent A0)
* **Capteur Température/Humidité DHT20** -> Bus `I2C1`
* **Écran LCD 16x2** -> Bus `I2C0` (SCL = `Pin 9`, SDA = `Pin 8`)

---

### 💻 Éléments principaux du code (MicroPython)

#### 1. Calcul de la température de consigne
La valeur brute lue par le potentiomètre varie de 0 à 65535. Le code la convertit proportionnellement en une température allant de 15°C à 35°C, puis définit le seuil d'alarme 3 degrés plus haut.
```python
raw = RAS.read_u16()
# Mise à l'échelle pour obtenir une température entre 15°C et 35°C
tempconsigne = round(int((raw / 65535) * 20) + 15)
alarm = tempconsigne + 3
```

#### 2. Affichage sur l'écran LCD
L'écran est mis à jour chaque seconde. Il affiche en permanence la température ambiante sur la première ligne, et bascule la deuxième ligne entre l'affichage de la consigne et le message d'alerte.
```python
d.setCursor(0, 0)
d.print("Ambient :" + str(temper) + "°C")
```

#### 3. Gestion non bloquante du temps (Clignotement LED)
Au lieu d'utiliser `time.sleep()` qui mettrait tout le programme en pause, le code utilise `time.ticks_ms()` pour mesurer le temps écoulé. Cela permet de faire clignoter la LED à différentes vitesses sans bloquer la lecture des capteurs.
```python
tempsboucle = time.ticks_ms()

# Exemple de clignotement rapide pour l'alarme (500 ms)
if tempsboucle - derniertemps > 1000:
    led.value(0)
    derniertemps = time.ticks_ms()
if tempsboucle - derniertemps > 500:
    led.value(1)
```
