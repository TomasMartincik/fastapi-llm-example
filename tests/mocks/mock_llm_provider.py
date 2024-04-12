from typing import Optional

from app.schemas.pokemon import Pokemon, Stats
from app.services.llm_providers import LLMProvider


class MockLLMProvider(LLMProvider):
    def __init__(self, behavior="succeed"):
        self.behavior = behavior

    async def identify_pokemon(self, query: str) -> Optional[Pokemon]:
        match self.behavior:
            case "succeed":
                match query:
                    case "Pikachu":
                        return Pokemon(
                            id=25,
                            name="Pikachu",
                            height=16,
                            weight=13.2,
                            category="Mouse Pokemon",
                            types=["Electric"],
                            weaknesses=["Ground"],
                            abilities=["Static", "Lightning Rod"],
                            stats=Stats(
                                hp=35,
                                attack=55,
                                defense=40,
                                special_attack=50,
                                special_defense=50,
                                speed=90,
                            ),
                        )
                    case _:
                        return None
            case "fail_with_none":
                return None
            case "fail_with_exception":
                raise Exception("An error occurred")
            case _:
                return None
