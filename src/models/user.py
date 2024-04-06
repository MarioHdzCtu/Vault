from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str
    recovery_email: str | None = None

    def get_dict(self):
        return {'id': self.id, 'username':self.username, 'recovery_email': self.recovery_email}