class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O restaurante {self.restaurant_name} é o restaurante{
              self.cuisine_type} mais famoso da cidade\nVeja abaixo nosso cardápio:')
        print('-------------------------\n-------------------------\n-------------------------')

    def open_restaurant(self,):
        print(f'O restaurante acabou de abrir')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def flavor_list(self):
        print('Essa é a nossa lista de sabores:')
        print(self.flavors)

sorveteria = IceCreamStand('Sorvesan','Brasileiro',['morango', 'chocolate', 'creme'])
sorveteria.flavor_list()