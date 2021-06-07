class Client():
    def __init__(self, name, email, cpf):
        self.__name = name
        self.__email = email
        self.__cpf = cpf

    # ---name--- #
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # ---email--- #
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # ---cpf--- #
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
