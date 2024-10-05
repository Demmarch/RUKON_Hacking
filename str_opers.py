def count_characters(text):
    return len(text)

def find_substring(text, substring):
    if substring in text:
        return f"Подстрока '{substring}' найдена в строке"
    else:
        return f"Подстрока '{substring}' не найдена в строке"

def replace_characters(text, old, new):
    return text.replace(old, new)