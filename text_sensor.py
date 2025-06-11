from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data["dimmer_node_8ch"]["coordinator"]
    async_add_entities([
        IPAddressSensor(coordinator),
        MACAddressSensor(coordinator),
        SSIDSensor(coordinator)
    ])

class IPAddressSensor(Entity):
    def __init__(self, coordinator):
        self._name = "Adresse IP"
        self._state = "192.168.1.100"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

class MACAddressSensor(Entity):
    def __init__(self, coordinator):
        self._name = "Adresse Mac"
        self._state = "AA:BB:CC:DD:EE:FF"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

class SSIDSensor(Entity):
    def __init__(self, coordinator):
        self._name = "SSID Wi-Fi"
        self._state = "MonReseauWiFi"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state