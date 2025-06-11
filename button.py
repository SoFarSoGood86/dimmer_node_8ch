from homeassistant.components.button import ButtonEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data["dimmer_node_8ch"]["coordinator"]
    async_add_entities([RestartButton(coordinator)])

class RestartButton(ButtonEntity):
    def __init__(self, coordinator):
        self._coordinator = coordinator
        self._name = "Redémarrer le Node"

    @property
    def name(self):
        return self._name

    async def async_press(self):
        self._coordinator.reboot()