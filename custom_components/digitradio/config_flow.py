import logging
from urllib.parse import urlparse

import voluptuous as vol
from homeassistant.components import ssdp
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_HOST

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class DigitRadioConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_ssdp(self, info):
        name = info[ssdp.ATTR_UPNP_FRIENDLY_NAME]
        serial_number = info[ssdp.ATTR_UPNP_SERIAL]
        host = urlparse(info[ssdp.ATTR_SSDP_LOCATION]).hostname

        _LOGGER.info("discovered digitradio: %s (%s) @ %s",
                     name, serial_number, host)

        device_info = {
            "identifiers": {
                (DOMAIN, serial_number),
            },
            "name": name,
            "manufacturer": info[ssdp.ATTR_UPNP_MANUFACTURER],
            "model": info[ssdp.ATTR_UPNP_MODEL_NAME],
        }

        await self.async_set_unique_id(serial_number)
        self._abort_if_unique_id_configured(updates={CONF_HOST: host})

        return self.async_create_entry(
            title=name,
            data={
                "device_info": device_info,
                "serial_number": serial_number,
                CONF_HOST: host,
            },
        )
