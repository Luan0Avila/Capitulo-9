class User:
    def __init__(self, user, age, location):
        self.user = user
        self.age = age
        self.location = location
        self.login = 0

    def describe_user(self):
        print(f'Informações sobre o usuário:\nUsuário: {
              self.user}\nIdade: {self.age}\nLocalidade: {self.location}')

    def greet_user(self):
        print(f'Olá {self.user} seja bem vindo(a)!')

    def increment_login_attempts(self):
        self.login += 1
        print(f"{self.login} tentativas de login")

    def reset_login_attempts(self):
        self.login = 0
        print(f"{self.login} tentativas de login")

class Admin(User):
    def __init__(self, user, age, location):
        super().__init__(user, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f'This is some privleges for admin:\n {self.privileges}')

admin0 = Admin('luan', 20, 'aracariguama')
admin0.show_privileges()