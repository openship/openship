"""Karrio UPS connection settings."""

import attr
from karrio.providers.ups_ground.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """UPS connection settings."""

    username: str
    password: str
    access_license_number: str
    account_number: str = None
    account_country_code: str = None

    id: str = None
    test: bool = False
    carrier_id: str = "ups_ground"