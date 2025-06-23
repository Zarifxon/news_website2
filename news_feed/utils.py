# news/utils.py

def latin_to_cyrillic(text):
    multi_letters = {
        'sh': 'ш', 'ch': 'ч', 'ng': 'нг', 'ya': 'я', 'yo': 'ё',
        'yu': 'ю', 'o‘': 'ў', 'g‘': 'ғ', "o'": 'ў', "g'": 'ғ'
    }

    letters = {
        'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ',
        'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
        'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в',
        'x': 'х', 'y': 'й', 'z': 'з',
        'ʼ': 'ъ', "'": 'ъ', "’": 'ъ'
    }

    result = ''
    i = 0
    while i < len(text):
        if i+1 < len(text):
            pair = text[i:i+2].lower()
            if pair in multi_letters:
                result += multi_letters[pair]
                i += 2
                continue
        char = text[i].lower()
        result += letters.get(char, char)
        i += 1
    return result


def cyrillic_to_latin(text):
    multi_letters = {
        'ш': 'sh', 'ч': 'ch', 'нг': 'ng', 'я': 'ya', 'ё': 'yo',
        'ю': 'yu', 'ў': "o‘", 'ғ': "g‘", 'ъ': "'", 'ь': ''
    }

    letters = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'j',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'қ': 'q', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'x', 'ҳ': 'h', 'э': 'e'
    }

    result = ''
    i = 0
    while i < len(text):
        if i+1 < len(text):
            pair = text[i:i+2].lower()
            if pair in multi_letters:
                result += multi_letters[pair]
                i += 2
                continue
        char = text[i].lower()
        result += multi_letters.get(char, letters.get(char, char))
        i += 1
    return result
