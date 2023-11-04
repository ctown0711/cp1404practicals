"""
Project Management Program
Estimated: 1 hour 40 minutes
Actual: 7min
"""

import datetime
from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")

print(MENU)
menu_choice = input(">>> ").upper()
projects = []
in_file = open(FILENAME)
in_file.readline()
for line in in_file:
    parts = line.strip().split(" ")
    projects.append(Project(parts))
in_file.close()
while menu_choice != "Q":
    if menu_choice == "L":
        input_filename = input("Projects filename: ")
        projects = []
        in_file = open(input_filename)
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(" ")
            projects.append(parts)
    elif menu_choice == "S":
        save_choice = input("Save to current file Y/n: ").upper()
        while save_choice != "Y" or save_choice != "N":
            print("Invalid input")
            save_choice = input("Save to current file Y/n: ").upper()
        if save_choice == "Y":
            output_file = FILENAME
        else:
            output_file = input("Save Filename: ")
        out_file = open(output_file, 'w')
        for project in projects:
            print(f"{project.name} {project.date} {project.priority}"
                  f" {project.cost_estimate} {project.completion_percent}", file=out_file)
        out_file.close()
    elif menu_choice == "D":
        print("Incomplete projects: ")
        for project in project if project.completion_percent != 100
        print("Completed Projects: ")
        for project in project if project.completion_percent == 100
    elif menu_choice == "F":

    elif menu_choice == "A":

    elif menu_choice == "U":

    else:
        "Please enter a valid input"
    print(MENU)
