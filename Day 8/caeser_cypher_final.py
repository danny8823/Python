alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ''
    if shift_amount > 12:
        print('Number too large')
    else:
        for letter in original_text:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]

    print(encrypted_text)


def decrypt(original_text, shift_amount):
    decrypted_text = ''
    for letter in original_text:
        decrypted_text += alphabet[alphabet.index(letter) - shift_amount]

    print(decrypted_text)


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
