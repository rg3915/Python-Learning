from datetime import datetime


def age(birthday):
    '''
    Retorna a idade em anos
    '''
    today = datetime.now()

    if not birthday:
        return None

    age = today.year - birthday.year

    # Valida a data de nascimento
    if birthday.year > today.year:
        print('Data inválida!')
        return None

    # Verifica se o dia e o mês já passaram;
    # se não, tira 1 ano de 'age'.
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1

    return age

if __name__ == '__main__':
    birthday = input('Digite sua data de nascimento no formato dd/mm/yyyy: ')
    birthday = datetime.strptime(birthday, '%d/%m/%Y')
    if age(birthday):
        print(age(birthday))
