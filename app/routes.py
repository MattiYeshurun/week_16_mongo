from fastapi import APIRouter
from dal import get_collection, get_all_employes, get_employees_by_age_and_role, get_employees_by_age_or_seniority, get_employees_by_lastname_and_age, get_engineering_high_salary_employees, get_managers_excluding_departments, get_top_seniority_employees_excluding_hr

router = APIRouter()

@router.get("/employees/engineering/high-salary")
def engineering_high_salary_employees():
    return get_engineering_high_salary_employees()


@router.get("/employees/by-age-and-role")
def employees_by_age_and_role():
    return get_employees_by_age_and_role

@router.get("/employees/top-seniority")
def top_seniority_employees_excluding_hr():
    return get_top_seniority_employees_excluding_hr

@router.get("/employees/age-or-seniority")
def employees_by_age_or_seniority():
    return get_employees_by_age_or_seniority()

@router.get("/employees/managers/excluding-departments")
def managers_excluding_departments():
    return get_managers_excluding_departments

@router.get("/employees/by-lastname-and-age")
def employees_by_lastname_and_age():
    return get_employees_by_lastname_and_age
