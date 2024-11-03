import queue
import random
import string
import time

class ServiceCenter:
    def __init__(self):
        self.queue = queue.Queue()

    def generate_request(self):
        """Генеруємо випадкову заявку та додаємо її до черги."""
        request_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        request_description = ''.join(random.choices(string.ascii_lowercase, k=10))
        request = f"Заявка {request_id}: {request_description}"
        self.queue.put(request)
        print(f"Згенеровано заявку: {request}")

    def process_request(self):
        """Видаляємо заявку з черги та імітуємо її обробку."""
        if not self.queue.empty():
            request = self.queue.get()
            print(f"Обробка заявки: {request}")
        else:
            print("Черга заявок пуста.")

# Створення екземпляру сервісного центру
service_center = ServiceCenter()

# Головний цикл програми
while True:  
    service_center.generate_request()
    time.sleep(1)
    service_center.process_request()