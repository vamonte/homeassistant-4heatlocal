import voluptuous as vol
from homeassistant.data_entry_flow import FlowResult
from homeassistant import config_entries
from .const import DOMAIN

class FourHeatLocalConfiGFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:

        user_form = vol.Schema({
            vol.Required("ip"): str,
            vol.Required("port", default="8080"): str,
        })

        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=user_form)
        