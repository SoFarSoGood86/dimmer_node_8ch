import logging
from homeassistant.components.light import LightEntity

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data["dimmer_node_8ch"]["coordinator"]
    lights = []
    for i in range(1, 9):
        lights.append(DimmerLight(coordinator, f"Variateur Lumière {i:02}", i))
    async_add_entities(lights)

class DimmerLight(LightEntity):
    def __init__(self, coordinator, name, channel):
        self._coordinator = coordinator
        self._name = name
        self._channel = channel
        self._is_on = False
        self._brightness = 255

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def brightness(self):
        return self._brightness

    async def async_turn_on(self, **kwargs):
        self._is_on = True
        if "brightness" in kwargs:
            self._brightness = kwargs["brightness"]
        _LOGGER.debug(f"Turning on {self._name} to brightness {self._brightness}")

    async def async_turn_off(self, **kwargs):
        self._is_on = False
        _LOGGER.debug(f"Turning off {self._name}")