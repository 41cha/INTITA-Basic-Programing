
class OrderProcesser:
    def __init__(self):
        pass

    def handle_order(self, order):
        self.__registration()
        self.__check_availability()
        self.__form_documents()
        self.__broned_products()
        self.__payment()
        self.__delivery()
    
    def __registration(self):
        print("Реєстрація замовлення")
        
    def __check_availability(self):
        print("Перевірка наявності товарів")
        
    def __form_documents(self):
        print("Формування документів")
        
    def __broned_products(self):
        print("Резервування товарів")
        
    def __payment(self):
        print("Обробка оплати")

    def __delivery(self):
        print("Організація доставки")


processor = OrderProcesser()
order = {'id': '001', 'customer': 'Іван Петренко'}
processor.handle_order(order)