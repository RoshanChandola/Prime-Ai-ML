class Product:
    count =0
    def __init__(self, name, price):
        self.name=name
        self.price=price
        Product.count+= 1
    def get_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price}")
    @classmethod
    def get_count(cls):
        print(f"Total Products: {cls.count}")
    @staticmethod
    def total_discout (price, discount):
        return price - (price * discount / 100)
p1=Product("Laptop", 1200)
p1.get_info()  # Output: Product Name: Laptop, Price: $1200
p2=Product("Smartphone", 800)
p2.get_info()  # Output: Product Name: Smartphone, Price: $800
Product.get_count()  # Output: Total Products: 2
p1. total_price = Product.total_discout(p1.price, 10)
print(f"Price after discount for {p1.name}: ${p1.total_price}")

