# Carrera de Buses

## Descripción
**Carrera de Buses** es un juego de carrera simple implementado en Python. Dos buses compiten en una carrera en un entorno de texto. La velocidad de los buses varía según las condiciones climáticas (soleado, lluvia o niebla) y se simula el consumo de combustible. El primer bus que llegue a la meta ganará la carrera.

## Características
- Dos buses: **114** y **120**.
- Condiciones climáticas que afectan la velocidad:
  - Soleado: máxima velocidad.
  - Lluvia: reduce la velocidad a la mitad.
  - Niebla: reduce la velocidad a un 70%.
- Consumo de combustible para cada bus.
- Reproducción de música de fondo.

## Uso
Para jugar a **Carrera de Buses**, asegúrate de tener Python y las bibliotecas necesarias instaladas. Sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/juanjose23/CarreraBusesPython.git
   cd CarreraBusesPython

## Instalación de dependencias
Asegúrate de tener `pygame` instalado. Puedes instalarlo utilizando `pip`:

```bash
pip install pygame

## Ejecuta el juego
Asegúrate de tener el archivo de música `carrera-de-buses.mp3` en la misma carpeta que tu script. Luego, ejecuta:

```bash
python app.py
