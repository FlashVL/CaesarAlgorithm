print('Введите строку для шифрования')
strForСipher = input()
print('Введите сдвиг')
shift = int(input()) 
strСipher = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'

Сipher = strСipher.split(' ')

s = 'зашифрованная строка: '
for k in strForСipher:





    res = [y for y in Сipher if k.upper() in y]
 
    if len(res) != 0:
        m = Сipher[(Сipher.index(k.upper()) + shift)%33] 

        if k.isupper(): 
            s = s + m 
        else:
            s = s + m.lower()  
    else:
        s = s + k     
print(s)