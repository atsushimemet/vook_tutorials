from models.user import User
from pydantic import ValidationError


def main():
    # user_data = {"name": "John Doe", "email": "john.doe@example.com", "age": 25}
    # user_data = {"name": "John Doe", "email": "john.doe@example.com", "age": "25"}
    user_data = {"name": "John Doe", "email": "john.doe@example.com", "age": "25a"}

    try:
        user = User(**user_data)
        print(user.dict())
    except ValidationError as e:
        print(e.errors())


if __name__ == "__main__":
    main()
