import tkinter as tk
from ttkbootstrap import ttk
from resolverproblema_mat import gerarproblema

# cria um problema matematico
ex, r = gerarproblema()

def resolverproblema():
    r_user = entryInt.get()
    print(r)
    if r_user == r:
        output_string.set(f'Resposta certa! (RESULTADO: {r})')
    else:
        output_string.set(f'Resposta errada (RESULTADO: {r})')
    replay_string.set('Você quer jogar novamente?')
    replay_frame.pack()
    botao_sim_replay.pack()

# função para reiniciar o jogo
def replayproblema():
    global r
    replay_frame.pack_forget()  
    ex, r = gerarproblema()
    title_label.config(text=f'Calcule este problema: {ex}')  # atualiza o problema na tela
    entryInt.set('0')  
    output_string.set('')  
    replay_string.set('') 

# criando base
window = tk.Tk()
window.geometry("500x250")
window.title("MatProcessos")

_icon = tk.PhotoImage(file='lampada.png')
window.iconphoto(True, _icon)

title_label = ttk.Label(master= window, text= f'Calcule este problema: {ex}', font= 'Calibri 24')
title_label.pack()

# enviar a resposta e ver se está correta
input_frame = ttk.Frame(master= window)
entryInt = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entryInt)
botao = ttk.Button(master= input_frame, text= 'Ver resposta', command= resolverproblema)
entry.pack(side= 'left', padx= 15)
botao.pack(side= 'left')
input_frame.pack(pady= 15)

output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= 'Resultado: ', font= 'Calibri 24', textvariable= output_string)
output_label.pack(pady= 5)

# botoes de replay
replay_string = tk.StringVar()
replay_frame = ttk.Frame(master= window)
replay_label = ttk.Label(master= window, text= 'Quer jogar novamente?', font= 'Calibri 24', textvariable= replay_string)
botao_sim_replay = ttk.Button(master= replay_frame, text= 'Sim', command=replayproblema)
replay_frame.pack()
replay_label.pack()
botao_sim_replay.pack()
replay_frame.pack_forget()

# roda a janela
window.mainloop()