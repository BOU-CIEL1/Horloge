import time

def horloge():
  secondes = 0
  minutes = 0
  heures = 0

  while True:
    time.sleep(1)
    secondes += 1
    if secondes == 60:
      secondes = 0
      minutes += 1
    if minutes == 60:
      minutes = 0
      heures += 1
    if heures == 24:
      heures = 0

    if secondes < 10:
      printSecondes = (f"0{secondes}")
    else:
      printSecondes = secondes
    if minutes < 10:
      printMinutes = (f"0{minutes}")
    else:
      printMinutes = minutes
    if heures < 10:
      printHeures = (f"0{heures}")
    else:
      printHeures = heures

    print(f"{printHeures}:{printMinutes}:{printSecondes}")

horloge()