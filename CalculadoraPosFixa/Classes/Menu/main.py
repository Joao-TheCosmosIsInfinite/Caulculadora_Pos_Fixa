import Classes.EstruturaDados.Pilha as p
import Classes.ExpressaoMatematica.ExpressaoInfixa as exp
def main():
    pass
    print("Main Acionado")
    pilha_1 = p.Pilha()
    formula = "1+1*9+-7"
    expressao = exp.ExpressaoInf(formula)

    pilha_1.empilha("Macaco")
    pilha_1.empilha("Laranja")
    pilha_1.empilha("Gol")
    pilha_1.empilha("Processador")
    pilha_1.exibir_pilha()

    pilha_1.limpar_pilha()

    pilha_1 = expressao.empilhar_expressao()

    pilha_1.exibir_pilha()
if __name__ =="__main__":
    main()