# cli.py

import sys
from helpers import (
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees
)

MENU_OPTIONS = {
    "0": "Exit the program",
    "1": "List all departments",
    "2": "Find department by name",
    "3": "Find department by id",
    "4": "Create department",
    "5": "Update department",
    "6": "Delete department",
    "7": "List all employees",
    "8": "Find employee by name",
    "9": "Find employee by id",
    "10": "Create employee",
    "11": "Update employee",
    "12": "Delete employee",
    "13": "List all employees in a department"
}


def main():
    while True:
        print_menu()
        choice = input("Please select an option: ")
        if choice == "0":
            exit_program()
        elif choice in MENU_OPTIONS:
            execute_option(choice)
        else:
            print("Invalid choice\n")


def print_menu():
    for option, description in MENU_OPTIONS.items():
        print(f"{option}. {description}")


def execute_option(choice):
    if choice == "1":
        list_departments()
    elif choice == "2":
        find_department_by_name()
    elif choice == "3":
        find_department_by_id()
    elif choice == "4":
        create_department()
    elif choice == "5":
        update_department()
    elif choice == "6":
        delete_department()
    elif choice == "7":
        list_employees()
    elif choice == "8":
        find_employee_by_name()
    elif choice == "9":
        find_employee_by_id()
    elif choice == "10":
        create_employee()
    elif choice == "11":
        update_employee()
    elif choice == "12":
        delete_employee()
    elif choice == "13":
        list_department_employees()


def exit_program():
    print("Goodbye!")
    sys.exit()


if __name__ == "__main__":
    main()
