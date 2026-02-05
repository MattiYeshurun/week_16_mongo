from connection import collection, client

def get_collection(collection):
    return collection

def ping_db_health():
    try:
        client.admin.command("ping")
        print("MongoDB connect ✔️")
    except Exception as e:
        print("No connection to MongoDB ❌")
        print(e)

def get_all_employes():
    employes = get_collection(collection)
    docs = list(employes.find())
    return serialize_docs(docs)

def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]

def run_query(query, projection=None, sort=None):
    cursor = collection.find(query, projection)   
    if sort:
        cursor = cursor.sort(sort) 
    results = list(cursor)    
    return results


def get_engineering_high_salary_employees():
    query = run_query({"job_role.title": "Engineer","salary": {"$gt": 65000}}, {"employee_id": 1, "name": 1, "salary": 1, "_id": 0 })
    return query

def get_employees_by_age_and_role():
    query = run_query({"age": {"$gt": 30, "$lt": 45},"$or": [{"job_role.title": "Engineer"}, {"job_role.title": "Specialist"}]}, {"_id": 0})
    return query

def get_top_seniority_employees_excluding_hr():
    query = run_query({"job_role.department": {"$ne": "HR"}.sort("years_at_company", -1).limit(7)})
    return query

def get_employees_by_age_or_seniority():
    pass

def get_managers_excluding_departments():
    pass

def get_employees_by_lastname_and_age():
    pass
