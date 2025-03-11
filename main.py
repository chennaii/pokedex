import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import PIL
from io import BytesIO

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


master = tk.Tk()

master.title("login")
master.geometry("800x500")
master.configure(background = "light blue")

def openNewWindow(): 

    def get_pokemon_data():
        pokemon_name = submit_entry.get().strip().lower()  # Get the Pokémon name from the user input
        
        if not pokemon_name:
            messagebox.showwarning("Input Error", "Please enter a Pokémon name!")
            return
        
        url = f"{BASE_URL}{pokemon_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract the necessary data
            name = data['name'].capitalize()
            types = [t['type']['name'].capitalize() for t in data['types']]
            abilities = [a['ability']['name'].capitalize() for a in data['abilities']]
            height = data['height'] / 10  # Convert to meters
            weight = data['weight'] / 10  # Convert to kilograms
            species_url = data['species']['url']  # Get the species URL for catch rate data
            
            # Fetch species data for catch rate
            species_response = requests.get(species_url)
            if species_response.status_code == 200:
                species_data = species_response.json()
                catch_rate = species_data['capture_rate']  # Capture rate is inside 'capture_rate'
                # Display the catch rate without percentage
                catch_rate_str = f"{catch_rate}"  # Remove the "%" symbol
            else:
                catch_rate_str = "N/A"
            
            # Update the labels with the fetched data
            name_label.config(text=f"{name}")
            type1label.config(text=f"Type 1: {types[0]}")
            type2label.config(text=f"Type 2: {types[1] if len(types) > 1 else 'N/A'}")
            abilities_label.config(text=f"Abilities: {', '.join(abilities)}")
            height_label.config(text=f"Height: {height} m")
            weight_label.config(text=f"Weight: {weight} kg")
            catch_rate_label.config(text=f"Catch Rate: {catch_rate_str}")
            
            # Fetch and display the Pokémon sprite (image)
            sprite_url = data['sprites']['front_default']
            sprite_response = requests.get(sprite_url)
            if sprite_response.status_code == 200:
                sprite_data = sprite_response.content
                img = Image.open(BytesIO(sprite_data))  # Open the image from byte data
                img = img.resize((150, 150))  # Resize the image for display
                
                # Convert the image to a format Tkinter can use
                img_tk = ImageTk.PhotoImage(img)
                
                # Update the image label and keep a reference to the image
                img_label.config(image=img_tk)
                img_label.image = img_tk  # This keeps the reference, which is crucial in Tkinter
            else:
                img_label.config(image='')  # If there's an issue with the image URL
                
        else:
            messagebox.showerror("Not Found", f"Pokémon '{pokemon_name.capitalize()}' not found!")
            img_label.config(image='')  # Clear image if Pokémon not found

    newWindow = tk.Toplevel(master)

    newWindow.title("Pokedex")

    newWindow.geometry("800x500")
    newWindow.configure(background="pink")

    newWindow.rowconfigure([i for i in range(4)], minsize=50, weight=1)
    newWindow.columnconfigure([i for i in range(3)], minsize=50, weight=1)

    search_frame = tk.Frame(newWindow, relief=tk.RAISED, borderwidth=2, background="pink")
    search_frame.columnconfigure([0, 1, 2], weight=1)

    submit_entry = tk.Entry(search_frame, font=("Futura", 16))
    submit_entry.grid(row=0, column=1)

    submit_button = tk.Button(search_frame, text="Search!", font=("Futura", 16), command=get_pokemon_data)
    submit_button.grid(row=0, column=2)


    search_frame.grid(row=0, column=1, columnspan=2, sticky="ew")

    picture_frame = tk.Frame(newWindow, relief=tk.SUNKEN, borderwidth=2, background="pink")
    name_label = tk.Label(picture_frame, text="Pokémon Name", font=("Futura", 16), background="pink")
    name_label.pack(pady=10)  # Display the name at the top of the picture

    img_label = tk.Label(picture_frame, text="Pokémon Picture", font=("Futura", 16), background="pink")
    img_label.pack()
    picture_frame.grid(row=1, column=0, rowspan=2, sticky="ns")

    type_frame = tk.Frame(newWindow, relief=tk.RAISED, borderwidth=2, background="pink")
    type1label = tk.Label(type_frame, text="Type 1", font=("Futura", 12), background="pink")
    type1label.grid(row=0, column=0)
    type2label = tk.Label(type_frame, text="Type 2", font=("Futura", 12), background="pink")
    type2label.grid(row=0, column=1)
    type_frame.grid(row=3, column=0)

    info_frame = tk.Frame(newWindow, relief=tk.SUNKEN, borderwidth=4, background="pink")
    info_frame.rowconfigure([0, 1, 2], weight=1)
    info_frame.columnconfigure([0, 1], weight=1)

    pokedex_entry = tk.Label(info_frame, text="Pokedex Entry", font=("Futura", 16), background="pink")
    pokedex_entry.grid(row=0, column=0, columnspan=2)

    height_label = tk.Label(info_frame, text="Height", font=("Futura", 16), background="pink")
    height_label.grid(row=1, column=0)

    weight_label = tk.Label(info_frame, text="Weight", font=("Futura", 16), background="pink")
    weight_label.grid(row=1, column=1)

    catch_rate_label = tk.Label(info_frame, text="Catch Rate", font=("Futura", 16), background="pink")
    catch_rate_label.grid(row=2, column=0)

    abilities_label = tk.Label(info_frame, text="Abilities", font=("Futura", 16), background="pink")
    abilities_label.grid(row=2, column=1)

    info_frame.grid(row=1, rowspan=3, column=1, columnspan=2, sticky="nsew")
 


btn = tk.Button(master, 
             text ="Click to open pokedex", 
             command = openNewWindow)
btn.pack(pady = 10)
 
master.mainloop()

