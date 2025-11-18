import pytest
from sqlalchemy import create_engine, inspect, text

class EmployeeTable:
    __scripts = {
        "get employee info": "select * from employee where id = :select_id",
        "insert employee": "INSERT INTO employee (is_active, first_name, last_name, phone, company_id) VALUES (:is_active, :first_name, :last_name, :phone, :company_id)",
        "get company employees": "select * from employee where company_id = :company_id",
        "delete employee": "delete from employee where id = :id",
        "get MAX id": "SELECT MAX(id) FROM employee",
        "update employee": "UPDATE employee SET last_name = :last_name, email = :email, phone = :phone WHERE id = :id"
    }

    def __init__(self,connection_string):
        self.engine = create_engine(connection_string)
        self.connection = self.engine.connect()

    def get_employee_info(self, id):
        sql = text(self.__scripts["get employee info"])
        result = self.connection.execute(sql, {"select_id": id})
        return result.mappings().fetchall()
    
    def create(self, first_name, last_name, phone, company_id, is_active=True):
        self.sql = text(self.__scripts["insert employee"])
        self.connection.execute(self.sql, {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone, 
            "company_id": company_id,
            "is_active": is_active
        })
        self.connection.commit()

    def get_max_id(self):
        sql = text(self.__scripts["get MAX id"])
        result = self.connection.execute(sql).fetchall()
        return result[0][0]
    
    def delete(self, id):
        self.sql = text(self.__scripts["delete employee"])
        self.connection.execute(self.sql, {"id": id})
        self.connection.commit()

    def get_company_employees(self, company_id):
        sql = text(self.__scripts["get company employees"])
        result = self.connection.execute(sql, {"company_id": company_id})
        return result.mappings().fetchall()

    def update_employee(self, employee_id, last_name, email, phone):
        sql = text(self.__scripts["update employee"])
        self.connection.execute(sql, {
            "id": employee_id,
            "last_name": last_name,
            "email": email,
            "phone": phone
        })
        self.connection.commit()