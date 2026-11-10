"""Guarda telemetría MQTT en SQLite y muestra alertas de umbral."""

import json
import sqlite3

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
DB_NAME = "telemetria.db"


def inicializar_base_datos():
    with sqlite3.connect(DB_NAME) as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS gps_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_id TEXT,
                lat REAL, lng REAL, speed REAL, timestamp TEXT
            );
            CREATE TABLE IF NOT EXISTS temp_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_id TEXT,
                temperature REAL, unit TEXT, timestamp TEXT
            );
            CREATE TABLE IF NOT EXISTS fuel_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_id TEXT,
                fuel_level REAL, unit TEXT, timestamp TEXT
            );
            """
        )
    print(f"Base de datos inicializada: {DB_NAME}")


def al_recibir_mensaje(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        vehicle_id, timestamp = payload["vehicle_id"], payload["timestamp"]
        with sqlite3.connect(DB_NAME) as conn:
            if msg.topic.endswith("/gps"):
                conn.execute(
                    "INSERT INTO gps_data (vehicle_id, lat, lng, speed, timestamp) VALUES (?, ?, ?, ?, ?)",
                    (vehicle_id, payload["lat"], payload["lng"], payload["speed"], timestamp),
                )
            elif msg.topic.endswith("/temperatura"):
                temperature = float(payload["temperature"])
                if temperature > 4:
                    print(f"⚠️ ALERTA TEMPERATURA: {vehicle_id} — {temperature} °C")
                conn.execute(
                    "INSERT INTO temp_data (vehicle_id, temperature, unit, timestamp) VALUES (?, ?, ?, ?)",
                    (vehicle_id, temperature, payload.get("unit"), timestamp),
                )
            elif msg.topic.endswith("/combustible"):
                fuel_level = float(payload["fuel_level"])
                if fuel_level < 20:
                    print(f"⚠️ ALERTA COMBUSTIBLE: {vehicle_id} — {fuel_level}%")
                conn.execute(
                    "INSERT INTO fuel_data (vehicle_id, fuel_level, unit, timestamp) VALUES (?, ?, ?, ?)",
                    (vehicle_id, fuel_level, payload.get("unit"), timestamp),
                )
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError, ValueError, sqlite3.Error) as exc:
        print(f"Error procesando mensaje de {msg.topic}: {exc}")


def principal():
    inicializar_base_datos()
    client = mqtt.Client()
    client.on_message = al_recibir_mensaje
    client.connect(BROKER, PORT, 60)
    client.subscribe("flota/+/gps", qos=1)
    client.subscribe("flota/+/temperatura", qos=1)
    client.subscribe("flota/+/combustible", qos=1)
    print("Suscriptor activo en flota/+/[gps|temperatura|combustible]. Ctrl+C para detener.")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nCerrando suscriptor...")
    finally:
        client.disconnect()


if __name__ == "__main__":
    principal()
