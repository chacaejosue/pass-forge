from .generator import MIN_LENGTH, generate_password


def main():
    while True:
        try:
            entry = input(
                f"Longitud de la contraseña (mínimo {MIN_LENGTH}): "
            )

            length = int(entry)
            break

        except ValueError:
            print(f'"{entry}" no es un número válido.')

    if length < MIN_LENGTH:
        print(
            f"Por seguridad, ajustaremos la longitud a {MIN_LENGTH}."
        )

    password = generate_password(length)

    print(f"Tu contraseña segura: {password}")


if __name__ == "__main__":
    main()