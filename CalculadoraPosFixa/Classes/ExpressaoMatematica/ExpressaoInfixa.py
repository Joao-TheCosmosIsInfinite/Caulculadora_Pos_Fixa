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
    