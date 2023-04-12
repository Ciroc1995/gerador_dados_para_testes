import random
import os
import time

print('Bem-vindo ao Gerador de Dados para testes')
print('---------------------------------')

nomes = ['cicero', 'sara', 'paula', 'lucas', 'gabriel']
emails = ['cicero@gmail.com', 'sara@gmail.com',
          'paula@gmail.com', 'lucas@gmail.com', 'gabriel@gmail.com']
telefones = ['33984557830', '33984589187',
             '33984667321', '33987654324', '33987563821']
cidades = ['manhuacu', 'reduto', 'sao-paulo', 'manhumirim', 'simonesia']
estados = ['MG', 'SP', 'ES', 'RJ', 'RS']


def nome_aleatorio(nomes):
    nome = random.choice(nomes)
    dados_aleatorios.append(nome)
    print(nome)


def email_aleatorio(emails):
    email = random.choice(emails)
    dados_aleatorios.append(email)
    print(email)


def telefone_aleatorio(telefones):
    telefone = random.choice(telefones)
    dados_aleatorios.append(telefone)
    print(telefone)


def cidade_aleatoria(cidades):
    cidade = random.choice(cidades)
    dados_aleatorios.append(cidade)
    print(cidade)


def estado_aleatorio(estados):
    estado = random.choice(estados)
    dados_aleatorios.append(estado)
    print(estado)


while True:
    print('Opções de dados a serem gerados')
    print('[1] - Nome')
    print('[2] - Email')
    print('[3] - Telefone')
    print('[4] - Cidade')
    print('[5] - Estado')

    dados_aleatorios = ['']
    opcoes = input('Qual ou quais dados deseja gerar? ')

    for opcao in opcoes:
        if opcao == '1':
            nome_aleatorio(nomes)
        elif opcao == '2':
            email_aleatorio(emails)
        elif opcao == '3':
            telefone_aleatorio(telefones)
        elif opcao == '4':
            cidade_aleatoria(cidades)
        elif opcao == '5':
            estado_aleatorio(estados)

    salvar = input('Deseja salvar os dados em um arquivo txt, (s/n)? ')
    if salvar == 's':
        print('Criando arquivo para salvar os dados')
        time.sleep(1)
        print('Arquivo criado e dados salvos com sucesso')

        with open('dados.txt', 'w', newline='') as arquivo:
            for dado in dados_aleatorios:
                arquivo.write(dado + os.linesep)
    elif salvar == 'n':
        parar_ou_continuar = input(
            'Deseja continuar rodando o programa e salvar mais arquivos ou parar? (c/p)')
        if parar_ou_continuar == 'c':
            continue
        else:
            break
