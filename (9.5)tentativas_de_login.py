class User:
    def __init__(self, user, age, location):
        self.user = user
        self.age = age
        self.location = location
        self.login = 0

    def describe_user(self):
        print(f'Informações sobre o usuário:\nUsuário: {self.user}\nIdade: {self.age}\nLocalidade: {self.location}')

    def greet_user(self):
        print(f'Olá {self.user} seja bem vindo(a)!')

    def increment_login_attempts(self):
        self.login += 1
        print (f"{self.login} tentativas de login")
    def reset_login_attempts(self):
        self.login = 0
        print(f"{self.login} tentativas de login")

user1 = User('luan', 20, 'araçariguama')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

