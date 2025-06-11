from homeassistant.components.sensor import SensorEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data["dimmer_node_8ch"]["coordinator"]
    async_add_entities([
        WifiSignalSensor(coordinator),
        UptimeSensor(coordinator)
    ])

class WifiSignalSensor(SensorEntity):
    def __init__(self, coordinator):
        self._coordinator = coordinator
        self._name = "Signal WiFi"
        self._state = -60

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

class UptimeSensor(SensorEntity):
    def __init__(self, coordinator):
        self._coordinator = coordinator
        self._name = "Temps d'utilisation"
        self._state = 12345

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state