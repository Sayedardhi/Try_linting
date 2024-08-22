123456789012345678901234567890123456789012345678901234567890

            You have to provide the rationale for each change. Please follow PEP8 format:
            ```python
            # E0710(invalid-name):
            # If you need help, please post in the discussion forum. 
            # See https://docs.google.com/document/d/16pL9I2yJ4Q5uN_hYV4wW8m3gU-5iX1q5Z0aO_1cG4rE
            raise CustomException("Width is zero") # Raising a new style class which doesn't inherit from BaseException (E0710)
            ```
    """,
}


def run():

    print(help[command])


if __name__ == "__main__":
    command = input()
    try:
        help[command]
        if command == "exit":
            exit()
    except KeyError:
        print("Invalid command")
    run()
