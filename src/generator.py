import secrets
import string


MIN_LENGTH = 12


def generate_password(length):
    """
    Genera una contraseña utilizando una fuente de aleatoriedad
    criptográficamente segura.
    """
    if length < MIN_LENGTH:
        length = MIN_LENGTH

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    characters = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    all_characters = lowercase + uppercase + digits + symbols
    remaining = length - len(characters)

    characters.extend(
        secrets.choice(all_characters)
        for _ in range(remaining)
    )

    for i in range(len(characters) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        characters[i], characters[j] = characters[j], characters[i]

    return "".join(characters)