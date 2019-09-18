class User:
    def __init__(self, name):
        self.name = name
        self.email = "email+" + self.name.lower().replace(" ", "_") + "@gmail.com"
        self.phone = "11 1 1111 1111"
        self.password = "1234567a"
