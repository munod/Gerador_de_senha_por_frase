import base64, re
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Frase', size=(10, 1)),
             sg.Input(key='Frase', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres'), sg.Combo(values=list(range(8, 21)), key='Total_chars', default_value= 8,
                                                           size=(8, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]

        ]
        #Declarar a janela
        self.janela = sg.Window('Gerador de Senha por Frase', layout)
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.Gera_senha(valores)
                print(f'Senha: {nova_senha}, {len(nova_senha)} digitos.')
    def Gera_senha(self, valores):
        senha_base = valores['Frase'].encode('utf-8')
        senha_nova = base64.b64encode(senha_base).decode('utf-8')
        return re.sub(r'[GW]', '1', senha_nova[-valores['Total_chars']:])

gen = PassGen()
gen.Iniciar()