from typing import List

from pydantic import BaseModel, Field


class Stats(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class Pokemon(BaseModel):
    id: int
    name: str
    height: int = Field(..., description="Height of the pokemon in inches")
    weight: float = Field(..., description="Weight of the pokemon in pounds")
    category: str
    types: List[str]
    weaknesses: List[str]
    abilities: List[str]
    stats: Stats = Field(..., description="Base stats of th pokemon")
