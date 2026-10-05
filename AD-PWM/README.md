# Module AD-PWM : Analogique, PWM et Buzzer

Ce dossier contient les projets et notions fondamentales sur l'utilisation des signaux analogiques, de la modulation de largeur d'impulsion (PWM) et du buzzer avec le Raspberry Pi Pico.

## 1. Le Capteur d'Angle Rotatif (Potentiomètre)
* Le potentiomètre modifie sa valeur de résistance en fonction de la rotation de son bouton de réglage.
* Il permet d'entrer des signaux analogiques de différentes valeurs.
* Le Raspberry Pi Pico ne pouvant traiter directement que les signaux numériques (0 et 1), il utilise un **ADC (Analog to Digital Converter)** pour convertir les signaux analogiques.
* Sur le Pico, les canaux ADC sont situés sur les broches GP26, GP27 et GP28, connectées aux ports A0, A1 et A2 du Shield.
* La fonction `read_u16()` permet de lire la valeur de retour du capteur sous forme d'un entier binaire non signé sur 16 bits, variant de 0 à 65535.

## 2. La Modulation de Largeur d'Impulsion (PWM)
* Le Pico ne possédant pas de convertisseur numérique-analogique (DAC) natif, il doit utiliser la **PWM (Pulse Width Modulation)** pour contrôler les circuits analogiques.
* Le signal PWM est un signal d'impulsion numérique envoyé selon des motifs périodiques continus d'état haut et bas.
* Il est défini par trois composantes principales : le cycle, le **rapport cyclique** (*duty cycle*) et la **fréquence**.
* Le rapport cyclique représente le rapport entre le temps à l'état haut et la durée totale du cycle.
* La fonction `duty_u16()` permet de modifier le rapport cyclique du signal PWM.

## 3. Le Buzzer Passif
* Le buzzer passif ne possède pas de source d'oscillation interne.
* Il ne peut fonctionner qu'en recevant un signal PWM externe (sous forme d'onde carrée) pour créer un champ magnétique alternatif et faire vibrer l'appareil.
* En ajustant la **fréquence** du signal PWM à l'aide de la fonction `freq()`, on peut contrôler la tonalité (la hauteur du son) du buzzer.
* En ajustant le **rapport cyclique** à l'aide de la fonction `duty_u16()`, on peut contrôler le volume sonore du buzzer.
