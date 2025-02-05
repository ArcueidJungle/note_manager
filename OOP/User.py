class User:
    def __init__(self, username, password = None):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passw):
        if len(passw) < 8:
            raise ValueError('("Пароль должен быть не короче 8 символов")')
        else:
            self.__password = passw

    def __repr__(self):
        return f'User({self.username})'

user = User("alex")
user.password = "secure123"
print(user)  # "User(alex)"