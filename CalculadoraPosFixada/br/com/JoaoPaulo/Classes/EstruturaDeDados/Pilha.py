class Pilha:
    """
        Representa a estutura da pilha como um todo


    """
    ## Método: Iniciar a Pilha
    def __init__(self):
        self.__items = []

    ## Método: Tamanho da Pilha
    def __len__(self):
        return len(self.__items)

    ## Método: Verificar se a pilha esta vazia
    def pilhaVazia(self):
        return len(self.__items) == 0

    ## Método: Empilhar um elemento na Pilha
    def empilha(self, item):
        self.__items.append(item)

    ## Método: Desempilhar um elemento da pilha
    def desempilha(self):
        if (self.pilhaVazia()):
            print("Pilha Vazia")
            return 0
        else:
            return self.__items.pop()

    ## Método: Exibir a pilha
    def exibirPilha(self):
        try:
            print(self.__items)
        except:
            print("Pilha vazia")

