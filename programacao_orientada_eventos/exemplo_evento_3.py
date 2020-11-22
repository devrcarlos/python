from tkinter import Tk, Text, BOTH

def tecla_pressionada(event):
    print('Tecla: {}'.format(event.keysym))

def botao_esquerdo_mouse(event):
    print('Botão esquerdo do mouse clicado!')

def botao_direito_mouse(event):
    print('Botão direito do mouse clicado!')

root = Tk()
text = Text(root, width=20, height=5)
text.bind('<KeyPress>', tecla_pressionada)
text.bind('<Button-1>', botao_esquerdo_mouse)
text.bind('<Button-2>', botao_direito_mouse)
text.pack(expand=True, fill=BOTH)

root.mainloop()
