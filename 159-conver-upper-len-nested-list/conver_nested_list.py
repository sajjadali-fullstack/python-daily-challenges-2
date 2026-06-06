# inp : 'python is simple to learn' [QST]
# out : [['PYTHON',6],['IS',2.......]]

input_string = 'python is simple to learn'

out = [[word.upper(), len(word)] for word in input_string.split()]
print(out)
