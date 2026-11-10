"""Publica telemetría simulada para una flota de tres vehículos."""

import datetime
import json
import random
import time

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
VEHICULOS = ["VH-001", "VH-002", "VH-003"]


def on_connect(client, userdata, flags, rc):
    print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Conexión MQTT: código {rc}")


def simular_gps():
    return {
        "lat": round(-2.1709 + random.uniform(-0.01, 0.01), 6),
        "lng": round(-79.9224 + random.uniform(-0.01, 0.01), 6),
        "speed": round(random.uniform(20, 80), 1),
    }


def simular_temperatura():
    return {"temperature": round(random.uniform(-5, 8), 1), "unit": "celsius"}


def simular_combustible():
    return {"fuel_level": round(random.uniform(10, 100), 1), "unit": "percent"}


def publicar(client, topic, payload):
    info = client.publish(topic, json.dumps(payload), qos=1)
    info.wait_for_publish()
    if info.rc != mqtt.MQTT_ERR_SUCCESS:
        print(f"No se pudo publicar en {topic}: código {info.rc}")


def principal():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    print("Iniciando simulador; publica cada 5 segundos. Ctrl+C para detener.")
    try:
        while True:
            for vehiculo in VEHICULOS:
                timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
                for tipo, datos in (
                    ("gps", simular_gps()),
                    ("temperatura", simular_temperatura()),
                    ("combustible", simular_combustible()),
                ):
                    publicar(
                        client,
                        f"flota/{vehiculo}/{tipo}",
                        {"vehicle_id": vehiculo, "timestamp": timestamp, **datos},
                    )
                print(f"[{timestamp}] Telemetría publicada: {vehiculo}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nDeteniendo simulador...")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    principal()
