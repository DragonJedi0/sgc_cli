from data import PERSONNEL, MISSIONS
from models import Personnel, Missions, Role, Status

def main():
    exit = False

    print("******************************************")
    print("Welcome to SGC Personnel Management System")

    while not exit:
        print("******************************************")
        print("1. List Personnel")
        print("2. Add Personnel")
        print("3. List Missions")
        print("4. Add Mission Report")
        print("0. Exit")

        choice = input("Choose an option: ")

        match (choice):
            case "1":
                list_personnel()
            case "2":
                add_personnel()
            case "3":
                list_missions()
            case "4":
                add_mission()

            case "0":
                print("Exiting...")
                exit = True

            case _:
                print("******************************************")
                print("That is not a valid option\nPlease select a valid option (0-4)")

def add_mission():
    print("******************************")
    title = input("Enter Mission Title: ")
    team = input("Enter SG Team: ")
    date = input("Enter mission date: ")
    summary = input("Enter brief mission summary: ")

    def get_team_members(team):
        team_members = []
        for person in PERSONNEL:
            if person.assignment == team:
                team_members.append(person.id)

        return team_members

    participants = get_team_members(team)

    if not participants:
        print("No personnel currently assigned to that team. Mission not added.")
        return

    mission_report = Missions(title, team, date, participants[0], participants, summary)
    MISSIONS.append(mission_report)

    print(f"Added mission report {mission_report.id}, {mission_report.title}")

def list_missions():
    print("************************************")
    print("* Stargate Command Mission Reports *")
    print("************************************")
    for mission in MISSIONS:
        print(f"Mission Report {mission.id}: {mission.title}, {mission.date}; Team assigned: {mission.team}, Team Lead: {mission.commanding_officer_id}")

def list_personnel():
    print("******************************")
    print("* Stargate Command Personnel *")
    print("******************************")
    for person in PERSONNEL:
        print(f"ID {person.id}: {person.name}, {person.rank}; {person.assignment} - Status: {person.status.value}")

def add_personnel():
    print("******************************")
    fname = input("Enter personnel's first name: ")
    mname = input("Enter personnel's middlie name (Press Enter for N/A): ")
    lname = input("Enter personnel's last name: ")

    if mname:
        full_name = fname + " " + mname + " " + lname
    else:
        full_name = fname + " " + lname

    rank = input("Enter personnel's rank: ")
    assignment = input("Enter personnel's assignment: ")
    role = input("Enter personnel's role: ")

    sg_member = Personnel(full_name, rank, assignment, role)

    PERSONNEL.append(sg_member)

    print("***********************************************")
    print(f"Added {sg_member.id}: {sg_member.name} to {sg_member.assignment}")


if __name__ == "__main__":
    main()