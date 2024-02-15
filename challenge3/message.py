import json
from challenge3.user import User

class Message:
    def __init__(self, type_, user=None,message=None):
        self.type = type_
        self.user = user
        self.message = message

    def to_json(self):
        data = {"type": self.type,"user":""}
        if self.user:
            data["user"] = self.user.to_dict()
        if self.message:
            data["message"] = self.message
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        user_data = data.get("user",None)
        user = User.from_dict(user_data) if user_data else None
        message = data.get("message")
        if message is not None:
            return cls(data['type'], user,message)
        return cls(data['type'], user)
