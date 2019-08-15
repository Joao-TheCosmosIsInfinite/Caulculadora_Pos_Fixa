class Pilha:
    """
        Representa a estutura da pilha como um todo, onde seŕa possivel armazenar
        qualquer informação, utilizando o conceito nativo dessa estrutura de dados

        Attributes: Não possui
    """

    ## Método: Iniciar a Pilha
    def __init__(self):
        ''' Constructor:    __init__
                            Iniciar a pilha
            Args: Nenhum
        '''
        self.__items = []

    ## Método: Tamanho da Pilha
    def __len__(self):
        ''' Constructor:    __len__
                            Tamanho da pilha, quantidade de elementos na pilha
            Args: Nenhum

            Return: {a}
                    - a = retorna a quantidade de items na pilha
        '''
        return len(self.__items)

    ## Método: Limpar Pilha
    def limpar_pilha(self):
        ''' Constructor:    limpar_pilha
                            limpar/ zerar a pilha
            Args: Nenhum

            Return: Nenhum
        '''
        self.__items.clear()

    ## Método: Verificar se a pilha esta vazia
    def pilha_vazia(self):
        ''' Constructor:    pilha_vazia
                            - Informa se a pilha esta vazia
            Args: Nenhum

            Return: {a}
                    - a = retorna se a pilha possui itens(0) ou não possui(1)
        '''
        return len(self.__items) == 0

    ## Método: Empilhar um elemento na Pilha
    def empilha(self, item):
        ''' Constructor:    empilha
                            - Insere um elemento na proxima posição da pilha
            Args:   {item}
                    - O item/ objeto que sera inserido na pilha

            Return: Nenhum
        '''
        self.__items.append(item)

    ## Método: Desempilhar um elemento da pilha
    def desempilha(self):
        ''' Constructor:    desempilha
                            - remove e retorna o ultimo elemento da pilha
            Args:  Nenhum

            Return: {a},{b}
                    - a = flag que indica que foi possivel remover um elemento
                    - b = o elemento removido em si
        '''
        return 1, self.__items.pop() if self.pilha_vazia() > 0 else 0, "Pilha Vazia"

    ## Método: Exibir a pilha
    def exibir_pilha(self):
        ''' Constructor:    exibir_pilha
                            - Exibi a pilha e todos os seus elementos
             Args:  Nenhum

             Return: {a},{b}
                     - a = flag que indica que há um ou n elementos na pilha
                     - b = a pilha propriamente dita
        '''
        print(self.__items if not self.pilha_vazia() else "Pilha Vazia")

    ## Método: Topo da Pilha, o ultimo elemento
    def topo_pilha(self):
        ''' Constructor:    exibir_pilha
                                    - Exibi a pilha e todos os seus elementos
            Args:  Nenhum

            Return: {a},{b}
                    - a = flag que indica que há um ou n elementos na pilha
                    - b = a pilha propriamente dita
         '''
        return 1, self.__items[-1] if self.pilha_vazia() > 0 else 0, "Pilha Vazia"


