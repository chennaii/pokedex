import tkinter as tk 


# opens window
window = tk.Tk()

window.title("pokedex")
window.configure(background = "pink")
window.geometry("800x500")

window.rowconfigure([i for i in range(4)], minsize = 50, weight = 1)
window.columnconfigure([i for i in range(3)], minsize = 50, weight = 1)

# rows and coloumns 
name_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 4)
label = tk.Label(name_frame, text = "pokemons name", font = ("Futura", 16))

# frame for name
name_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 4)
label = tk.Label(name_frame, text = "pokemons Name", font = ("Futura", 16))

#where the picture goes 
picture_frame = tk.Frame(window, relief = tk.SUNKEN, borderwidth = 2)
label = tk.Label(picture_frame, text = "pokemons Picture", font = ("Futura", 16))
label.pack()
picture_frame.grid(row = 1, column = 0, rowspan = 2, sticky = "ns")

#where the types go
type_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)
type1label = tk.Label(type_frame, text = "type 1 ", font = ("Futura", 12))
type1label.grid(row = 0, column = 0)
type2label = tk.Label(type_frame, text = "type 2 ", font = ("Futura", 12))
type2label.grid(row = 0, column = 1)
type_frame.grid(row = 3, column = 0)

#where they can search 
search_frame = tk.Frame(window, relief = tk.RAISED, borderwidth = 2)

#rowconfigure and columnfigure with an infoframe this helps the lable to be centred 
search_frame.columnconfigure([0,1,2,3], weight = 1)

label = tk.Label(search_frame, text = "left Arrow", font = ("Futura", 16))
label.grid(row = 0, column = 0)

label = tk.Label(search_frame, text = "search box\n drop-down menu", font = ("Futura", 16))
label.grid(row = 0, column = 1, columnspan = 2)

label = tk.Label(search_frame, text = "right Arrow", font = ("Futura", 16))
label.grid(row = 0, column = 3)

search_frame.grid(row = 0, column = 1, columnspan = 2, sticky = "ew")

#info frame 
info_frame = tk.Frame(window, relief = tk.SUNKEN, borderwidth = 4)

# helps the lable be centred 
info_frame.rowconfigure([0,1,2], weight = 1)
info_frame.columnconfigure([0,1], weight = 1)

#where the pokedex entry will be 
pokedex_entry = tk.Label(info_frame, text = "Pokedex Entry", font = ("Futura", 16))
pokedex_entry.grid(row = 0, column = 0, columnspan = 2)

height_entry = tk.Label(info_frame, text = "Height", font = ("Futura", 16))
height_entry.grid(row = 1, column = 0)

weight_entry = tk.Label(info_frame, text = "Weight", font = ("Futura", 16))
weight_entry.grid(row = 1, column = 1)

species_entry = tk.Label(info_frame, text = "Species", font = ("Futura", 16))
species_entry.grid(row = 2, column = 0)

catch_entry = tk.Label(info_frame, text = "Catch Rate", font = ("Futura", 16))
catch_entry.grid(row = 2, column = 1)

info_frame.grid(row = 1, rowspan = 3, column = 1, columnspan = 2, sticky = "nsew")


window.mainloop()