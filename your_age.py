from datetime import datetime

y = 0

while(y < 3):

    hoje = datetime.today()

    diaatual, mesatual, anoatual = hoje.strftime("%d-%m-%Y").split()

    print ("Digita sua data de nascimento = (dia mes ano)")
    print ("Data de Nascimento:")

    dia, mes, ano = input().split()

    print("Data de nascimento: {0}/{1}/{2}".format(dia,mes,ano))

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    diaatual = int(diaatual)
    mesatual = int(mesatual)
    anoatual = int(anoatual)
       
    idade = anoatual - ano
       
    if mes > 12:
        print("Mes inexistente", mes)
        y = y = 2
        
    elif dia > 31:
        print("Dia inexistente", dia)
        y = y = 2
    
    elif ano > anoatual:
        print ("Você veio do futuro?")
        y = y = 2
        
    elif mesatual > mes:
        idade = idade
        y = y = 5

    elif mes == mesatual and diaatual >= dia:
        y = y = 5
    else:
        idade = idade - 1
    
print ("Idade:", idade)