

class User:
    def __init__(self, name, surname, email, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['surname'], data['email'], data['phone'])
