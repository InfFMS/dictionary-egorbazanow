# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
alph = {
    'а': '@',  'б': '#',  'в': '$',  'г': '%',  'д': '^',  'е': '&',  'ё': '*',
    'ж': '(',  'з': ')',  'и': '-',  'й': '+',  'к': '=',  'л': '{',  'м': '}',
    'н': '[',  'о': ']',  'п': ':',  'р': ';',  'с': '"',  'т': "'",  'у': '<',
    'ф': '>',  'х': ',',  'ц': '.',  'ч': '/',  'ш': '?',  'щ': '!',  'ъ': '`',
    'ы': '~',  'ь': '_',  'э': '1',  'ю': '2',  'я': '3',  ' ': '|'
}
decipher_key = {v: k for k, v in alph.items()}

def encrypt(text):
    text = text.lower()
    return ''.join(alph.get(ch, ch) for ch in text)
def decrypt(encoded_text):
    return ''.join(decipher_key.get(ch, ch) for ch in encoded_text)
message = "привет шпион"
encoded = encrypt(message)
decoded = decrypt(encoded)

print("Оригинал:     ", message)
print("Зашифровано:  ", encoded)
print("Дешифровано:  ", decoded)

