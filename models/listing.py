from dataclasses import dataclass
from typing import Optional


@dataclass
class Listing:
    title: str
    price: Optional[int]
    address: str
    bedrooms: Optional[float]
    bathrooms: Optional[float]
    pets: Optional[bool]
    source: str
    url: str
