import requests


class TodoListAPI:
    """Класс для работы с API сервиса задач Sky Todo List"""
    
    def __init__(self, base_url="https://sky-todo-list.herokuapp.com"):
        self.base_url = base_url
    
    def get_all_tasks(self):
        """Получение списка всех задач"""
        response = requests.get(f"{self.base_url}/")
        print(f"GET {self.base_url}/ - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def get_task(self, task_id):
        """Получение конкретной задачи по ID"""
        response = requests.get(f"{self.base_url}/task/{task_id}")
        print(f"GET {self.base_url}/task/{task_id} - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def create_task(self, title):
        """Создание новой задачи"""
        task_data = {
            "title": title,
        }
        response = requests.post(f"{self.base_url}/task", json=task_data)
        print(f"POST {self.base_url}/task - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def update_task(self, task_id, new_title):
        """Переименование задачи"""
        update_data = {
            "title": new_title
        }
        response = requests.put(f"{self.base_url}/task/{task_id}", json=update_data)
        print(f"PUT {self.base_url}/task/{task_id} - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def mark_task_completed(self, task_id):
        """Отметка задачи как выполненной"""
        response = requests.patch(f"{self.base_url}/task/{task_id}")
        print(f"PATCH {self.base_url}/task/{task_id} - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def mark_task_incomplete(self, task_id):
        """Снятие отметки о выполнении"""
        # В большинстве Todo API используется тот же PATCH с изменением статуса
        # Если API не поддерживает отдельный endpoint, используем update
        update_data = {
            "completed": False
        }
        response = requests.patch(f"{self.base_url}/task/{task_id}", json=update_data)
        print(f"PATCH {self.base_url}/task/{task_id} - Status: {response.status_code}")
        response.raise_for_status()
        return response.json()
    
    def delete_task(self, task_id):
        """Удаление задачи"""
        response = requests.delete(f"{self.base_url}/task/{task_id}")
        print(f"DELETE {self.base_url}/task/{task_id} - Status: {response.status_code}")
        response.raise_for_status()
        return {"message": "Task deleted successfully", "status_code": response.status_code}