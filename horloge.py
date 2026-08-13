import time
import keyboard

def horloge():
  # Initialisation des variables
  secondes = 0
  minutes = 0
  heures = 0

  while True: # S"éxecute tout le temps
    for i in range(10):
      time.sleep(0.1) # Intervalle d'une seconde découpée en 10 pour détecter correctement la touche ESPACE
    secondes += 1
    if secondes == 60: # Passage à 1 minute
      secondes = 0
      minutes += 1
    if minutes == 60: # Passage à 1 heure
      minutes = 0
      heures += 1
    if heures == 24: # Passage à 1 journée
      heures = 0

    print(f"{heures:02d}:{minutes:02d}:{secondes:02d}") # Affichage comme une horloge

    pause()

    
def pause():
  if keyboard.is_pressed("space"):
    print("PAUSE")
    time.sleep(1)

    keyboard.wait("space")

    print("REPRISE")
    time.sleep(0.3)

horloge()