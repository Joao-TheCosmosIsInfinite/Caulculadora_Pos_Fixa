import br.com.JoaoPaulo.Classes.EstruturaDeDados.Pilha as pilha

if __name__ == '__main__':

    minhaPilha = pilha.Pilha()
    if(minhaPilha.pilhaVazia()):
        print("Pilha vazia")

    minhaPilha.desempilha()
    minhaPilha.empilha("Macaco")
    minhaPilha.empilha("Sabonete")
    minhaPilha.empilha([1, 2, 3, 4, 5])

    print(minhaPilha.desempilha())

    minhaPilha.exibirPilha()
