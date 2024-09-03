def validate(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not any(char.islower() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char in ['$', '#', '@'] for char in password):
        return False
    else:
        return True


def main():
    print(validate("A753d#$"))


if __name__ == "__main__":
    main()
