from data import PERSONNEL, MISSIONS
from models import Personnel, Missions, Role, Status

def main():
    # Set Loop control
    exit = False

    # Print header
    print("******************************************")
    print("Welcome to SGC Personnel Management System")

    # Loop the main menu until exit condition is true
    while not exit:
        print("******************************************")
        print("1. List Personnel")
        print("2. Add Personnel")
        print("3. View Personnel")
        print("4. Edit Personnel")
        print("5. Delete Personnel")
        print("6. List Missions")
        print("7. Add Mission Report")
        print("0. Exit")

        choice = input("Choose an option: ")

        match (choice):
            case "1":
                list_personnel()
            case "2":
                add_personnel()
            case "3":
                try:
                    sg_member = get_personnel("view")
                except ValueError as err:
                    print(str(err))
                    continue
                # Handle not found
                if not sg_member:
                    print("ID not found. Please try again.\nUse 'List Personnel' for list of valid IDs.")
                    continue
                view_personnel(sg_member)
            case "4":
                edit_personnel()
            case "5":
                try:
                    sg_member = get_personnel("delete")
                except ValueError as err:
                    print(str(err))
                    continue
                # Handle not found
                if not sg_member:
                    print("ID not found. Please try again.\nUse 'List Personnel' for list of valid IDs.")
                    continue
                delete_personnel(sg_member)
            case "6":
                list_missions()
            case "7":
                add_mission()

            case "0":
                print("Exiting...")
                exit = True

            case _:
                print("******************************************")
                print("That is not a valid option\nPlease select a valid option (0-4)")

def add_mission():
    # Print header
    print("******************************")

    # Ask user for core mission data
    title = input("Enter Mission Title: ")
    team = input("Enter SG Team: ")
    date = input("Enter mission date: ")

    # Ask user to enter mission summary
    summary = input("Enter brief mission summary: ")

    # helper function to populate participants list
    def get_team_members(team):
        team_members = []
        for person in PERSONNEL:
            # Add only personnel assigned to SG team for mission report
            if person.assignment == team:
                team_members.append(person.id)

        return team_members

    participants = get_team_members(team)

    # Catch empty participant list prior to creating mission entry
    if not participants:
        print("No personnel currently assigned to that team. Mission not added.")
        return

    # Add mission report to MISSIONS list
    mission_report = Missions(title, team, date, participants[0], participants, summary)
    MISSIONS.append(mission_report)

    # Print confirmation message
    print("***********************************************")
    print(f"Added mission report {mission_report.id:02d}, {mission_report.title}")

def list_missions():
    # Print Header
    print("************************************")
    print("* Stargate Command Mission Reports *")
    print("************************************")

    # Loop through MISSIONS list and print simple mission report data
    for mission in MISSIONS:
        print(f"Mission Report {mission.id:02d}: {mission.title}, {mission.date}; Team assigned: {mission.team}, Team Lead: {mission.commanding_officer_id}")

def list_personnel():
    # Print Header
    print("******************************")
    print("* Stargate Command Personnel *")
    print("******************************")

    if not PERSONNEL:
        print("No records found...")

    # Loop through PERSONNEL list and print simple personnel data
    for person in PERSONNEL:
        print(f"ID {person.id:02d}: {person.name}, {person.rank}; {person.assignment} - Status: {person.status.value}")

def add_personnel():
    # Print header
    print("******************************")
    # Ask user for personnel's name
    fname = input("Enter personnel's first name: ")
    mname = input("Enter personnel's middlie name (Press Enter for N/A): ")
    lname = input("Enter personnel's last name: ")

    if mname:
        full_name = fname + " " + mname + " " + lname
    else:
        full_name = fname + " " + lname

    # Ask user for personnel's data
    rank = input("Enter personnel's rank: ")
    assignment = input("Enter personnel's assignment: ")
    role = input("Enter personnel's role: ")

    sg_member = Personnel(full_name, rank, assignment, role)

    # Add personnel to PERSONNEL list
    PERSONNEL.append(sg_member)

    # Print Confirmation message
    print("***********************************************")
    print(f"Added {sg_member.id:02d}: {sg_member.name} to {sg_member.assignment}")

def get_personnel(action):
    # Print header
    print("******************************")

    # Ask user for personnel id
    try:
        pid = int(input(f"Enter personnel ID to {action}: "))
    except ValueError:
        raise ValueError("Invalid ID. Please enter a valid number.\nUse 'List Personnel' for list of valid IDs.")
    
    for person in PERSONNEL:
        if person.id == pid:
            return person
    
    return None

def view_personnel(sg_member):
    # Print header
    print("***********************")
    print(f"* SGC Personnel ID {sg_member.id:02d} *")
    print("***********************")
    print(f"Name: {sg_member.name}")
    print(f"Rank: {sg_member.rank}")
    print(f"Current Assignment: {sg_member.assignment}")
    print(f"Role: {sg_member.role}")
    print(f"Status: {sg_member.status.value}")

def edit_personnel():
    # Find selected personnel
    try:
        sg_member = get_personnel("edit")
    except ValueError as err:
        print(str(err))
        return
    
    # Handle not found
    if not sg_member:
        print("ID not found. Please try again.\nUse 'List Personnel' for list of valid IDs.")
        return

    # Edit fields (Enter = keep current value)
    print("Press Enter to keep the current value")

    new_rank = input(f"Enter new rank (Current: {sg_member.rank}): ")
    if new_rank:
        sg_member.rank = new_rank
    
    new_assignment = input(f"Enter new assignment (Current: {sg_member.assignment}): ")
    if new_assignment:
        sg_member.assignment = new_assignment
    
    # Print Confirmation message
    print("***********************************************")
    print(f"Updated ID {sg_member.id:02d}: {sg_member.name}, {sg_member.rank}; {sg_member.assignment} - Status: {sg_member.status.value}")

def delete_personnel(sg_member):
    # Print Confirmation message
    confirm = input(f"Are you sure you want to delete Record ID {sg_member.id:02d}? (Y/N): ").strip().lower()

    # Handle invalid input
    if confirm not in ("y", "yes", "n", "no"):
        print("That is not a valid selection")
        print("Returning to main menu...")
        return

    # If Yes, remove from PERSONNEL
    if confirm in ("y", "yes"):
        PERSONNEL.remove(sg_member)
        print(f"Successfully removed Personnel Record (ID {sg_member.id:02d})")
    else:
        print("Deletion cancled.")
    
    print(f"Returning to main menu...")


if __name__ == "__main__":
    main()