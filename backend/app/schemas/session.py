
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SessionCreate(BaseModel):
    goal: str = Field(min_length=5, max_length=1000)
    scenario: str = Field(default="custom", min_length=2, max_length=100)
    constraints: list[str] = Field(default_factory=list, max_length=20)


class SessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    goal: str
    scenario: str
    status: str
    constraints: list[str]
    created_at: datetime
    updated_at: datetime
