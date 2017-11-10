name = input('Digite seu nome: ')

p = ['da', 'de', 'di', 'do', 'du', 'para']

items = []

for item in name.split():
    if not item in p:
        item = item.capitalize()
    items.append(item)

full_name = ' '.join(items)
print(full_name)
