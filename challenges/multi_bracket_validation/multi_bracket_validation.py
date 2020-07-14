import re

def multi_bracket_validation(string):
    string1 = re.sub('[^\[\]\{\}\(\)]', '', string, flags=re.DOTALL)

    if len(string1) % 2 > 0:
        return False

    for _ in range(int(len(string1)/2)):
        string1 = re.sub('(\(\)|\[\]|\{\})', '', string1, flags=re.DOTALL)

    if len(string1) > 0:
        return False
    else:
        return True
