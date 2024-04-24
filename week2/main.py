var: str = 'String'
tmp: int = 5

if (var == 'String'):
    print('True')
else:
    print('False')

if (len(var) == 2):
    print('var is short')
elif (len(var) == 4):
    print('var is medium')
else:
    print('fml')  


if (len(var) >= 2 and len(var)<= 10):
    print('some mixed conditionals')
else:
    print('False') 

