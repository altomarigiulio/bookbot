def word_count(file_path):
    counter = 0
    file_content = open(file_path)
    text = file_content.read()
    words = text.split()
    for i in range (len(words)):
        counter+=1
    print(f"Found {counter} total words")

def stat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_content:
        text = file_content.read().lower()
    char_count = count_characters(text)
    sort_characters_by_count(char_count)

def count_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Filtra solo lettere
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_characters_by_count(char_count):
    sorted_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_list:
        print(f"{char}: {count}")

