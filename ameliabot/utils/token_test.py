import token

#mapping, struct = token.scape('''test \\\ e''')

print token.tokenizer(r'arg1 arg2 arg3 "word1 word2 word3" "word3 \" word4 \"" "word5 word6 word7"')


