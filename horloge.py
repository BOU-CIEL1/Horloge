import time
import keyboard

# Initialisation des variables dans un dictionnaire pour pouvoir les utiliser n'importe où dans le code
temps = {
  "secondes": 0,
  "minutes": 0,
  "heures": 0
}


def horloge():
  while True: # S"éxecute tout le temps
    delai = avance_rapide()
    for i in range(10):
      time.sleep(delai) # Intervalle d'une seconde découpée en 10 pour détecter correctement la touche ESPACE
    temps["secondes"] += 1
    if temps["secondes"] >= 60: # Passage à 1 minute
      temps["secondes"] = 0
      temps["minutes"] += 1
    if temps["minutes"] >= 60: # Passage à 1 heure
      temps["minutes"] = 0
      temps["heures"] += 1
    if temps["heures"] >= 24: # Passage à 1 journée
      temps["heures"] = 0

    print(f"{temps["heures"]:02d}:{temps["minutes"]:02d}:{temps["secondes"]:02d}") # Affichage comme une horloge

    pause()

    
def pause(): # Met l'horloge en pause quand la touche ESPACE est pressée
  if keyboard.is_pressed("space"):
    print("PAUSE")
    time.sleep(1)

    keyboard.wait("space")

    print("REPRISE")
    time.sleep(0.3)

def avance_rapide(): # Fait s'écouler le temps plus rapidement quand la touche M est enfoncée
  if keyboard.is_pressed("m"):
    return 0.01
  return 0.1


horloge()