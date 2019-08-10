import requests
import sys
from DictionaryServices import DCSGetTermRangeInString, DCSCopyTextDefinition

class pycolor:
    FG_RED = '\033[31m'
    BG_RED = '\033[41m'
    END = '\033[0m'

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
    result = get_dict_definition(word).encode(ENCODING)
    if result != "< Not found >" and len(sys.argv) == 3:
        split = result.split(sys.argv[2])
        for i in range(len(split)-1):
            sys.stdout.write(split[i] + pycolor.BG_RED + sys.argv[2] + pycolor.END)
        print(split[len(split)-1])
    else:
        print(result)

def get_dict_definition(word):
    word_range = DCSGetTermRangeInString(DICTIONARY, word, OFFSET)
    try:
        word_definition = DCSCopyTextDefinition(DICTIONARY, word, word_range)
    except IndexError as e:
        word_definition = "< Not found >"
    return word_definition
