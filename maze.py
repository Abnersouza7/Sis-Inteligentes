
"""variaveis

ordem_matriz                            ok
matriz                                  inserida por usuario
pos_inicio                              ok
pos_fim                                 ok
pos_atual
lista [[x,y],[0]]
caminho

funcoes

bfs - fifo
dfs - lifo

find_pos_inicio                         ok
find_pos_fim                            ok

init                                    ok
funcao sucessor                         ok
teste objetivo                          ok
custo de caminho
custo de passo
"""

from logging.handlers import QueueListener
from platform import node


class Maze:
    def __init__(self, matriz):
        self.ordem = len(matriz)
        self.matriz = matriz
        self.find_pos_inicio()
        self.find_pos_fim()
        self.pos_atual = self.pos_inicio

    def find_pos_inicio(self):
        for i in range(self.ordem):  # linha
            for j in range(self.ordem):  # coluna
                if self.matriz[i][j] == 2:
                    self.pos_inicio = [i, j]  # linha,coluna
        print("Pos inicio: ", self.pos_inicio)

    def find_pos_fim(self):
        for i in range(self.ordem):
            for j in range(self.ordem):
                if self.matriz[i][j] == 3:
                    self.pos_fim = [i, j]
        print("Pos fim: ", self.pos_fim)

    def funcao_sucessor(self):
        # coord = [linha, coluna] | direita = [ , +] , esquerda = [ , i], cima = [ , -], baixo = [ , +]
        x = self.pos_atual[0]
        y = self.pos_atual[1]
        self.lista_aux = []
        if self.matriz[x, y + 1] == 1 and y != 9 or self.matriz[x, y - 1] == 1 and y != 0 or self.matriz[x + 1, y] == 1 and x != 9 or self.matriz[x - 1, y] == 1 and x != 0:
            self.lista.append([[x, y], [0]])
            self.lista_aux.append([[x, y], [0]])

    def teste_objetivo(self):
        # coord = [linha, coluna] | direita = [ , +] , esquerda = [ , i], cima = [ , -], baixo = [ , +]
        x = self.pos_atual[0]
        y = self.pos_atual[1]

        if self.matriz[x, y + 1] == 3 and y != 9 or self.matriz[x, y - 1] == 3 and y != 0 or self.matriz[x + 1, y] == 3 and x != 9 or self.matriz[x - 1, y] == 3 and x != 0:
            return 0
        return 1

    def bfs(self):
        # toda vez que der um passo, chamar funcao_sucessor E pos_atual att q ja percorreu -> lista[1] = 1 E self.caminho.append(pos_atual)
        while (self.teste_objetivo()):
            for i in self.lista:
                if i[1] == 0:
                    self.pos_atual = i[0]
                    i[1] = 1
                    self.funcao_sucessor()
                    #######
                    self.caminho.append(i[0])

        # objetivo funcao: traçar caminho
        print("bla")


if __name__ == "__main__":

    matriz = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 3, 1, 1, 1, 1, 0, 0]]

    maze = Maze(matriz)
