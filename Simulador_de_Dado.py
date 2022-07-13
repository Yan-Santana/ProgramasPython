# Simulador de Dado
# Simular um uso de um dado, gerando um valor de 1 até 6.
import random
import PySimpleGUI as sg

class simuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        
        # Layout
        sg.theme('DarkAmber')
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button("SIM"), sg.Button("NÂO")]
            ]
        
        
        # Vazer alguma coisa com esses valores
    def Iniciar(self):
        # Criar the window
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        
        # Ler os valores na tela 
        self.eventos, self.Valores = self.janela.Read()
        
        # Veridicar resposta:
        try:
            if self.eventos == 'SIM':
                self.GerarValorDoDado()
                
            elif self.eventos == 'NÂO':
                print("Agradeço a sua participação!")

            else:
                print("Por favor, digitar sim ou não.")
        except:
            print("Ocorreu um erro ao receber a sua resposta.")
        
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = simuladorDeDado()
simulador.Iniciar()