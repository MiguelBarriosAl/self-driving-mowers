from pydantic import BaseModel, Field
from typing import List, Union


class Input(BaseModel):
    top: List[Union[int, int]] = Field(None, min_items=2, max_items=2)
    position: List[Union[int, int, str]] = Field(min_items=3, max_items=3)
    instructions: str
