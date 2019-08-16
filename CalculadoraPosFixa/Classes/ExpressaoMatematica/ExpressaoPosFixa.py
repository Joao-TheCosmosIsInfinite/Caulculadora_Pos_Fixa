import Classes.ExpressaoMatematica.ExpressaoInfixa as ExpInf
import Classes.EstruturaDados.Pilha as imp_pilha

class ExpressaoPosFixa(ExpInf):
    def __init__(self):
        super().__init__()
        self._indice = 0
        pilha = imp_pilha.Pilha()

    def prioridade_operador(self, caracter):
        if (caracter == "+" or caracter == "-"):
            return 1
        elif (caracter == "*" or caracter == "/"):
            return 2
        elif (caracter == ">" or caracter == "<"):
            return 3
        else:
            return 0

    def alocar_caracter(self, caracter, pilha_aux = imp_pilha.Pilha(), pilha_pos= imp_pilha.Pilha()):
        prioridade_caracter = self.prioridade_operador(caracter)
        prioridade_aux = 0
        flag =0

        if pilha_aux.pilha_vazia():
            pilha_aux.empilha(caracter)
        else:
            while flag == 0 or (prioridade_caracter <= prioridade_aux and not pilha_aux.pilha_vazia()):
                caracter_aux = pilha_aux.desempilha()
                prioridade_aux = self.prioridade_operador(caracter_aux)
                pilha_pos.empilha(caracter_aux) if (prioridade_caracter <= prioridade_aux) else pilha_aux.empilha(caracter_aux)
                flag += 1
            pilha_aux.empilha(caracter)

    def rearranjar_parenteses(self, caracter, pilha_aux = imp_pilha.Pilha(), pilha_pos= imp_pilha.Pilha()):
        flag = 0
        caracter_aux = ""
        if(pilha_aux.pilha_vazia() or caracter == "("):
            pilha_aux.empilha(caracter)
        else:
            while flag == 0 or (caracter_aux != "(" and not pilha_aux.pilha_vazia()):
                caracter_aux = pilha_aux.desempilha()
                if caracter_aux != "(":
                    pilha_pos.empilha(caracter_aux)
                flag += 1

    def expressao_infixa_para_posfixa(self, pilha = imp_pilha.Pilha()):
        pilha_infx = imp_pilha.Pilha()
        pilha_aux = imp_pilha.Pilha()
        caracter = None

        pilha_infx = pilha.__copy__()
        pilha_infx.inverter_pilha()
        while not pilha_infx.pilha_vazia():
            caracter = pilha_infx.desempilha()
            if self.eh_operando(caracter):
                pilha.empilha(caracter)
            elif self.eh_parenteses(caracter):
                self.rearranjar_parenteses(caracter, pilha_aux, pilha)
            else:
                self.alocar_caracter(caracter, pilha_aux, pilha)
        while(not pilha_aux.pilha_vazia()):
            pilha.empilha(pilha_aux.desempilha())



