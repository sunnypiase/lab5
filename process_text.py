import os
import re

def custom_sort_key(word):
    # Словник для визначення порядку сортування літер
    ukr_alphabet_order = {
        'а': 0, 'б': 1, 'в': 2, 'г': 3, 'ґ': 4, 'д': 5, 'е': 6, 'є': 7, 'ж': 8, 'з': 9, 'и': 10, 'і': 11, 'ї': 12,
        'й': 13, 'к': 14, 'л': 15, 'м': 16, 'н': 17, 'о': 18, 'п': 19, 'р': 20, 'с': 21, 'т': 22, 'у': 23, 'ф': 24,
        'х': 25, 'ц': 26, 'ч': 27, 'ш': 28, 'щ': 29, 'ь': 30, 'ю': 31, 'я': 32
    }

    # Функція для перетворення слова в відповідний ключ для сортування
    def get_sort_key(char):
        if char in ukr_alphabet_order:
            return ukr_alphabet_order[char]
        return char

    # Перетворення слова в нижній регістр для правильного порівняння
    word = word.lower()

    # Слова, які починаються з латинської літери, переводимо на початок
    if word[0].isalpha() and word[0] < 'а':
        return (0, word)

    # Визначення порядку сортування за українською абеткою
    order = [get_sort_key(char) for char in word]
    return (1, order)

def read_and_process_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.readline()
            print("Перше речення з файлу:")
            print(text)

            # Використовуємо регулярний вираз для поділу рядка на слова
            words = re.findall(r'\b\w+\b', text)

            # Відсортовуємо слова з використанням кастомного ключа сортування
            cleaned_words = sorted(words, key=custom_sort_key)

            print("\nСлова у відсортованому порядку:")
            print(cleaned_words)
            print("\nКількість слів:", len(cleaned_words))

    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    filename = "text_file.txt"
    read_and_process_text_file(filename)
