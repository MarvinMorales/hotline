from typing import Any

from pydantic import BaseModel


class Generic_Response(BaseModel):
    success: bool
    error: bool | str
    data: Any
