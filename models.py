from enum import Enum

PERSONS_ID = 0
MISSION_ID = 0

class Status(Enum):
    ACTIVE = "Active"
    MIA = "MIA"
    KIA = "KIA"
    RETIRED = "Retired"

class Role(Enum):
    TEAMLEADER = "Team Leader"
    TACTICAL = "Tactical"
    SCIENTIST = "Scientist"
    ARCHEOLOGIST = "Archeologist"

class Personnel:
    def __init__(self, name, rank, assignment, role, status=Status.ACTIVE):
        global PERSONS_ID
        PERSONS_ID += 1
        self.id = PERSONS_ID
        self.name = name
        self.rank = rank
        self.assignment = assignment
        self.role = role
        self.status = status


class Missions:
    def __init__(self, title, team, date, commanding_officer_id, participants, summary=""):
        global MISSION_ID
        MISSION_ID += 1
        self.id = MISSION_ID
        self.title = title
        self.team = team
        self.date = date
        self.commanding_officer_id = commanding_officer_id
        self.participants = participants
        self.summary = summary