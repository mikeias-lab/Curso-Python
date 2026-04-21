s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s != 'M' and s != 'F':
    s = str(input('\033[31mRESPOSTA INVÁLIDA!\033[m Digite novamente: ')).strip().upper()
print('FIM')
