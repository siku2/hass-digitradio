import logging

from .const import DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    _LOGGER.info("setup done")
    return True


async def async_setup_entry(hass, entry):
    for platform in PLATFORMS:
        hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, platform))

    _LOGGER.info("entry setup done")


async def async_remove_entry(hass, entry) -> None:
    for platform in PLATFORMS:
        await hass.config_entries.async_forward_entry_unload(entry, platform)
