async def async_setup_entry(hass, entry, _add_devices):
    hass.async_add_job(
        hass.config_entries.async_forward_entry_setup(entry, "media_player"))


async def async_remove_entry(hass, entry) -> None:
    await hass.config_entries.async_forward_entry_unload(entry, "media_player")
