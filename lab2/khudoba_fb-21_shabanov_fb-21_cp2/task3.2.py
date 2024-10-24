from collections import Counter


# Функція для знаходження ключа
def find_key(file_name, key_len):
    with open(file_name, 'r', encoding='utf-8') as f:
        cipher_text = ''.join(f.read().split())  # Видаляємо пробіли та нові рядки

    # Розбиваємо текст на групи за довжиною ключа
    grouped_blocks = [''.join([cipher_text[i] for i in range(pos, len(cipher_text), key_len)]) for pos in
                      range(key_len)]

    key = []
    for block in grouped_blocks:
        most_common_letter = Counter(block).most_common(1)[0][0]  # Найчастіша літера в групі
        shift = (ord(most_common_letter) - ord('о')) % 32  # Порівнюємо з "о", бо вона найчастіша в рос. мові
        key_letter = chr(ord('а') + shift)
        key.append(key_letter)

    return ''.join(key)


# Функція для розшифровки тексту на основі ключа
def decrypt_vigenere(cipher_text, key):
    decrypted_text = []
    key_len = len(key)

    for i, char in enumerate(cipher_text):
        if char in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':  # Перевірка чи символ в алфавіті
            shift = ord(key[i % key_len]) - ord('а')
            decrypted_char = chr((ord(char) - ord('а') - shift) % 32 + ord('а'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Якщо це не літера, просто додаємо без змін

    return ''.join(decrypted_text)


# Основна функція, яка знаходить ключ і розшифровує текст
def main():
    file_name = 'task3.txt'
    key_len = 15

    # Знаходимо ключ
    key = find_key(file_name, key_len)
    print(f'Знайдений ключ: {key}')

    # Читаємо шифротекст і розшифровуємо його
    with open(file_name, 'r', encoding='utf-8') as f:
        cipher_text = ''.join(f.read().split())  # Видаляємо пробіли та нові рядки

    decrypted_text = decrypt_vigenere(cipher_text, key)

    # Зберігаємо розшифрований текст у файл
    with open('solve.txt', 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
    print("Розшифрований текст збережено в solve.txt")


# Викликаємо основну функцію
if __name__ == '__main__':
    main()