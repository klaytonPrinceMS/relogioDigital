'''

Analista de sistemas : PRINCE, K.B
Versão: 1.020230905

Relogio digital
Deve falar hora, e ter 2 despertador programavel em hora e minuto

'''

import tkinter as tk
import pyttsx3
import datetime as dt
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.utf8')

larguraBox = 600
alturaBox = 50
falante = pyttsx3.init()
janela = tk.Tk()
#janela.iconbitmap('ico.png')
janela.title("DTI - Monte Santo")
janela.geometry("{}x{}".format(larguraBox,alturaBox))
fonte = "Arial"
tamanhoTexto = 30
padingx = 2
padingy = 2
segundoSaida = "01"



#horaAlarme1 = input("Qual a hora do Alarme1: ")
horaAlarme1 = ''
if horaAlarme1 == "":
    horaAlarme1 = "11"
    minutoAlarme1 = "55"
    tituloAlarme1 = "Almoço"
else:
    minutoAlarme1 = input("Qual o minuto do alarme: ")
    tituloAlarme1 = input("Qual o titulo do alarme: ")
#horaAlarme2 = input("Qual a hora do alarme2: ")
horaAlarme2 =''
if horaAlarme2 == "":
    horaAlarme2 = "16"
    minutoAlarme2 = "50"
    tituloAlarme2 = "Saída"
else:
    minutoAlarme2 = input("Qual o minuto do alarme: ")
    tituloAlarme2 = input("Qual o titulo do alarme: ")
# Função para falar o horário
def falar_horario(hora, minuto, segundo):
    falante.setProperty('rate', 180)
    falante.setProperty('volume',1)
    if minuto == "00" and segundo == "01":
        falante.say("{} Horas".format(hora))
    elif hora == horaAlarme1 and minuto == minutoAlarme1 and segundo == segundoSaida:
        falante.say("Atenção {}     {} horas e {} minutos".format(tituloAlarme1, hora, minuto))
    elif hora == horaAlarme2 and minuto == minutoAlarme2 and segundo == segundoSaida:
        falante.say("Atenção {}     {} horas e {} minutos".format(tituloAlarme2, hora, minuto))
    falante.runAndWait()
# Função para atualizar o relógio
def atualizar_relogio():
    data = dt.datetime.now()
    dia = data.strftime('%d')
    mes = data.strftime('%B')
    ano = data.strftime('%y')
    hora = data.strftime('%H')
    minuto = data.strftime('%M')
    segundo = data.strftime('%S')
    textoRelogio = "{}:{}:{}    {} de {} de {}".format(hora, minuto, segundo, dia, mes, ano)
    label_hora.config(text=textoRelogio,font="{} {}".format(fonte,tamanhoTexto), wraplength=larguraBox, padx=padingx, pady=padingy)
    falar_horario(hora, minuto, segundo)
    janela.after(1000, atualizar_relogio)

# Label para exibir a hora
label_hora = tk.Label(janela, font=("{}".format(fonte), tamanhoTexto), fg="black")
label_hora.pack(padx=10, pady=10)
# Chamada inicial da função de atualização do relógio
atualizar_relogio()
# Loop principal da interface gráfica
janela.mainloop()
















