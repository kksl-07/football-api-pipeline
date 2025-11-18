from pydantic import BaseModel, Field


class TopScores(BaseModel):
    league: str
    season: str = Field(pattern=r"^(20)[1-3]{2}$")


class Player(BaseModel):
    endpoint_name: str = "players"
    top_scores_obj: TopScores
