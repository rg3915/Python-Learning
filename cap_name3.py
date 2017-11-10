name = input('Digite seu nome: ')
p = ['da', 'de', 'di', 'do', 'du', 'para']
r = ' '.join(
    list(map(lambda w: w.capitalize() if not w in p else w, name.split())))
print(r)
