#Iniciando minha classe Agendamento com variáveis não definidas,pois não tenho valores pré-definidos para elas.

class agendamento:
  dia = None
  mes = None
  ano = None
  hora = None
  duracao = None
  descricao = None


#Este código define uma função chamada validardata que recebe três argumentos:dia, mes e ano.A função verifica se a data é válida ou não, retornando -1 se a data for inválida.

def validardata(dia,mes,ano):
  if dia < 1 or  dia > 31:
    print("\tDia invalida") #\t = tabulação
    return -1
  if mes < 1 or mes > 12 :
    print("\tMes invalida")
    return -1
  if ano < 2023:
    print("\tAno invalida")
  if dia > 31 or mes > 12 or ano < 2023:

    return -1




listaAgendamento = [] # inicializa uma lista vazia para amazenar os agendamentos


def incluir(): # Esse código implementa uma função chamada incluir() que permite ao usuário fazer um novo agendamento.
  print('~~~~~~~~~Você pode fazer seu agendamento~~~~~~~~')
  print('='*50)
  print()

  while True:
    incluirAgenda = agendamento()
    incluirAgenda.dia = int(input('Digite o dia: '))
    incluirAgenda.mes = int(input('Digite o mes: '))
    incluirAgenda.ano = int(input('Digite o ano: '))
    while validardata(incluirAgenda.dia,incluirAgenda.mes,incluirAgenda.ano) == -1:
      print('   Digite a data de novo!   ')
      incluirAgenda.dia = int(input('Digite o dia: '))
      incluirAgenda.mes = int(input('Digite o mes: '))
      incluirAgenda.ano = int(input('Digite o ano: '))
    incluirAgenda.hora = float(input('Digite a hora: '))
    incluirAgenda.duracao = float(input('Digite a duração: '))
    if incluirAgenda.hora < 0 or incluirAgenda.hora > 23:
      print('Hora inválida. Digite um valor entre 0 e 23.')
      continue
    if incluirAgenda.duracao < 1 or incluirAgenda.duracao > 60:
      print('Duração inválida. Digite um valor entre 1 e 60.')
      continue
    incluirAgenda.descricao = str(input('Digite a descrição: '))
    achou = False
    for agen in listaAgendamento:
       if incluirAgenda.dia == agen.dia and  incluirAgenda.mes == agen.mes and incluirAgenda.ano == agen.ano and incluirAgenda.hora == agen.hora:
          achou = True
          print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
          print("    Não há vaga para esse horário!!!!     ")
          print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
       else:
          achou = False
    if achou == False:
      listaAgendamento.append(incluirAgenda)
    quest = False
    while True:
      print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
      question =input('Você quer continuar? yes/No : ')
      print()
      question = question.lower()
      if question == "yes":
        quest = True
      if question != "yes" and question != "no":
         print('Erro, digite tua resposta novamente')
         continue
         quest = True
      else:
        quest = False
      break
    if quest == False:
      break



# O segundo código que contém uma função chamada consultar() que serve para consultar os agendamentos previamente cadastrados em uma lista listaAgendamento.
def consultar():
  if not listaAgendamento:
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('   --> Ainda Não existe agendamento para fazer sua consultação <--     ')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
  else:
    print('='*100)
    print("      Como que deseja fazer a sua consulta? se for pela DATA, digite 1. \nSe for pela DATA e HORA digite 2.        ")
    print('================================================================================================================')
    opcao = int(input("Opcao:\n"))
    if opcao == 1:
      dia1 = int(input('Digite o dia: '))
      mes1 = int(input('Digite o mes: '))
      ano1 = int(input('Digite o ano: '))
      achou = False
      for agen in listaAgendamento:
        if dia1 == agen.dia and mes1 == agen.mes and ano1 == agen.ano:
          achou = True
          data_em_texto = '{}/{}/{}'.format(agen.dia, agen.mes,agen.ano)
          print("Data: ",data_em_texto)
          print('Hora: ',agen.hora )
          print('Duração: ',agen.duracao)
          print('Descrição: ',agen.descricao )
      if achou == False:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print("   Nenhum agendamento encontrado para essa data!!!    ")
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    elif opcao == 2:
      dia1 = int(input('Digite o dia: '))
      mes1 = int(input('Digite o mes: '))
      ano1 = int(input('Digite o ano: '))
      hora1 = float(input('Digite a hora: '))
      achou = False
      for agen in listaAgendamento:
        if dia1 == agen.dia and mes1 == agen.mes and ano1 == agen.ano and hora1 == agen.hora:
          achou = True
          data_em_texto = '{}/{}/{}'.format(agen.dia, agen.mes,agen.ano)
          print("DATA: ",data_em_texto)
          print('Hora: ',agen.hora )
          print('Duração: ',agen.duracao)
          print('Descrição: ',agen.descricao )
          print("================================================")
        else:
          achou == False
      if achou == False:
        print("Não existe agendamento para essa data!!!")
    else:
      print("Opção invalida!")


