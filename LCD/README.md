## L'écran LCD (Liquid-Crystal Display)

### Comment il fonctionne
L'écran LCD fonctionne grâce à des molécules de cristaux liquides qui modifient la direction de la lumière lorsqu'elles sont soumises à un champ électrique (tension). Étant donné que le cristal liquide ne produit aucune lumière par lui-même, un panneau de rétroéclairage est nécessaire pour servir de source lumineuse. Des filtres polariseurs sont placés de part et d'autre pour bloquer la lumière indésirable et générer l'affichage final.

Le module **Grove - 16x2 LCD** permet d'afficher un total de 32 caractères, répartis sur 2 lignes de 16 caractères chacune. Il communique avec le microcontrôleur en utilisant le bus **I2C**, un protocole qui transmet les informations via seulement deux lignes :
*   **SCL** : une ligne d'horloge.
*   **SDA** : une ligne de données.

---

### Éléments principaux du code

Pour faire fonctionner l'écran LCD avec le Raspberry Pi Pico en MicroPython, le code doit s'articuler autour de bibliothèques spécifiques et de commandes d'initialisation.

#### 1. Importation des bibliothèques
Le programme nécessite les bibliothèques standards `machine` (pour les fonctionnalités I2C et Pin) et `utime` (pour gérer le temps), ainsi qu'une bibliothèque externe nommée `lcd1602.py` qu'il faut préalablement sauvegarder sur le Pico.

```python
from lcd1602 import LCD1602
from machine import I2C, Pin
from utime import sleep
```

#### 2. Initialisation du bus I2C et création de l'objet LCD
Il est impératif de configurer les broches SCL et SDA ainsi que la fréquence de communication. L'écran est ensuite initialisé en transmettant la configuration I2C, le nombre de lignes (2) et le nombre de caractères par ligne (16).

```python
# Initialisation du bus I2C
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Création de l'objet LCD
d = LCD1602(i2c, 2, 16)
```

#### 3. Commandes de contrôle et d'affichage
Voici les commandes principales pour interagir avec l'écran :

*   `d.display()` : Active l'affichage de l'écran LCD.
*   `d.clear()` : Efface le contenu actuel de l'écran et replace le curseur à sa position initiale.
*   `d.setCursor(col, row)` : Place le curseur à une position précise pour démarrer l'écriture. Les index des colonnes et des lignes commencent à 0.
*   `d.print('texte')` : Affiche les caractères sur l'écran. **Attention**, cette fonction n'accepte que des chaînes de caractères ; les données numériques doivent être converties à l'aide de la fonction `str()` (par exemple `str(valeur)`) avant d'être affichées.

#### 4. Intégration dans une boucle
Ces blocs de code peuvent être intégrés dans une boucle `while True:` couplée à une commande de délai `sleep()` pour rafraîchir en continu les données affichées sur l'écran.

```python
d.display()

while True:
    d.clear()
    
    # Affichage sur la première ligne
    d.setCursor(0, 0)
    d.print("Temp: 25")
    
    # Affichage sur la deuxième ligne avec conversion d'une donnée numérique
    d.setCursor(0, 1)
    humidite = 40
    d.print("Humid: " + str(humidite))
    
    sleep(1)
```
