from data import PERSONNEL, MISSIONS
from models import Personnel, Missions

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
                # list_missions()
                pass
            case "4":
                # add_mission()
                pass

            case "0":
                print("Exiting...")
                exit = True

            case _:
                print("******************************************")
                print("That is not a valid option\nPlease select a valid option (0-4)")

def list_personnel():
    print("******************************")
    print("* Stargate Command Personnel *")
    print("******************************")
    for i in range(0, len(PERSONNEL)):
        print(f"ID {PERSONNEL[i].id}: {PERSONNEL[i].name}, {PERSONNEL[i].rank}; {PERSONNEL[i].assignment} - Status: {PERSONNEL[i].status.value}")

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