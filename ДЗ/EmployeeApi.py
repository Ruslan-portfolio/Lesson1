import requests

class EmployeeApi:

    def __init__(self, url):
        self.url = url 

    def get_employee_info(self, employee_id):
        resp = requests.get(self.url + '/info/' + str(employee_id))
        return resp.json()
    
    def get_token(self, user = 'harrypotter', password = 'expelliarmus'):
        creds = {
            'username': user ,
            'password': password
        }

        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    def add_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate ):
        employee = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee/create', json=employee, headers = my_headers)
        return resp.json()

    def get_list_employee(self, company_id):
        resp = requests.get(self.url + '/employee/list/' + str(company_id))
        return resp.json()
    
    def patch_employee(self, new_phone, new_last_name, new_e_mail, new_id):
        employee_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{new_id}?client_token={employee_token}"

        new_employee = {
        "last_name": new_last_name,
        "email": new_e_mail,
        "phone": new_phone
    }
        resp = requests.patch(url_with_token, json=new_employee)    
        
        return resp.json()   
