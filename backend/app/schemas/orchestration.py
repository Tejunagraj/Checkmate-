
from pydantic import BaseModel, Field


class OrchestrationRequest(BaseModel):
    goal: str = Field(min_length=5, max_length=1000)
    constraints: list[str] = Field(default_factory=list, max_length=20)
