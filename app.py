import requests
import sys
from DictionaryServices import DCSGetTermRangeInString, DCSCopyTextDefinition

ENCODING = 'utf-8'
DICTIONARY = None
OFFSET = 0

config = {
    'print_word': False,
}

def main():
    word = sys.argv[1].decode(ENCODING)
    if config['print_word']:
        print(word.encode(ENCODING))
    print(get_dict_definition(word).encode(ENCODING))

def get_dict_definition(word):
    word_range = DCSGetTermRangeInString(DICTIONARY, word, OFFSET)
    try:
        word_definition = DCSCopyTextDefinition(DICTIONARY, word, word_range)
    except IndexError as e:
        word_definition = '<Not found the translation>'
    return word_definition
