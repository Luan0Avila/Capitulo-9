class User:
    def __init__(self, user, age, location):
        self.user = user
        self.age = age
        self.location = location

    def describe_user(self):
        print(f'Informações sobre o usuário:\nUsuário: {self.user}\nIdade: {self.age}\nLocalidade: {self.location}')

    def greet_user(self):
        print(f'Olá {self.user} seja bem vindo(a)!')

luan = User('Luan', 20, 'Araçariguama')
luan.greet_user()
luan.describe_user()

ladyane = User('Ladyane', 19, 'Araçariguama')
ladyane.greet_user()
ladyane.describe_user()

mateus = User('Mateus', 40, 'Mairinque')
mateus.greet_user()
mateus.describe_user()
    
    