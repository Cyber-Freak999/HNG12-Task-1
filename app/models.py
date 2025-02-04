from pydantic import BaseModel
from typing import List


class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: List[str]
    digit_sum: int
    fun_fact: str


class ErrorResponse(BaseModel):
    number: str
    error: bool = True
