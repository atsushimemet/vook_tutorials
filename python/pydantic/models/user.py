from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    name: constr(min_length=2, max_length=100)
    email: EmailStr
    age: int
