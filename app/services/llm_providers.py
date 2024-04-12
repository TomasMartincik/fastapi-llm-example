from abc import ABC, abstractmethod
from typing import Optional

from app.schemas.pokemon import Pokemon


class LLMProvider(ABC):
    @abstractmethod
    async def identify_pokemon(self, query: str) -> Optional[Pokemon]:
        pass
