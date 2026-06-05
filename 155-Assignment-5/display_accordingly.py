# Q.5 REMOVE "PETER" FROM THE LIST USING TWO DIFFERENT METHODS (EXTERNAL RESEARCH)
# - remove(), del

name = ["Mitch", ["sara", "sally", "joe"], "peter", "aly"]
print(f'Original List : {name}')

name.remove('peter')
print(f'1. Remove Peter : {name}')

name.pop(-2)
print(f'2.  Remove Peter : {name}')
