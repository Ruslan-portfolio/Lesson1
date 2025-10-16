from EmployeeApi import EmployeeApi

api = EmployeeApi("http://5.101.50.27:8000") 

def test_get_employee_info():
   employee_id = 1
   body = api.get_employee_info(employee_id)
   assert len(body) > 0     

def test_create_employee():
   company_id = 1

   employees_before = api.get_list_employee(company_id)
   len_before = len(employees_before)

   name="Ванек"
   last_name="Ваньков"  
   midle_name="Ванькович"
   id=company_id  
   e_mail="Vanek@van.ss"
   phone="984823498234"
   birthdate="2222-12-22"

   api.add_employee(name, last_name, midle_name, id, e_mail, phone, birthdate)

   employees_after = api.get_list_employee(company_id)
   len_after = len(employees_after)
    
   last_employee = employees_after[-1]
   assert last_employee["email"] == "Vanek@van.ss"
   assert len_after == len_before + 1

def test_get_list_employee():
   company_id = 1
   employees = api.get_list_employee(company_id)
   assert len(employees) > 1
   for employee in employees:
      assert "first_name" in employee
      assert "last_name" in employee
      assert "email" in employee

def test_edit():
   company_id = 1

   employees_before = api.get_list_employee(company_id)

   new_employee_data = {
        "first_name": "Ванек",
        "last_name": "Ваньков", 
        "middle_name": "Ванькович",
        "company_id": company_id,
        "email": "Vanek@van.ss",
        "phone": "984823498234",
        "birthdate": "2222-12-22"
    }
   api.add_employee(**new_employee_data)
   
   employees_after = api.get_list_employee(company_id)
   assert len(employees_after) == len(employees_before) + 1

   new_employee = employees_after[-1]
   employee_id = new_employee["id"]

   update_data = {
        "last_name": "Александров",
        "email": "Sashka@mail.ru",
        "phone": "987985947"
    }

   updated_employee = api.patch_employee(employee_id, **update_data)

   assert updated_employee["last_name"] == update_data["last_name"]
   assert updated_employee["email"] == update_data["email"]
   assert updated_employee["phone"] == update_data["phone"]


