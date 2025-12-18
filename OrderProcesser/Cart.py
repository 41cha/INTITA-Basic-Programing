class Cart():

    def __init__(self):
        self.__items = []
        self.available_products = {
            '1': 10,
            '2': 15,
            '3': 8
        }
        
    def add_item(self, item, quantity):
        
        if quantity <= 0:
            raise ValueError("Кількість товару повинна бути більшою за нуль.")

        if self.available_products[item] < quantity:
            raise ValueError("Недостатня кількість товару на складі.")
        
        self.__items.append((item, quantity))
        
        print(f"Додано товар {item} у кількості {quantity} до кошика.")
        
cart = Cart()
cart.add_item('1', 14)