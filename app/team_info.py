from dataclasses import dataclass
from typing import List


@dataclass
class TeamInfo:
    name: str
    id: int
    members: List[str]
    description: str

TEAMS = {
    "Management": TeamInfo(
        name="Management",
        id=1,
        members=["Kelvin", "Nathan"],
        description = "This be the management team!"
    ),
    "Procurement": TeamInfo(
        name="Procurement",
        id=2,
        members=["Briana", "Kera", "Ryan"],
        description = "This be the procurement team!"
    ),
    "Social": TeamInfo(
        name="Social",
        id=3,
        members=["Megan", "Kara", "Jen"],
        description = "This be the social team!"
    ),

}
