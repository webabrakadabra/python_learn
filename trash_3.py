class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.count("@") == 1 and "." in email[email.index("@"):]:
            self.__email = email
        else:
            print("Ошибочная почта")
    email = property(fget=get_email, fset=set_email)

