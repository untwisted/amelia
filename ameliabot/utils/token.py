""" This module breaks sequence of parameters as follows.
    print token.tokenizer(r'arg1 arg2 arg3 "word1 word2 word3" "word3 \" word4 \"" "word5 word6 word7"') 
    ['arg1', 'arg2', 'arg3', 'word1 word2 word3', 'word3 " word4 "', 'word5 word6 word7']
"""


from re import sub, findall, compile

ARG_STR = '[^" ]+|"[^"]+"'
ARG_REG = compile(ARG_STR)
FLAG_STR = '\(([0-9]+)\)'
FLAG_REG = compile(FLAG_STR)

def scape(data):
    mapping = dict()

    def replace(matchobj):
        char = matchobj.group(1)

        while data.find('(%s)' % replace.count) >= 0:
            replace.count = replace.count + 1

        mapping[replace.count] = char

        chunk = '(%s)' % replace.count 
        replace.count = replace.count + 1
        return chunk

    replace.count = 0

    struct = sub(r'\\(.)', replace, data)
    return mapping, struct

def tokenizer(data):
    mapping, struct = scape(data)
    chunk_list = findall(ARG_REG, struct)

    chunk_list = map(
                        lambda x: sub('^"|"$', '', x), 
                        chunk_list
                    )

    def replace(matchobj):
        char = mapping.get(int(matchobj.group(1)))
        return char
            
    new_list = list()

    for ind in chunk_list:
        chunk = sub(FLAG_REG, replace, ind)
        new_list.append(chunk)

    return new_list

