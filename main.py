from customtkinter import *
class Janela:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("220x300")
        self.janela.config(bg='white')
        self.janela.title("Calculadora IMC")
        self.janela.resizable(False,False)
        self.home()
        
    def home(self):
        texto_altura = 'Sua altura em cm*'
        texto_peso = 'Seu peso*'
        
        def limpar_texto():
            self.pegar_peso = CTkEntry(self.frame, width=120,border_color='#d0e0eb', placeholder_text=texto_peso)
            self.pegar_peso.place(x=50, y=140)
            
            self.pegar_altura = CTkEntry(self.frame, width=120, placeholder_text=texto_altura,border_color='#d0e0eb')
            self.pegar_altura.place(x=50, y=70)
        
        self.frame = CTkFrame(self.janela, fg_color='#070743',width=220, height=220)
        self.frame.grid(row=0, column=0)
        
        self.frame_baixo = CTkFrame(self.janela, fg_color='#070743',width=220, height=80)
        self.frame_baixo.grid(row=1, column=0)
        
        self.titulo = CTkLabel(self.frame,width=220,height=30,fg_color='#d0e0eb', text_color='#12122b',text='calcular imc', font=('Arial',20))
        self.titulo.place( x=1,y=0)
        
        self.nome_altura = CTkLabel(self.frame, text='Altura', font=('Arial',13))
        self.nome_altura.place(x=54, y=47)

        self.pegar_altura = CTkEntry(self.frame, width=120, placeholder_text=texto_altura,border_color='#d0e0eb')
        self.pegar_altura.place(x=50, y=70)
        
        self.nome_peso = CTkLabel(self.frame, text='Peso', font=('Arial',13))
        self.nome_peso.place(x=54, y=117)
        
        self.pegar_peso = CTkEntry(self.frame, width=120,border_color='#d0e0eb', placeholder_text=texto_peso)
        self.pegar_peso.place(x=50, y=140)
        
        self.botao_calcular = CTkButton(self.frame, text_color='#12122b',fg_color='#88abc2', text='Calcular', width=30, height=25)
        self.botao_calcular.place(x=50, y=190)
        
        self.botao_limpar = CTkButton(self.frame,text_color='#12122b',fg_color='#88abc2',text='Limpar', width=30, height=25, command=limpar_texto)
        self.botao_limpar.place(x=120, y=190)
        
if __name__ == '__main__':
    app = CTk()
    calc = Janela(app)
    app.mainloop()

    
