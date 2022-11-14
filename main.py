from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Tabela de cores
co0 = "#444466"     # Preto
co1 = "#feffff"     # Branco
co2 = "#6f9fbd"     # Azul
co3 = "#38576b"     # Valor
co4 = "#403d3d"     # Letra
co5 = "#ef5350"     # Vermelho

# Criando a janela
janela = Tk()
janela.title("HB - Pokedéx")
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# Frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# Nome
pokemon_nome = Label(frame_pokemon, text="Pikachu", relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pokemon_nome.place(x=12, y=15)

# Categoria
pk_tipo = Label(frame_pokemon, text="Elétrico", relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pk_tipo.place(x=12, y=50)

# ID
pk_id = Label(frame_pokemon, text="#025", relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pk_id.place(x=12, y=75)

# Imagem do Pokemon
pokemon_imagem = Image.open('images/pikachu.png')
pokemon_imagem = pokemon_imagem.resize((238, 238))
pokemon_imagem = ImageTk.PhotoImage(pokemon_imagem)
pk_imagem = Label(frame_pokemon, image=pokemon_imagem, relief='flat', bg=co1, fg=co0)
pk_imagem.place(x=60, y=50)

pk_tipo.lift()

# Status
pk_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pk_status.place(x=15, y=310)

# HP
pk_hp = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_hp.place(x=15, y=360)

# Ataque
pk_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_ataque.place(x=15, y=385)

# Defesa
pk_defesa = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_defesa.place(x=15, y=410)

# Velocidade
pk_velocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_velocidade.place(x=15, y=435)

# Total
pk_total = Label(janela, text='Total: 1700', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_total.place(x=15, y=460)

# Habilidades
pk_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pk_habilidades.place(x=180, y=310)

pk_habilidades_1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_habilidades_1.place(x=180, y=360)

pk_habilidades_2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pk_habilidades_2.place(x=180, y=385)

# Criando botões para Pokemon
pokemon_imagem_1 = Image.open('images/cabeca-pikachu.png')
pokemon_imagem_1 = pokemon_imagem_1.resize((40, 40))
pokemon_imagem_1 = ImageTk.PhotoImage(pokemon_imagem_1)
bt_pk_1 = Button(janela, image=pokemon_imagem_1, text="Pikachu", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_1.place(x=375, y=10)

pokemon_imagem_2 = Image.open('images/cabeca-bulbasaur.png')
pokemon_imagem_2 = pokemon_imagem_2.resize((40, 40))
pokemon_imagem_2 = ImageTk.PhotoImage(pokemon_imagem_2)
bt_pk_2 = Button(janela, image=pokemon_imagem_2, text="Bulbasaur", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_2.place(x=375, y=65)

pokemon_imagem_3 = Image.open('images/cabeca-charmander.png')
pokemon_imagem_3 = pokemon_imagem_3.resize((40, 40))
pokemon_imagem_3 = ImageTk.PhotoImage(pokemon_imagem_3)
bt_pk_3 = Button(janela, image=pokemon_imagem_3, text="Chamander", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_3.place(x=375, y=120)

pokemon_imagem_4 = Image.open('images/cabeca-gyarados.png')
pokemon_imagem_4 = pokemon_imagem_4.resize((40, 40))
pokemon_imagem_4 = ImageTk.PhotoImage(pokemon_imagem_4)
bt_pk_4 = Button(janela, image=pokemon_imagem_4, text="Gyarados", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_4.place(x=375, y=175)

pokemon_imagem_5 = Image.open('images/cabeca-gengar.png')
pokemon_imagem_5 = pokemon_imagem_5.resize((40, 40))
pokemon_imagem_5 = ImageTk.PhotoImage(pokemon_imagem_5)
bt_pk_5 = Button(janela, image=pokemon_imagem_5, text="Gengar", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_5.place(x=375, y=230)

pokemon_imagem_6 = Image.open('images/cabeca-dragonite.png')
pokemon_imagem_6 = pokemon_imagem_6.resize((40, 40))
pokemon_imagem_6 = ImageTk.PhotoImage(pokemon_imagem_6)
bt_pk_6 = Button(janela, image=pokemon_imagem_6, text="Dragonite", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
bt_pk_6.place(x=375, y=285)

janela.mainloop()