#-*-coding:utf8;-*-
#qpy:console

from decimal import Decimal, getcontext
from datetime import datetime
import sys

CURSOR_POSITIONS = ('\\', '|', '/', '-')
CURRENT_CURSOR_POS = 0

TERMS = [(12, 18), (8, 57), (-5, 239)] 
def arctan(talj, kvot):
    
    summation = 0
    talj *= product
    qfactor = 1 
    
    while talj:
        talj //= kvot
        summation += (talj // qfactor)
        qfactor += 2
    return summation 

def _get_next_cursor_():
    global CURRENT_CURSOR_POS
    try:
        CURRENT_CURSOR_POS += 1
        return CURSOR_POSITIONS[CURRENT_CURSOR_POS]
    except:
        CURRENT_CURSOR_POS = 0
        return CURSOR_POSITIONS[CURRENT_CURSOR_POS]
        
def spinning_cursor_with_label(label_text):
    sys.stdout.write('\r[{}]\t{}'.format(_get_next_cursor_(), label_text))
    sys.stdout.flush()
   
number_of_places = int(input("Número de casas decimais: "))
getcontext().prec = number_of_places
product = 10 ** number_of_places
result = 0 

formatdate = '%H:%M:%S'

hstart = datetime.now().strftime(formatdate)
print('Hora de início: ', hstart)
print('''Aguarde enquanto é escrito as casas decimais. 
Dependendo do número de casas, esse processo pode demorar.
''')

for multiplier, denominator, in TERMS:
    denominator = Decimal(denominator)
    result += arctan(- denominator * multiplier, - (denominator ** 2))
    spinning_cursor_with_label(label_text="Aguarde, processando termo {}...".format(denominator))

result *= 4 
string = str(result) 
 
hend = datetime.now().strftime(formatdate)
print('Conluído!')

dif = (datetime.strptime(hend, formatdate) - datetime.strptime(hstart, formatdate))

print(''' 

O valor de Pi com ''' + str(number_of_places) + ''' casas decimais é: 
''', string[0:string.index("E")])

print('Tempo usado: ', dif)