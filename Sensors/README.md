## Le capteur de Température et d'Humidité (DHT20)

### Comment il fonctionne

Un capteur de température et d'humidité permet, comme son nom l'indique, de détecter ces deux grandeurs physiques dans l'environnement. Le **DHT20** est la version nouvelle et améliorée de l'ancien modèle DHT11. 

Comparé à son prédécesseur, le DHT20 offre de nets avantages : une plus grande précision, une plage de mesure plus large, une consommation d'énergie réduite et une excellente stabilité. La plus grande différence réside dans sa communication : il utilise désormais une interface numérique entièrement calibrée qui communique via le **bus I2C** avec le microcontrôleur.

### Éléments principaux du code

Pour faire fonctionner le capteur DHT20 avec le Raspberry Pi Pico en MicroPython, vous devez utiliser des bibliothèques spécifiques pour la communication I2C et la lecture des données.

#### 1. Importation des bibliothèques

Le programme nécessite la bibliothèque standard `machine` (pour configurer le bus I2C) et une bibliothèque externe spécifique nommée `dht20.py` (qui fait environ 2kB) qu'il faut impérativement télécharger et sauvegarder sur votre Pico au préalable.

```python
from machine import I2C
from dht20 import DHT20
from utime import sleep
```

#### 2. Initialisation du bus I2C et création de l'objet DHT20

Étant donné que le DHT20 utilise le protocole I2C, la première étape consiste à initialiser ce bus. Ensuite, on passe cet objet I2C à la classe `DHT20` pour créer notre capteur.

```python
# Initialisation du bus I2C (le numéro de bus dépend de votre câblage, ici 0)
i2c = I2C(0)

# Création de l'objet capteur DHT20
capteur_dht20 = DHT20(i2c)
```

#### 3. Commandes de lecture des données

La bibliothèque `dht20.py` rend la récupération des données très simple grâce à deux fonctions dédiées :

* `capteur_dht20.dht20_temperature()` : Lit et retourne la valeur actuelle de la température.
* `capteur_dht20.dht20_humidity()` : Lit et retourne la valeur actuelle du taux d'humidité.

#### 4. Intégration dans une boucle

Voici un exemple complet montrant comment lire et afficher (dans la console) les données du capteur en continu, avec une pause d'une seconde entre chaque lecture.

```python
from machine import I2C
from dht20 import DHT20
from utime import sleep

# Configuration matérielle
i2c = I2C(0)
capteur_dht20 = DHT20(i2c)

# Boucle principale
while True:
    # Lecture des valeurs
    temper = capteur_dht20.dht20_temperature()
    humid = capteur_dht20.dht20_humidity()
    
    # Affichage dans la console (conversion en texte avec str())
    print("Température : " + str(temper) + " °C")
    print("Humidité : " + str(humid) + " %")
    
    # Attente d'une seconde avant la prochaine lecture
    sleep(1)
```
