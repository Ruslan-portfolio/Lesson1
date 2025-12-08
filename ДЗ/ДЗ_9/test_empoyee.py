import allure
from EmployeeTable import EmployeeTable


db = EmployeeTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


@allure.title("Тест создания и получения сотрудника")
@allure.description("Проверяет создание сотрудника и получение его данных")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_and_get_employee():
    """
    Проверяет создание сотрудника и получение его данных из базы.
    """
    
    with allure.step("Создать сотрудника"):
        db.create("Иван", "Петухов", "89891235566", 1)
        max_id = db.get_max_id()

    with allure.step("Получить данные сотрудника"):
        db_result = db.get_employee_info(max_id)

    with allure.step("Проверить корректность данных"):
        assert len(db_result) == 1
        assert db_result[0]["first_name"] == "Иван"
        assert db_result[0]["last_name"] == "Петухов"
        assert db_result[0]["phone"] == "89891235566"
        assert db_result[0]["company_id"] == 1

    with allure.step("Удалить тестового сотрудника"):
        db.delete(max_id)


@allure.title("Тест получения сотрудников компании")
@allure.description("Проверяет получение всех сотрудников компании")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_get_company_employees():
    """
    Проверяет получение списка сотрудников компании.
    """
    company_id = 1
    
    with allure.step(f"Получить сотрудников компании {company_id}"):
        employees = db.get_company_employees(company_id)
    
    with allure.step("Проверить данные сотрудников"):
        assert len(employees) > 0
        for employee in employees:
            assert "first_name" in employee
            assert "last_name" in employee
            assert "company_id" in employee
            assert employee["company_id"] == company_id


@allure.title("Тест обновления данных сотрудника")
@allure.description("Проверяет обновление данных сотрудника в базе")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_employee():
    """
    Проверяет обновление данных сотрудника.
    """
    
    with allure.step("Создать тестового сотрудника"):
        db.create("Петр", "Иванов", "89991234567", 1)
        max_id = db.get_max_id()

    with allure.step("Обновить данные сотрудника"):
        db.update_employee(max_id, "Сидоров", "sidorov@mail.ru", "87771234567")

    with allure.step("Проверить обновленные данные"):
        updated_employee = db.get_employee_info(max_id)
        assert updated_employee[0]["last_name"] == "Сидоров"
        assert updated_employee[0]["email"] == "sidorov@mail.ru"
        assert updated_employee[0]["phone"] == "87771234567"

    with allure.step("Удалить тестового сотрудника"):
        db.delete(max_id)


@allure.title("Тест удаления сотрудника")
@allure.description("Проверяет удаление сотрудника из базы данных")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee():
    """
    Проверяет удаление сотрудника из базы данных.
    """
    
    with allure.step("Создать тестового сотрудника"):
        db.create("Алексей", "Петров", "85551234567", 1)
        max_id = db.get_max_id()

    with allure.step("Проверить создание"):
        employee_before = db.get_employee_info(max_id)
        assert len(employee_before) == 1

    with allure.step("Удалить сотрудника"):
        db.delete(max_id)

    with allure.step("Проверить удаление"):
        employee_after = db.get_employee_info(max_id)
        assert len(employee_after) == 0


