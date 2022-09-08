
"""foi desenvolvido no trabalho a matriz de teste para o labirinto,
a leitura de posicao atual, uma funcao de teste de objetivo e implementado o algoritmo de DFS"""

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




from collections import defaultdict
from logging.handlers import QueueListener
from platform import node
from re import S
class Maze:
    def __init__(self, matriz):
        self.ordem = len(matriz)
        self.matriz = matriz
        self.find_pos_inicio()
        self.find_pos_fim()
        self.caminho = []

        print("DFS: ")
        self.dfs(self.pos_inicio)
        #for k in self.caminho:
        #    print(k)
        # self.bfs(self.pos_inicio)

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

    def teste_objetivo(self, next):
        y = next[0]
        x = next[1]

        if x < self.ordem - 1:
            if self.matriz[y][x + 1] == 3:
                next = [y, x + 1]
                return 1

        if x >= 0:
            if self.matriz[y][x - 1] == 3:
                next = [y, x - 1]
                return 1

        if y < self.ordem - 1:
            if self.matriz[y + 1][x] == 3:
                next = [y + 1, x]
                return 1

        if y >= 0:
            if self.matriz[y - 1][x] == 3:
                next = [y - 1, x]
                return 1

        return 0

    def dfs(self, next):
        # toda vez que der um passo, chamar funcao_sucessor E pos_atual att q ja percorreu -> lista[1] = 1 E self.caminho.append(pos_atual)

        if (next not in self.caminho):
            print(next)
            self.caminho.append(next)
            if (self.teste_objetivo(next)):
                print("FIM", self.pos_fim)
                self.caminho.append(self.pos_fim)
                return 1

            y = next[0]
            x = next[1]

            if x >= 0: # esquerda
                if self.matriz[y][x - 1] == 1:
                    next = [y, x - 1]
                    self.dfs(next)

            if y < self.ordem - 1: # baixo
                if self.matriz[y + 1][x] == 1:
                    next = [y + 1, x]
                    self.dfs(next)
            
            if x < self.ordem - 1: # direita
                if self.matriz[y][x + 1] == 1:
                    next = [y, x + 1]
                    self.dfs(next)

            if y >= 0: # cima
                if self.matriz[y - 1][x] == 1:
                    next = [y - 1, x]
                    self.dfs(next)

    def bfs(self, s):
        self.visited = [False] * (max(self.matriz) + 1)

        self.queue = []

        self.queue.append(s)
        self.visited[s] = True

        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")
            for i in self.matriz[s]:
                if self.visited[i] == False:
                    self.queue.append(i)
                    self.visited[i] = True


if __name__ == "__main__":
    # aaaaaaaa#0 #1 #2 #3 #4 #5 #6 #7 #8 #9
    matriz = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # 3
              [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # 4
              [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # 5
              [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],  # 6
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 7
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 8
              [0, 0, 1, 3, 1, 1, 1, 1, 0, 0]]  # 9
    for i in matriz:
        print(i)

    maze = Maze(matriz)
