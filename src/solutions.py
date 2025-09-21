# Reference solutions for Python data exercises
# Includes completed implementations for comparison and learning

from __future__ import annotations
from typing import Dict, List, Tuple, Iterable, Any

def company_name(data: Dict[str, Any]) -> str:
    return str(data.get("company", ""))

def total_hours_by_employee(data: Dict[str, Any]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for emp in data.get("employees", []):
        name = emp.get("name", "")
        total = 0
        for proj in emp.get("projects", []):
            try:
                total += int(proj.get("hours", 0))
            except Exception:
                pass
        result[name] = total
    return result

def total_hours_by_project(data: Dict[str, Any]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for emp in data.get("employees", []):
        for proj in emp.get("projects", []):
            pname = str(proj.get("name", ""))
            try:
                h = int(proj.get("hours", 0))
            except Exception:
                h = 0
            result[pname] = result.get(pname, 0) + h
    return result

def department_with_most_hours(data: Dict[str, Any]) -> Tuple[str, int]:
    dep_hours: Dict[str, int] = {}
    for emp in data.get("employees", []):
        dep = str(emp.get("department", ""))
        for proj in emp.get("projects", []):
            try:
                h = int(proj.get("hours", 0))
            except Exception:
                h = 0
            dep_hours[dep] = dep_hours.get(dep, 0) + h
    if not dep_hours:
        return ("", 0)
    dep = max(dep_hours, key=lambda k: dep_hours[k])
    return dep, dep_hours[dep]

def employees_with_skill(data: Dict[str, Any], skill: str) -> List[str]:
    target = skill.strip().lower()
    found: List[str] = []
    for emp in data.get("employees", []):
        skills = [str(s).lower() for s in emp.get("skills", [])]
        if target in skills:
            found.append(emp.get("name", ""))
    return sorted(found)

def employees_on_large_projects(data: Dict[str, Any], min_hours: int = 100) -> List[str]:
    res: List[str] = []
    for emp in data.get("employees", []):
        for proj in emp.get("projects", []):
            try:
                h = int(proj.get("hours", 0))
            except Exception:
                h = 0
            if h > min_hours:
                res.append(emp.get("name", ""))
                break
    return sorted(list(dict.fromkeys(res)))
