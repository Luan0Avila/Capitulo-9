class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O restaurante {self.restaurant_name} é o restaurante{self.cuisine_type} mais famoso da cidade\nVeja abaixo nosso cardápio:')
        print('-------------------------\n-------------------------\n-------------------------')

    def open_restaurant(self,):
        print(f'O restaurante acabou de abrir')

jacao = Restaurant('Jacao', 'Francês')
jacao.open_restaurant()
jacao.describe_restaurant()

rolander = Restaurant('Rolander', 'Paraguaio')
rolander.open_restaurant()
rolander.describe_restaurant()

mario = Restaurant('Mario', 'italiano')
mario.open_restaurant()
mario.describe_restaurant()