import requests
from datetime import datetime
import pytz

TOKEN = "8474282235:AAEEW6v74vMq5d4kXDS9LNYAHuv0Xi35Yk4"
CHAT_ID = "6877119669"

def es_hora_ejecucion():
    tz = pytz.timezone('Europe/Madrid')
    ahora = datetime.now(tz)
    hora = ahora.hour
    minuto = ahora.minute

    horarios = [
        (8, 50),
        (14, 0),
        (17, 30),
        (18, 0)
    ]

    return (hora, minuto) in horarios

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": texto}
    r = requests.get(url, params=params)
    return r.status_code

def main():
    if not es_hora_ejecucion():
        print("No es hora de ejecutar el informe.")
        return

    mensaje = "Informe diario automático de Repsol y Brent"
    # Aquí puedes ampliar con análisis e indicadores
    status = enviar_mensaje(mensaje)
    print(f"Mensaje enviado con código: {status}")

if __name__ == "__main__":
    main()
