#minha solução
cidade = str(input('Em que cidade você nasceu? '))
esp = cidade.strip()
mai = esp.upper()
print('SANTO' in mai)

#solução do professor
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')