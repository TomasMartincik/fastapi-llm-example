from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_llm_provider
from app.schemas.pokemon import Pokemon
from app.schemas.query import Query
from app.services.llm_providers import LLMProvider

router = APIRouter(prefix="/pokemon")


@router.post("/identify", response_model=Pokemon)
async def identify_pokemon(
    query: Query, llm_provider: LLMProvider = Depends(get_llm_provider)
):
    if not query.pokemon_description:
        raise HTTPException(
            status_code=400, detail="Pokemon description must not be empty"
        )

    if len(query.pokemon_description) > 500:
        raise HTTPException(
            status_code=400, detail="Pokemon description must not exceed 500 characters"
        )

    try:
        result = await llm_provider.identify_pokemon(query.pokemon_description)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

    if not result:
        raise HTTPException(
            status_code=404, detail="Could not identify a pokemon from the description"
        )

    return result
