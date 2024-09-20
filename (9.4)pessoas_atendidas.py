class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        print(f'O restaurante {self.restaurant_name} é o restaurante{self.cuisine_type} mais famoso da cidade\nVeja abaixo nosso cardápio:')
        print('-------------------------\n-------------------------\n-------------------------')

    def open_restaurant(self,):
        print(f'O restaurante acabou de abrir')

    def number_served(self):
        print(f'Foram atendidos um total de {self.num_served} mesas.')

joquinha = Restaurant('Joquinha', 'brasileiro')
joquinha.num_served = 11
joquinha.open_restaurant()
joquinha.describe_restaurant()
joquinha.number_served()

