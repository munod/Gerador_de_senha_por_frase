import base64, re
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg.theme('Black')
        tab1_window = [
            [sg.T(text='Frase', size=(4, 1)), sg.In(key='Frase', size=(34, 1))],
            [sg.Text('Quantidade de Caracteres', size=(29, 1)),
             sg.Combo(values=list(range(8, 21)), key='Total_chars', default_value=8,
                      size=(3, 1))],
            [sg.Output(size=(38, 5))],
            [sg.Button('Gerar Senha')]
        ]
        tab2_window = [
            [sg.T(text=u'Digite a frase que deseja transformar em senha.\n'
                       u'A idéia é que memorizar uma frase é melhor\nque '
                       u'uma senha complexa.\nO programa não armazena sua'
                       u' senha.\n\nAutor: Thiago Santos\nVersão: 1.1')]
        ]
        layout = [[sg.TabGroup([[sg.Tab('Principal', tab1_window), sg.Tab('Ajuda', tab2_window)]])],
              ]
        '''
        layout = [
            [sg.Text('Digite a frase que deseja transformar em senha.', size=(35, 1))],
            [sg.Text('Frase', size=(4, 1)),
             sg.Input(key='Frase', size=(33, 1))],
            [sg.Text('Quantidade de Caracteres'), sg.Combo(values=list(range(8, 21)), key='Total_chars', default_value= 8,
                                                           size=(14, 1))],
            [sg.Output(size=(37, 5))],
            [sg.Button('Gerar Senha')]

        ]
        '''
        #Declarar a janela
        self.janela = sg.Window('Gerador de Senha', layout)

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