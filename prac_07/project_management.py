"""
Project Management Program
Estimated: 1 hour 40 minutes
Actual: 2 hours 50 minutes
"""

import datetime
from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    projects = []
    extract_project_data(projects, FILENAME)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            input_filename = input("Projects filename: ")
            projects = []
            extract_project_data(projects, input_filename)
        elif menu_choice == "S":
            output_file = select_save_file()
            save_projects(output_file, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_program_details(projects)
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def save_projects(output_file, projects):
    out_file = open(output_file, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        print(f"{project.name}\t{project.date}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percent}", file=out_file)
    out_file.close()


def select_save_file():
    save_choice = input("Save to current file Y/n: ").upper()
    while save_choice != "Y" or save_choice != "N":
        print("Invalid input")
        save_choice = input("Save to current file Y/n: ").upper()
    if save_choice == "Y":
        output_file = FILENAME
    else:
        output_file = input("Save Filename: ")
    return output_file


def update_program_details(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    update_program_choice = int(input("Project choice: "))
    while update_program_choice < 0 or update_program_choice > len(projects) - 1:
        print("Invalid index")
        update_program_choice = int(input("Project choice: "))
    print(projects[update_program_choice])
    new_percentage = int(input("New Percentage: "))
    while new_percentage < 0 or new_percentage > 100:
        print("Must be between 0 and 100")
        new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    while new_priority < 1 or new_priority > 10:
        print("Must be between 1 and 10")
        new_priority = int(input("New Priority: "))
    projects[update_program_choice].completion_percent = new_percentage
    projects[update_program_choice].priority = new_priority


def add_new_project(projects):
    print("Lets add a new project")
    project_name = input("Name: ")
    project_date = input("Start date (dd/mm/yyyy): ")
    project_priority = input("Priority: ")
    project_cost = input("Cost estimate: ")
    project_percent = input("Percent complete: ")
    project = Project(project_name, project_date, project_priority, project_cost, project_percent)
    projects.append(project)


def filter_projects(projects):
    filter_date = input("Filter date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y")
    [print(project) for project in projects if
     datetime.datetime.strptime(project.date, "%d/%m/%Y") > filter_date]


def display_projects(projects):
    projects.sort()
    print("Incomplete projects: ")
    [print(project) for project in projects if project.completion_percent != 100]
    print("Completed Projects: ")
    [print(project) for project in projects if project.completion_percent == 100]


def extract_project_data(projects, filename):
    in_file = open(FILENAME)
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    in_file.close()
