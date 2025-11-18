from EmployeeTable import EmployeeTable

db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

def test_create_and_get_employee():
    # Создаем сотрудника
    db.create("Иван", "Петухов", "89891235566", 1)
    max_id = db.get_max_id()

    # Получаем данные
    db_result = db.get_employee_info(max_id)

    # Проверяем
    assert len(db_result) == 1
    assert db_result[0]["first_name"] == "Иван"
    assert db_result[0]["last_name"] == "Петухов"
    assert db_result[0]["phone"] == "89891235566"
    assert db_result[0]["company_id"] == 1

    # Чистим
    db.delete(max_id)

def test_get_company_employees():
    company_id = 1
    employees = db.get_company_employees(company_id)
    
    assert len(employees) > 0
    for employee in employees:
        assert "first_name" in employee
        assert "last_name" in employee
        assert "company_id" in employee
        assert employee["company_id"] == company_id

def test_update_employee():
    # Создаем сотрудника для теста
    db.create("Петр", "Иванов", "89991234567", 1)
    max_id = db.get_max_id()

    # Обновляем данные
    db.update_employee(max_id, "Сидоров", "sidorov@mail.ru", "87771234567")

    # Проверяем обновление
    updated_employee = db.get_employee_info(max_id)
    
    assert updated_employee[0]["last_name"] == "Сидоров"
    assert updated_employee[0]["email"] == "sidorov@mail.ru"
    assert updated_employee[0]["phone"] == "87771234567"

    # Чистим
    db.delete(max_id)

def test_delete_employee():
    # Создаем сотрудника
    db.create("Алексей", "Петров", "85551234567", 1)
    max_id = db.get_max_id()

    # Проверяем что создался
    employee_before = db.get_employee_info(max_id)
    assert len(employee_before) == 1

    # Удаляем
    db.delete(max_id)

    # Проверяем что удалился
    employee_after = db.get_employee_info(max_id)
    assert len(employee_after) == 0


