from typing import TypedDict
import pandas as pd
from dataclasses import dataclass
from dataclasses import field

@dataclass
class DTOBase:
    lista: list = field(default_factory=list)
    
   