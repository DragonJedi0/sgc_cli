from models import Personnel, Missions

JACK = Personnel("Jack O'Neill", "Colonel", "SG-1", "Team Leader")

summary = "Initial recon through Stargate to Abydos."
participants = [JACK.id]

ABYDOS = Missions("First Abydos Mission", "SG-1", "1997-07-27", JACK.id, participants, summary)

PERSONNEL = [JACK]
MISSIONS = [ABYDOS]