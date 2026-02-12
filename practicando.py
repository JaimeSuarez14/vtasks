lista = [
  1,2,3,4,5
]
print(lista)
age= 20
if age==20:
  print("tu edad es 20")

class Car:
  brand="default"
  model= "default"
  price= 100

  def __init__(self, brand, model, price):
    self.brand= brand
    self.model= model
    self.price= price

  def description(self):
    return f"{self.brand} - {self.model}"

car = Car("Mybrand", "Toyota", 1000)
print(car)
print(car.description())