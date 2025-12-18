
class Cart():

    def __init__(self):
        self.__items = []
        
        self.__available_products = {
            
            '1': 10,
            '2': 15,
            '3': 8
            
        }
        
    def add_item(self, item, quantity):
        
        if quantity <= 0:
            raise ValueError("кількість товару повинна бути більшою за нуль")
        
        if item not in self.__available_products:
            raise ValueError("товар не знайдено")

        if self.__available_products[item] < quantity:
            raise ValueError("недостатня кількість товару на складі")
        
        self.__items.append((item, quantity))
        
cart = Cart()
cart.add_item('1', 8)