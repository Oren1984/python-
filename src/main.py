# Entry point for Python data exercises
# Contains practice tasks and functions to implement

import json
from pathlib import Path
from .solutions import (
    company_name, total_hours_by_employee, total_hours_by_project,
    department_with_most_hours, employees_with_skill, employees_on_large_projects,
)

def load_data(path: str = "employees.json"):
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def main():
    data = load_data()
    print("=== Company ===")
    print(company_name(data))

    print("\n=== Total Hours by Employee ===")
    for name, hours in total_hours_by_employee(data).items():
        print(f"{name}: {hours}h")

    print("\n=== Total Hours by Project ===")
    for proj, hours in total_hours_by_project(data).items():
        print(f"{proj}: {hours}h")

    dep, hours = department_with_most_hours(data)
    print(f"\n=== Department with Most Hours ===\n{dep} ({hours}h)")

    print("\n=== Employees with 'Python' Skill ===")
    for name in employees_with_skill(data, "Python"):
        print(name)

    print("\n=== Employees on Large Projects (>100h) ===")
    for name in employees_on_large_projects(data, min_hours=100):
        print(name)

if __name__ == "__main__":
    main()