# A função alterar() tem como objetivo permitir que o usuário altere informações de um compromisso previamente cadastrado na lista listaAgendamento.

def alterar():
  if not listaAgendamento:
    print('====================================')
    print('   Lista de agendamento Vazio!    ')
    print('======================================')

  else:
    dia1 = int(input('Digite o dia: '))
    mes1 = int(input('Digite o mes: '))
    ano1 = int(input('Digite o ano: '))
    hora1 = float(input("Digite a hora: "))
    for agen in listaAgendamento:
      if dia1 == agen.dia and mes1 == agen.mes and ano1 == agen.ano and agen.hora != hora1:
        agen.descricao = str(input('Digite a descrição: '))
        agen.duracao = float(input('Digite a duração: '))
        agen.hora = int(input('Hora'))
      else:
        print("Compromiso não encontrado!!")


#A função excluir tem como objetivo remover um agendamento da lista de agendamentos existente.
def excluir():
  if not listaAgendamento:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('----> Nenhum agendamento encontrado, exclusão impossível!!! <---- ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  else:
      dia1 = int(input('Digite o dia: '))
      mes1 = int(input('Digite o mes: '))
      ano1 = int(input('Digite o ano: '))
      hora1 = float(input("Digite a hora: "))
      achou = False
      for agen in listaAgendamento:
        if dia1 == agen.dia and mes1 == agen.mes and ano1 == agen.ano and agen.hora == hora1:
           achou = True
           listaAgendamento.remove(agen)
           print("Agendamento excluido com sucesso!!!")
           return
        else:
          achou = False
      if achou == False:
        print("Agendamento não encontrado!")



# A função printAgenda() é responsável por imprimir todos os agendamentos existentes na lista de listaAgendamento.

def printAgenda():
  if not listaAgendamento:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('    Lista de agendamento Vazio!     ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  else:
    print('============Todos os agendamentos!================ ')
    for agen in listaAgendamento:
      data_em_texto = '{}/{}/{}'.format(agen.dia, agen.mes,agen.ano)
      print("Data: ",data_em_texto)
      print('Hora: ',agen.hora )
      print('Duração: ',agen.duracao)
      print('Descrição: ',agen.descricao )
      print('================================================')


#Essa função é responsável por exibir um menu com as opções disponíveis para o usuário escolher. As opções são:

def menu():
  print('==============================================')
  print('    ***SEJA BEM VINDO AO NOSSO SISTEMA***    ')
  print('==============================================')
  print('Escolher uma opção por favor:')
  print()
  print('\t1- Incluir um Agendamento ')
  print()
  print('\t2- Consultar um Agendamento ')
  print()
  print('\t3- Alterar um Agendamento ')
  print()
  print('\t4- Excluir um Agendamento')
  print()
  print('\t5- Listar Todos os Agendamentos ')
  print()
  print('\t6- Saindo do sistema até logo ')




# Programma principal
    #Esse trecho de código é responsável pelo loop principal do programa.
    # Ele exibe o menu com as opções disponíveis para o usuário e, em seguida, lê a entrada do usuário e executa a função correspondente à opção escolhida.
while True:
    menu()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    opcao = 0

    #use try Except to prevent error
    try:
     opcao = int(input('  Digite uma opção: '))
    except:
     opcao = 0
    if opcao == 1:
       incluir()
       print()
    elif opcao == 2:
       consultar()
       print()
    elif opcao == 3:
       alterar()
       print()
    elif opcao == 4:
       excluir()
       print()
    elif opcao == 5:
       printAgenda()
       print()
    elif opcao == 6:
       print()
       print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
       print('   Saindo do sistema! Até logo!  ')
       print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
       break

    else:
      print('::::::::::::::::::::::::::::::::::::::::::::::::::')
      print('   ERROR! Digite uma opção válido por favor!    ')
      print(':::::::::::::::::::::::::::::::::::::::::::::::::::')
      print()
