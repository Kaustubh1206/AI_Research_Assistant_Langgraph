from pydantic import BaseModel, Field
from typing import List

# Creating our object which is going to be an analyst
class Analyst(BaseModel):
    affilition: str = Field(description="Primary Affiliation of the analyst.")
    name: str = Field(description="Name of the analyst.")
    role: str = Field(description="Role of the analyst in the context of the topic.")
    description: str = Field(description="Description of the analyst focus, concerns and motives.")

    @property
    def persona(self)->str:
        return f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affilition}\nDescription: {self.description}"


class Perspectives(BaseModel):
    analysts:  List[Analyst] = Field(description="Comprehensive list of Analysts with their roles and affilition")