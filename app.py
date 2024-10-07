import os
import random
import time
import pygame 

pygame.mixer.init()
pygame.mixer.music.load("carrera-de-buses.mp3")
pygame.mixer.music.play(-1)  

GREN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
YELLOW = "\033[33m"
END = "\033[0m"

bus_1 = {"nombre": "  114   ", "velocidad_max": 5, "combustible": 100, "consumo": 2}
bus_2 = {"nombre": "  120   ", "velocidad_max": 5, "combustible": 100, "consumo": 2}

def buses(n1, n2, combustible_1, combustible_2, clima, mensaje_clima):
    output = []
    output.append(120 * "-")
    output.append((n1 * " ") + RED + "   _______________  "    + END + ((100 - n1) * " ") + "| META |")
    output.append((n1 * " ") + RED + "  |__|__|__|__|__|__"  + END + ((97 - n1) * " ") + " |")
    output.append((n1 * " ") + RED + f" |     {bus_1['nombre']}     |)" + END + ((96 - n1) * " ") + "|")
    output.append((n1 * " ") + RED + "  |~~~@~~~~~~~~~@~~~|)"  + END + ((95 - n1) * " ") + " |")
    output.append(120 * "_")
    output.append((n2 * " ") + BLUE + "   _______________  "   + END + ((100 - n2) * " ") + "| META |")
    output.append((n2 * " ") + BLUE + "  |__|__|__|__|__|__" + END + ((97 - n2) * " ") + " |")
    output.append((n2 * " ") + BLUE + f" |    {bus_2['nombre']}      |)" + END + ((96 - n2) * " ") + "|")
    output.append((n2 * " ") + BLUE + "  |~~~@~~~~~~~~~@~~~|)" + END + ((95 - n2) * " ") + " |")
    output.append(120 * "_")
    output.append(f"Clima: {clima} | Combustible {bus_1['nombre']}: {combustible_1}% | Combustible {bus_2['nombre']}: {combustible_2}%")
   
    output.append(120 * "-")
    return "\n".join(output)

clima = random.choice(["Soleado", "Lluvia", "Niebla"])
mensaje_clima = ""

if clima == "Lluvia":
    clima_mod = 0.5
  
elif clima == "Niebla":
    clima_mod = 0.7
   
else:
    clima_mod = 1.0
   

a = 0
b = 0
gano = None

os.system("cls" if os.name == "nt" else "clear")

presentacion = f"""
{YELLOW}        <<<<<<<<<<< CARRERA DE BUSES >>>>>>>>>>
            {RED}114 {YELLOW}VS{BLUE} 120 {END}
"""
print(presentacion)
time.sleep(2)

while a < 100 and b < 100 and (bus_1['combustible'] > 0 or bus_2['combustible'] > 0):
    if bus_1['combustible'] > 0:
        a += random.randint(1, int(bus_1['velocidad_max'] * clima_mod))
        bus_1['combustible'] -= bus_1['consumo']  
    
    if bus_2['combustible'] > 0:
        b += random.randint(1, int(bus_2['velocidad_max'] * clima_mod))
        bus_2['combustible'] -= bus_2['consumo']  

    a = min(a, 100)
    b = min(b, 100)

    os.system("cls" if os.name == "nt" else "clear")
    print(buses(a, b, bus_1['combustible'], bus_2['combustible'], clima, mensaje_clima))
    time.sleep(0.1)

if a >= 100:
    gano = bus_1['nombre']
elif b >= 100:
    gano = bus_2['nombre']
else:
    gano = "EMPATE por falta de combustible"

print(f"{GREN}¡GANÓ LA CARRERA: {gano}!{END}")
