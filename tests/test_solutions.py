
import json, pathlib
from src.solutions import (
    company_name, total_hours_by_employee, total_hours_by_project,
    department_with_most_hours, employees_with_skill, employees_on_large_projects,
)

DATA = json.loads(pathlib.Path("employees.json").read_text(encoding="utf-8"))

def test_company_name():
    assert isinstance(company_name(DATA), str)
    assert company_name(DATA) != ""

def test_totals_are_non_negative():
    emp = total_hours_by_employee(DATA)
    proj = total_hours_by_project(DATA)
    assert all(isinstance(v, int) and v >= 0 for v in emp.values())
    assert all(isinstance(v, int) and v >= 0 for v in proj.values())

def test_department_with_most_hours():
    dep, hours = department_with_most_hours(DATA)
    assert isinstance(dep, str)
    assert isinstance(hours, int)

def test_employees_with_skill_python():
    names = employees_with_skill(DATA, "Python")
    assert isinstance(names, list)

def test_large_projects():
    names = employees_on_large_projects(DATA, 100)
    assert isinstance(names, list)
