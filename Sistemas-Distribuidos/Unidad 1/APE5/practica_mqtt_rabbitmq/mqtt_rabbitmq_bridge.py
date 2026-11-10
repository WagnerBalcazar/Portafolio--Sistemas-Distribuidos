"""Reenvía GPS y alertas críticas desde MQTT a colas duraderas de RabbitMQ."""

import json

import pika
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
RABBITMQ_HOST = "localhost"


def configurar_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    for queue in (
        "cola.gps.telemetria",
        "cola.alertas.temperatura",
        "cola.combustible.nivel",
    ):
        channel.queue_declare(queue=queue, durable=True)
    print("Colas RabbitMQ declaradas.")
    return connection, channel


def al_recibir_mensaje_mqtt(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        channel = userdata["rabbitmq_channel"]
        queue = None
        if msg.topic.endswith("/gps"):
            queue = "cola.gps.telemetria"
        elif msg.topic.endswith("/temperatura") and float(payload.get("temperature", 0)) > 4:
            queue = "cola.alertas.temperatura"
            payload = {"type": "TEMP_ALERT", "message": "Temperatura excedida", **payload}
        elif msg.topic.endswith("/combustible") and float(payload.get("fuel_level", 0)) < 20:
            queue = "cola.combustible.nivel"
            payload = {"type": "FUEL_LOW", "message": "Combustible bajo", **payload}

        if queue:
            channel.basic_publish(
                exchange="",
                routing_key=queue,
                body=json.dumps(payload),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type="application/json",
                ),
            )
            print(f"Reenviado a {queue}: {msg.topic}")
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError, KeyError) as exc:
        print(f"Error procesando mensaje MQTT de {msg.topic}: {exc}")
    except pika.exceptions.AMQPError as exc:
        print(f"Error publicando en RabbitMQ: {exc}")


def principal():
    conn_rabbit, channel_rabbit = configurar_rabbitmq()
    client = mqtt.Client(userdata={"rabbitmq_channel": channel_rabbit})
    client.on_message = al_recibir_mensaje_mqtt
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.subscribe("flota/#", qos=1)
        print("Puente MQTT–RabbitMQ activo en flota/#. Ctrl+C para detener.")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nCerrando puente...")
    finally:
        client.disconnect()
        if conn_rabbit.is_open:
            conn_rabbit.close()


if __name__ == "__main__":
    principal()
