import string
from Classes.EstruturaDados import Pilha as imp_pilha
class ExpressaoInf:
    """
            Representa a estutura da pilha como um todo, onde seŕa possivel armazenar
            qualquer informação, utilizando o conceito nativo dessa estrutura de dados

            Attributes: Não possui
    """
    ## Método: inicar a classe
    def __init__(self, notacao):
        ''' Constructor:    __init__
                            inicia a classe que conterá a expressão matemática/2
             Args: {notacao}
                   - é a notação matemática em si, como 1+6, 9-8-2.
        '''
        self._notacao = notacao
        self._indice = 0
        self._tamanho_formula = 0

    ## Método: get
    def _get_notacao(self):
        return self._notacao

    ## Método: set
    def _set_notacao(self, notacao):
        self._notacao = notacao

    ## Encapsulamento pythonico
    notacao = property(_get_notacao, _set_notacao)

    ## Método: identificar se um dado caracter é um parenteses
    def eh_parenteses(self, caracter):
        return True if (caracter == "(" or caracter == ")") else False

    ## Método: identificar se um dado operador é negativo
    def eh_operador_negativo(self, caracter):
        return True if (caracter == "-") else False

    ## Método: identificar se um dado operador é negativo
    def eh_operador(self, caracter):
        return True if ("+-*/" in caracter) else False

    ## Método: identificar se um dado caracter é um operando
    def eh_operando(self, caracter):
        return True if not (self.eh_parenteses(caracter) or self.eh_operador(caracter)) else False

    ## Método: descobrir qual o proximo item da formula
    def sequencia_numerica(self, seq, formula, atual):
        while(atual < self._tamanho_formula-1 and not self.eh_operador(formula[atual + 1])) and not self.eh_parenteses(formula[atual + 1]):
            seq += formula[atual + 1]
            atual+=1
        self._indice = atual
        return seq


    ## Método: empilhar a expressão matemática
    def empilhar_expressao(self):

        pilha = imp_pilha.Pilha()
        formula_desmembrada = []
        self._indice = 0
        z = 0
        #formula operador, proximo, anterior, caracter, elemento = ''
        try:
            ## s.translate({ord(c): None for c in string.whitespace})
            ##formula = self._get_notacao
            formula = self.notacao
            formula.replace(" ", "")

            ## Gerar uma list com todos os elementos da formula
            formula_desmembrada = list(formula)

            ## Percorre a lista com os itens da expressao passada, e empilha-los na pilha
            for caracter in formula_desmembrada:

                if self._indice == 0 and not self.eh_parenteses(caracter):
                    elemento = self.sequencia_numerica(caracter, formula_desmembrada, self._indice)
                    pilha.empilha(elemento)
                elif self.eh_operador(caracter):
                    elemento = caracter
                    if self.eh_operador_negativo(caracter):
                        anterior = formula_desmembrada[self._indice - 1]
                        if self.eh_operador(anterior) or self.eh_parenteses(anterior):
                            elemento = self.sequencia_numerica(caracter, formula, self._indice)
                    pilha.empilha(elemento)
                elif not self.eh_operador(caracter) and not self.eh_parenteses(caracter) and (self._indice < formula_desmembrada.__len__() - 1):
                    elemento = self.sequencia_numerica(caracter, formula_desmembrada, self._indice)
                    pilha.empilha(elemento)
                elif not self.eh_operador(caracter) and not self.eh_parenteses(caracter):
                    elemento = caracter
                    pilha.empilha(elemento)
            return pilha
        except OSError as erro:
            print("Erro ao inserir a formula infixa na pilha. Erro: {}".format(erro.strerror))
        finally:
            pass

