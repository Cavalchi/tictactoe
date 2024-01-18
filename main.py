# Importando as bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# Definindo a classe do jogo
class TicTacToe:
    def __init__(self):
        # Inicializando a janela do jogo
        self.window = tk.Tk()
        self.window.withdraw()  # Escondendo a janela principal

        # Perguntando ao usuário se eles querem jogar contra outra pessoa ou contra a IA
        self.game_mode = simpledialog.askstring("Modo de Jogo", "Digite 'P' para jogar contra outra pessoa ou 'IA' para jogar contra a IA", parent=self.window)
        
        self.window.deiconify()  # Mostrando a janela principal
        self.window.title("Jogo da Velha")  # Definindo o título da janela

        # Inicializando o tabuleiro do jogo
        self.board = [[" "]*3 for _ in range(3)]
        self.player = "X"  # Definindo o jogador inicial

        # Inicializando os botões da interface gráfica do usuário
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text=" ", width=20, height=10, command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # Verificando se a célula está vazia
        if self.board[row][col] == " ":
            # Atualizando o tabuleiro e a interface gráfica do usuário para refletir o movimento
            self.board[row][col] = self.player
            self.buttons[row][col]['text'] = self.player
            if self.player == "X":
                self.buttons[row][col]['fg'] = "blue"
            else:
                self.buttons[row][col]['fg'] = "red"
            
            # Verificando se o jogo foi ganho
            if self.check_win():
                messagebox.showinfo("Jogo da Velha", f"O jogador {self.player} venceu!")
                self.window.quit()
            # Verificando se é um empate
            elif not any(" " in row for row in self.board):
                messagebox.showinfo("Jogo da Velha", "É um empate!")
                self.window.quit()
            else:
                # Alternando o jogador
                self.player = "O" if self.player == "X" else "X"
                # Se o modo de jogo for "IA" e for a vez do jogador "O", agendar o método `ai_move` para ser chamado após 1.1 segundos
                if self.game_mode == "IA" and self.player == "O":
                    self.window.after(1100, self.ai_move)
        else:
            # Se a célula já estiver ocupada, mostrar uma mensagem de erro
            messagebox.showinfo("Jogo da Velha", "Essa célula já está ocupada!")

    def ai_move(self):
        # Fazendo um movimento para a IA
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] == " ":
                self.make_move(row, col)
                break

    def check_win(self):
        # Verificando se o jogo foi ganho
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != " ":
                return True
        for col in range(len(self.board)):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count(check[0]) == len(check) and check[0] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return True
        return False

# Iniciando o jogo
if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
