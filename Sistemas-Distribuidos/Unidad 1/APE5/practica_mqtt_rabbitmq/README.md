# Práctica: MQTT y RabbitMQ para telemetría de flota

Simulación de tres vehículos que publican GPS, temperatura y combustible mediante MQTT. Un suscriptor almacena los datos en SQLite y un puente reenvía GPS y alertas críticas a RabbitMQ.

## Requisitos y puesta en marcha

Se necesita Docker con el complemento Compose y Python 3.9 o posterior.

```bash
cd practica_mqtt_rabbitmq
docker compose up -d
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

La interfaz de RabbitMQ está en <http://localhost:15672> (usuario y contraseña predeterminados: `guest` / `guest`). Mosquitto escucha en `localhost:1883`.

## Comprobación rápida de MQTT

En una terminal:

```bash
docker exec -it mosquitto_broker mosquitto_sub -h localhost -t 'test/topic'
```

En otra:

```bash
docker exec -it mosquitto_broker mosquitto_pub -h localhost -t 'test/topic' -m 'Hola MQTT'
```

## Ejecutar la práctica

Abre una terminal para cada proceso (con el entorno virtual activado):

```bash
python subscriber.py
python mqtt_rabbitmq_bridge.py
python sensor_simulador.py
```

El simulador publica cada cinco segundos en `flota/<vehículo>/gps`, `flota/<vehículo>/temperatura` y `flota/<vehículo>/combustible`. SQLite crea `telemetria.db` en el directorio actual. El puente declara las colas `cola.gps.telemetria`, `cola.alertas.temperatura` y `cola.combustible.nivel`; las alertas se generan con temperatura > 4 °C o combustible < 20 %.

Detén cada proceso con Ctrl+C. Para apagar los servicios: `docker compose down`.

## Preguntas de control

### 1. Diferencias entre MQTT y AMQP. ¿Por qué MQTT es adecuado para IoT?

MQTT es un protocolo ligero de publicación/suscripción sobre TCP, diseñado para clientes con recursos limitados o conexiones con ancho de banda reducido e intermitente. El cliente publica en un *topic* y los suscriptores reciben los mensajes de los temas a los que están suscritos. AMQP, utilizado por RabbitMQ, ofrece un modelo de mensajería más completo: exchanges reciben mensajes y los enrutan mediante *bindings* y claves de enrutamiento hacia colas. Puede proporcionar persistencia, confirmaciones, control de flujo y estrategias de enrutamiento flexibles.

MQTT es conveniente en IoT porque reduce el trabajo y los datos de protocolo necesarios para comunicar sensores y dispositivos remotos. Sus niveles QoS permiten elegir entre menor costo y mayor garantía de entrega. No significa que MQTT garantice por sí solo la entrega final a una aplicación: eso depende de QoS, sesión, broker y consumidor.

### 2. ¿Por qué MQTT usa jerarquía de topics y RabbitMQ exchanges, colas y bindings?

Los topics de MQTT dan un espacio de nombres jerárquico y simple. Los suscriptores usan `+` para un nivel y `#` para varios niveles, por lo que pueden filtrar dinámicamente mensajes sin declarar una cola por suscriptor. Esto facilita la distribución de telemetría por vehículo o tipo de sensor.

RabbitMQ separa la recepción del mensaje (exchange), las reglas de enrutamiento (bindings) y el almacenamiento/consumo (colas). Esa separación permite que varios consumidores compartan una cola, que diferentes colas reciban copias y que se apliquen políticas de durabilidad y confirmación. MQTT prioriza sencillez en la distribución; RabbitMQ ofrece control de enrutamiento y procesamiento desacoplado.

### 3. Niveles QoS de MQTT: ventajas, desventajas y uso en flota

- **QoS 0 — como máximo una vez:** no espera confirmación ni reintenta. Menor latencia y tráfico, pero se pueden perder mensajes. Útil para posiciones GPS muy frecuentes cuando la siguiente lectura reemplaza rápidamente a la anterior.
- **QoS 1 — al menos una vez:** requiere confirmación y reintenta si es necesario; puede haber duplicados. Aumenta la probabilidad de entrega a costa de más tráfico y requiere que el procesamiento tolere duplicados. Apropiado para telemetría de temperatura/combustible que se desea registrar.
- **QoS 2 — exactamente una vez a nivel de intercambio MQTT:** usa un intercambio de cuatro pasos, con mayor latencia y tráfico. Evita duplicados del protocolo, pero no equivale a una transacción exactamente una vez en la base de datos o sistema de negocio. Puede reservarse para eventos poco frecuentes donde duplicados sean costosos, como una apertura de puerta.

En esta implementación los publicadores y suscripciones usan QoS 1 como equilibrio para registrar telemetría con fiabilidad razonable.
