from customtkinter import *
class Janela:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry("220x300")
        self.janela.config(bg='white')
        self.janela.title("Calculadora IMC")
        self.janela.resizable(False,False)
        self.home()
        self.imc = None
        
        
    def home(self):
        self.texto_altura = 'Sua altura em cm*'
        self.texto_peso = 'Seu peso*'
        
        
        self.frame = CTkFrame(self.janela, fg_color='#070743',width=220, height=220)
        self.frame.grid(row=0, column=0)
        
        self.frame_baixo = CTkFrame(self.janela, fg_color='#070743',width=220, height=80)
        self.frame_baixo.grid(row=1, column=0)
        
        self.titulo = CTkLabel(self.frame,width=220,height=30,fg_color='#d0e0eb', text_color='#12122b',text='calcular imc', font=('Arial',20))
        self.titulo.place( x=1,y=0)
        
        self.nome_altura = CTkLabel(self.frame, text='Altura', font=('Arial',13))
        self.nome_altura.place(x=54, y=47)

        self.pegar_altura = CTkEntry(self.frame, width=120, placeholder_text=self.texto_altura,border_color='#d0e0eb')
        self.pegar_altura.place(x=50, y=70)
        
        self.nome_peso = CTkLabel(self.frame, text='Peso', font=('Arial',13))
        self.nome_peso.place(x=54, y=117)
        
        self.pegar_peso = CTkEntry(self.frame, width=120,border_color='#d0e0eb', placeholder_text=self.texto_peso)
        self.pegar_peso.place(x=50, y=140)
        
        self.botao_calcular = CTkButton(self.frame, text_color='#12122b',fg_color='#88abc2', text='Calcular', width=30, height=25, command=self.mostrarEstadoImc)
        self.botao_calcular.place(x=50, y=190)
        
        self.botao_limpar = CTkButton(self.frame,text_color='#12122b',fg_color='#88abc2',text='Limpar', width=30, height=25, command=self.limpar_texto)
        self.botao_limpar.place(x=120, y=190)
        
    def mostrarEstadoImc(self):
        lista_peso = ['','abaixo do peso',"peso normal","sobrepeso","obesidade grau I","obesidade grau II","obesidade grau III"] 
        self.classificarImc()
        try:
            self.most_imc = CTkLabel(self.frame_baixo, text=lista_peso[self.estadoImc],width=220, height=80, font=('Arial',20))
            self.most_imc.place(x=2,y=5)
        except:
            pass 
    def calcularImc(self):
        try:
            self.alturab = self.pegar_altura.get()
            self.pesob = self.pegar_peso.get()
            self.peso = float(self.pesob)
            self.altura = float(self.alturab)
            self.imc = self.peso / (self.altura ** 2)
            return self.imc
        except:
            pass
        
    def classificarImc(self):
        self.estadoImc = None
        self.calcularImc()
        try:
            if self.imc < 18.5:
                self.estadoImc = 1
                return self.estadoImc
            elif 18.5 <= self.imc < 24.9:
                self.estadoImc = 2
                return self.estadoImc
            elif 25 <= self.imc < 29.9:
                self.estadoImc = 3
                return self.estadoImc
            elif 30 <= self.imc < 34.9:
                self.estadoImc = 4
                return self.estadoImc
            elif 35 <= self.imc < 39.9:
                self.estadoImc = 5
                return self.estadoImc
            else:
                self.estadoImc = 6
                return self.estadoImc
        except:
            self.most_imc = CTkLabel(self.frame_baixo, text='Você não digitou nada!',width=220, height=80)
            self.most_imc.place(x=3,y=5)
            
        
    def limpar_texto(self):
        self.pegar_peso = CTkEntry(self.frame, width=120,border_color='#d0e0eb', placeholder_text=self.texto_peso)
        self.pegar_peso.place(x=50, y=140)
        
        self.most_imc = CTkLabel(self.frame_baixo, text='',width=220, height=80)
        self.most_imc.place(x=3,y=5)
        
        self.pegar_altura = CTkEntry(self.frame, width=120, placeholder_text=self.texto_altura,border_color='#d0e0eb')
        self.pegar_altura.place(x=50, y=70)
        
if __name__ == '__main__':
    app = CTk()
    calc = Janela(app)
    app.mainloop()

    
