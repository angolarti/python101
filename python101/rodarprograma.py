"""
Pergunta e calcula estatística de idade dos entrevistados

Este código é dividido em quatro partes
1ª Parte: ler arquivo json
2ª Parte: fazendo novas perguntas
3ª Parte: salvando tudo no arquivo
4ª Parte: calculando e mostrando as estatísticas
"""

import json
import statistics

import sh

from python101 import meuprograma


def carrega_dados():
    """
    Carrega as informações do arquvo JSON

    Popula a lista entrevistados com instancias da classe
    Entrevista com os valores que vem do arquivo JSON
    """

    global entrevistados

    def get_dados(obj):
        """
        Cria uma instancia nova de Entrevista.

        usa os dados vindos do json através do objecto 'obj'
        para nome, idade w ano_de_nascimento
        Retorna a instantacia Entrevista()
        """
        instance = meuprograma.Entrevista(
            nome=obj['nome'],
            idade=obj['idade'],
            ano=obj['ano']
        )
        return instance

    # Ler o arquivo JSON
    try:
        with open('dados.json', 'r') as file:
            dados = json.load(file)
            entrevistas = dados['Entrevistas']
            entrevistados = [get_dados(entrevista)
                             for entrevista in entrevistas]
    except Exception as erro:
        print('Ocorreu um erro ao carregar o arquivo')
        print('O Erro é: ', erro)


def novos_dados():
    """
    Pergunta novos nomes e anos de nascimentos.

    Enquanto o utilizador não digitar 'parar' ao perguntar o nome
    o programa pergunta o ano de nascimento e calcula a idade.
    """
    pode_parar = False

    while not pode_parar:
        entrevistado = meuprograma.Entrevista()

        if entrevistado.pergunta_nome().lower() == 'parar':
            pode_parar = True
        else:
            try:
                entrevistado.pergunta_idade()
            except ZeroDivisionError:
                print('Ocorreu um erro mais a lista foi salva')
                entrevistados.append(entrevistado)
            except Exception as erro:
                print('Ocorreu um erro mais a lista NÃO foi salva')
                print('O tipo de erro foi {}'.format(type(erro)))
                print('A mensagem foi {}'.format(erro))
            else:
                entrevistados.append(entrevistado)


def salvar_dados():
    """
    Salva as informações heradas num arquivo JSON

    Converte o dicionario Python para JSON e dalva os dados
    da lists 'entrevistados'

    Cria a lista no formato {nome=nome, ano=ano, idade=idade}
    Transaforma a lista em um discionário { "Entrevista". lista }
    """

    # Dicionário pro Compreensão
    # dicionario ) {<expressão para chave>:<expressão para valor> <loop> <expressão para lopp>}
    salvar_entrevista = [
        dict(nome=obj.nome, idade=obj.idade, ano=obj.ano_de_nascimento)
        for obj in entrevistados
    ]

    salvar_entrevistado = {"Entrevistas": salvar_entrevista}
    salvar_entrevistado = json.dumps(
        salvar_entrevistado, indent=4, sort_keys=False)
    try:
        with open('dados.json', 'w') as file:
            file.write(salvar_entrevistado)
    except Exception as erro:
        print('Ocorreu um erro salvar a lista')
        print('O tipo de erro foi {}'.format(type(erro)))
        print('A mensagem foi {}'.format(erro))


def calcular_dados():
    """
    Calcular as estatísticas de idade

    Mostrar a menor idade calculada
    Mostrar a maior idade calculada
    mostrar a média de idade dos adultos

    Mostrar a quantidade de nascimentos por década
    O que temos: [1987, 1989, 2012, 2015, 2017]
    O que queremos: {1980: 2, 2010: 3}

    Mostrar a quantidade de nascimento por década
    O que temos: [1987, 1865, 200, 2001]
    1º passo: converter anos em décadas
    2º passo: criar uma lista (set) com as décadas sem repetir
    3º passo: contar as décadas na lista original
    O que queremos: { 1980: 10, 1009: 15, 200: 5}
    1985 / 10 = 198.5 int -> 198 x 10 = 1980
    """

    # Lista por Cmpreensão
    # lista = [<epressão para valor> <loop> <expressão para loop>]
    menor_idade = min([entrevistado.idade for entrevistado in entrevistados])
    maior_idade = max([entrevistado.idade for entrevistado in entrevistados])

    media_idade_dos_adultos = statistics.median_high(
        [entrevistado.idade for entrevistado in entrevistados if entrevistado.idade >= 18])

    decadas = [int(entrevistado.ano_de_nascimento / 10)
               * 10 for entrevistado in entrevistados]
    set_decadas = set(decadas)

    # Dicionário pro Compreensão
    # dicionario ) {<expressão para chave>:<expressão para valor> <loop> <expressão para lopp>}
    entrevistados_por_decadas = {
        decada: decadas.count(decada) for decada in set_decadas}

    print('\nResultados:')
    print('--------------------------------')
    print('Quantidade de Entrevistas: {}'.format(len(entrevistados)))
    print('Menor idade: {}'.format(menor_idade))
    print('Maior idade: {}'.format(maior_idade))
    print('Ḿédia de idade dos adultos: {}'.format(media_idade_dos_adultos))
    print('\nNascimentos por Décadas')
    print('--------------------------------')
    for decada, quantidade in entrevistados_por_decadas.items():
        print('{}: {} nascimentos'.format(decada, quantidade))
    print('\n\n')

    resposta_ok = False

    while not resposta_ok:
        resposta = input('Deseja mostar os dados um arquivo? (s/n) ')
        resposta = resposta[0].lower()
        if resposta == 's' or resposta == 'n':
            resposta_ok = True

    if resposta_ok:
        sh.subl3('dados.json')


def main():
    carrega_dados()
    novos_dados()
    salvar_dados()
    calcular_dados()

