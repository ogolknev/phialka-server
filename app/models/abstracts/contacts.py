from abc import ABCMeta, abstractmethod
from typing import Optional

from pydantic import BaseModel



class AbsContacts(BaseModel):
    __metaclass__ = ABCMeta

    id: int
    owner_id: int
    user_ids: Optional[set[int]]