# -*- coding: utf-8 -*-

import tkinter as tk

class Tabuleiro:
    
    def __init__(self):

        self.window = tk.Tk()               
        self.window.title("Jogo da Velha")
        self.window.geometry("470x470")
        self.botão_main = tk.Button(self.window,height =8, width =20,text="Iniciar Jogo",command = self.limpar_tela)
        self.botão_main.grid(padx = 160,pady=150)   
        self.Matriz_Jogo = [[0,0,0],[0,0,0],[0,0,0]]
        self.Game_var = 0
        self.loop()
        
    def limpar_tela(self):
        self.Game_var += 1
        if self.Game_var == 1:
            self.botão_main.grid_forget()
            self.desenhar_tabuleiro()
            
        elif self.Game_var >= 1:        
            self.b_1.grid_forget()
            self.b_2.grid_forget()
            self.b_3.grid_forget()
            self.b_4.grid_forget()
            self.b_5.grid_forget()
            self.b_6.grid_forget()
            self.b_7.grid_forget()
            self.b_8.grid_forget()
            self.b_9.grid_forget()
            self.Prox_Jogada.grid_forget()   
            self.desenhar_tabuleiro()
        
    def desenhar_tabuleiro(self):
        self.b_1 = tk.Button(self.window,height =8, width =20)
        self.b_1.configure(command=self.postar(1))
        self.b_1.grid(row=0, column=0,pady=5)

        self.b_2 = tk.Button(self.window,height =8, width =20)
        self.b_2.configure(command=self.postar)
        self.b_2.grid(row=1, column=0,padx=5)
        
        self.b_3 = tk.Button(self.window,height =8, width =20)
        self.b_3.configure(command=self.postar)
        self.b_3.grid(row=2, column=0)
      
        self.b_4 = tk.Button(self.window,height =8, width =20)
        self.b_4.configure(command=self.postar)
        self.b_4.grid(row=0, column=1)

        self.b_5 = tk.Button(self.window,height =8, width =20)
        self.b_5.configure(command=self.postar)
        self.b_5.grid(row=1, column=1)
        
        self.b_6 = tk.Button(self.window,height =8, width =20)
        self.b_6.configure(command=self.postar)
        self.b_6.grid(row=2, column=1)
        
        self.b_7 = tk.Button(self.window,height =8, width =20)
        self.b_7.configure(command=self.postar)
        self.b_7.grid(row=0, column=2)

        self.b_8 = tk.Button(self.window,height =8, width =20)
        self.b_8.configure(command=self.postar)
        self.b_8.grid(row=1, column=2,padx=5)
        
        self.b_9 = tk.Button(self.window,height =8, width =20)
        self.b_9.configure(command=self.postar)
        self.b_9.grid(row=2, column=2,pady=5)
        
        self.Prox_Jogada = tk.Label(self.window, text="Próxima jogada: X", font=('Helvetica', 12))
        self.Prox_Jogada.grid(row=3, column=0, columnspan=1, sticky="nsew",pady=10) 
        
    def loop(self):
        self.window.mainloop()
    
    def postar(self, position):
        if position == 1:
            self.b_1.configure(text="X")
        if position == 2:
            self.b_2.configure(text="0")           
        if position == 3:
            self.b_3.configure(text="0")           
        if position == 4:
            self.botão8.configure(text="0")           
        if position == 5:
            self.botão8.configure(text="0")           
        if position == 6:
            self.botão8.configure(text="0")           
        if position == 7:
            self.botão8.configure(text="0")           
        if position == 8:
            self.botão8.configure(text="0")           
        if position == 9:
            self.botão8.configure(text="0")               
main = Tabuleiro()
main.loop()
