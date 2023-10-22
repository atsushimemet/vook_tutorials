from models.user import User


def main():
    user_data = {"name": "John Doe", "email": "john.doe@example.com", "age": 25}

    user = User(**user_data)
    print(user.dict())


if __name__ == "__main__":
    main()
