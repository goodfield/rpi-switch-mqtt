Raspberry Pi Switch/Relay MQTT
=============================

Use mqtt to control relays connected to a raspberry.


Installation:
-------------------

    pip install rpi-switch-mqtt

Configuration:
-------------------

Needs a json configuration file as follows (don't forget to change ip's and credentials ;-)):

.. code:: json

    {
        "mqtt_client_id": "power_meter",
        "mqtt_host": "192.168.0.210",
        "mqtt_port": "1883",
        "switches": [
           {
              "gpio": "4",
              "topic_status": "halti/stweg/door",
              "topic_set": "halti/stweg/door/set"
            }
          ]
    }



Start:
-------------------

    rpi-switch-mqtt config.json
