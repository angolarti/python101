import datetime
"""
Módulo que contém a classe Entrevista.

Esta classe será usada para instanciar e guardar cada entrevista
feita pelo programa mais as entrevistas guardadas em disco.

Os dados dessas instancias serão usados para fazer as estatísticas
"""


class Entrevista(object):
    """ Classe Entrevista """

    def __init__(self, nome="", idade=0, ano=0):
        """
        Entra com os valores iniciais. variáveis de sistema.

        nome = nome informado pelo entrevistado
        ano = ano informado pelo entrevistado
        idade = idade calculada pelo informadoo doentrevistado
        """
        self.nome = nome
        self.idade = idade
        self.ano_de_nascimento = ano

    def __str__(self):
        return 'Nome: {} Idade: {}'.format(self.nome, self.idade)

    def __repr__(self):
        # Use to develop time
        return 'input()={} input()=int({})'.format(self.nome, self.idade)

    def pergunta_nome(self):
        while not self.nome:
            self.nome = input('Qual é o seu nome? ')
        self.nome = self.nome.title()

        return self.nome

    def pergunta_idade(self):
        ano_currente = datetime.date.today().year
        isnumber = False

        while not isnumber:
            try:
                self.ano_de_nascimento = int(input(
                    'Ei ' + self.nome + ', em que ano vocë nasceu? '))
                isnumber = True
            except ValueError:
                continue
            else:
                if self.ano_de_nascimento >= 1900 and \
                        self.ano_de_nascimento <= ano_currente:
                    pass
                else:
                    isnumber = False
        self.idade = ano_currente - self.ano_de_nascimento

        return (self.ano_de_nascimento, self.idade)
