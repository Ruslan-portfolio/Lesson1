import pytest
from sqlalchemy import create_engine, inspect, text
import allure


class EmployeeTable:
    """
    Класс для работы с таблицей employee в базе данных.
    Предоставляет методы для CRUD операций с сотрудниками.
    """
    
    __scripts = {
        "get employee info": "select * from employee where id = :select_id",
        "insert employee": "INSERT INTO employee (is_active, first_name, last_name, phone, company_id) VALUES (:is_active, :first_name, :last_name, :phone, :company_id)",
        "get company employees": "select * from employee where company_id = :company_id",
        "delete employee": "delete from employee where id = :id",
        "get MAX id": "SELECT MAX(id) FROM employee",
        "update employee": "UPDATE employee SET last_name = :last_name, email = :email, phone = :phone WHERE id = :id"
    }

    def __init__(self, connection_string):
        """
        Создает соединение с базой данных.
        
        Args:
            connection_string: Строка подключения к базе данных
        """
        self.engine = create_engine(connection_string)
        self.connection = self.engine.connect()

    @allure.step("Получить информацию о сотруднике с id={id}")
    def get_employee_info(self, id):
        """
        Получает информацию о сотруднике по его ID.
        
        Args:
            id: ID сотрудника
            
        Returns:
            Список словарей с информацией о сотруднике
        """
        sql = text(self.__scripts["get employee info"])
        result = self.connection.execute(sql, {"select_id": id})
        return result.mappings().fetchall()
    
    @allure.step("Создать сотрудника: {first_name} {last_name}")
    def create(self, first_name, last_name, phone, company_id, is_active=True):
        """
        Создает нового сотрудника в базе данных.
        
        Args:
            first_name: Имя сотрудника
            last_name: Фамилия сотрудника
            phone: Телефон сотрудника
            company_id: ID компании
            is_active: Активен ли сотрудник
        """
        self.sql = text(self.__scripts["insert employee"])
        self.connection.execute(self.sql, {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone, 
            "company_id": company_id,
            "is_active": is_active
        })
        self.connection.commit()

    @allure.step("Получить максимальный ID сотрудника")
    def get_max_id(self):
        """
        Получает максимальный ID из таблицы сотрудников.
        
        Returns:
            Максимальный ID сотрудника
        """
        sql = text(self.__scripts["get MAX id"])
        result = self.connection.execute(sql).fetchall()
        return result[0][0]
    
    @allure.step("Удалить сотрудника с id={id}")
    def delete(self, id):
        """
        Удаляет сотрудника по его ID.
        
        Args:
            id: ID сотрудника для удаления
        """
        self.sql = text(self.__scripts["delete employee"])
        self.connection.execute(self.sql, {"id": id})
        self.connection.commit()

    @allure.step("Получить сотрудников компании {company_id}")
    def get_company_employees(self, company_id):
        """
        Получает всех сотрудников компании.
        
        Args:
            company_id: ID компании
            
        Returns:
            Список словарей с сотрудниками компании
        """
        sql = text(self.__scripts["get company employees"])
        result = self.connection.execute(sql, {"company_id": company_id})
        return result.mappings().fetchall()

    @allure.step("Обновить данные сотрудника {employee_id}")
    def update_employee(self, employee_id, last_name, email, phone):
        """
        Обновляет данные сотрудника.
        
        Args:
            employee_id: ID сотрудника
            last_name: Новая фамилия
            email: Новый email
            phone: Новый телефон
        """
        sql = text(self.__scripts["update employee"])
        self.connection.execute(sql, {
            "id": employee_id,
            "last_name": last_name,
            "email": email,
            "phone": phone
        })
        self.connection.commit()