import datetime as dt
import tkinter as tk
from tkinter import Button, Entry, Label, Radiobutton, StringVar, Toplevel
from tkinter.simpledialog import askstring

from PIL import Image, ImageTk

import ini


class MapApp:
    def __init__(self, root, map_url):
        self.root = root
        self.root.title("Mapa Interactivo")

        # Crear un marco principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Crear un marco para contener la imagen
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear un lienzo (Canvas) para mostrar la imagen
        self.canvas = tk.Canvas(self.image_frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Coordenadas del origen y destino ingresadas por el usuario
        self.origin_coordinates = None
        self.destination_coordinates = None
        #Origen y destino
        self.origin=""
        self.destination=""
        # Cuadros de entrada para las coordenadas
        self.origin_entry = Entry(self.main_frame, width=10)
        self.origin_entry.pack(pady=5)

        self.destination_entry = Entry(self.main_frame, width=10)
        self.destination_entry.pack(pady=5)

        # Agregar etiquetas para mostrar mensajes
        self.origin_label = tk.Label(self.main_frame, text="Origen:", font=("Arial", 14), bg="white")
        self.origin_label.pack(pady=5)

        self.destination_label = tk.Label(self.main_frame, text="Destino:", font=("Arial", 14), bg="white")
        self.destination_label.pack(pady=5)
        
        # Preferencia del usuario
        self.preference_var = None
        self.preference = None
        #Variable hora de salida
        self.departure_time=None
        # Botón para preguntar al usuario si quiere ingresar manualmente o seleccionar en el mapa
        ask_method_button = Button(self.main_frame, text="¿Cómo quieres ingresar el destino?", command=self.ask_input_method)
        ask_method_button.pack(pady=10)
        # Agregar un botón para ingresar la hora de salida
        enter_time_button = Button(self.main_frame, text="Hora de Salida", command=self.enter_departure_time)
        enter_time_button.pack(pady=10)

        # Intentar cargar automáticamente la imagen del mapa al iniciar
        self.load_map(map_url)
    def coordenadas_a_estaciones(self,coords):
        c1=coords[0]
        c2=coords[1]
        res="Selección no válida"
        if c1<72 and c1>52 and c2<133 and c2>113:
            res="Gare de Vaise"
        elif c1<75 and c1>55 and c2<168 and c2>148:
            res="Valmy"
        elif c1<76 and c1>56 and c2<222 and c2>202:
            res="Gorge de Loup"
        elif c1<164 and c1>144 and c2<259 and c2>239:
            res="Vieux Lyon\nCathedrale St. Jean"
        elif c1<144 and c1>127 and c2<268 and c2>248:
            res="Minimes Theatres Romains"
        elif c1<128 and c1>109 and c2<273 and c2>253:
            res="Saint Just"
        elif c1<195 and c1>175 and c2<279 and c2>259:
            res="Bellecour"
        elif c1<238 and c1>218 and c2<292 and c2>272:
            res="Guillotière"
        elif c1<255 and c1>235 and c2<301 and c2>281:
            res="Saxe Gambetta"
        elif c1<291 and c1>271 and c2<319 and c2>299:
            res="Garibaldi"
        elif c1<333 and c1>313 and c2<339 and c2>319:
            res="Sans-Souci"
        elif c1<360 and c1>340 and c2<353 and c2>333:
            res="Monplaisir-Lumière"
        elif c1<396 and c1>376 and c2<370 and c2>350:
            res="Grange Blanche"
        elif c1<420 and c1>400 and c2<390 and c2>370:
            res="Laennec"
        elif c1<428 and c1>408 and c2<453 and c2>433:
            res="Mermoz Pinel"
        elif c1<429 and c1>409 and c2<503 and c2>483:
            res="Parilly"
        elif c1<433 and c1>413 and c2<595 and c2>575:
            res="Garre de Venissieux"
        elif c1<116 and c1>96 and c2<536 and c2>516:
            res="Oullins Gare"
        elif c1<185 and c1>165 and c2<474 and c2>454:
            res="Stade de Gerland"
        elif c1<198 and c1>178 and c2<442 and c2>422:
            res="Debourg"
        elif c1<219 and c1>199 and c2<392 and c2>372:
            res="Place Jean Jaurès"
        elif c1<234 and c1>214 and c2<353 and c2>333:
            res="Jean Macé"
        elif c1<260 and c1>240 and c2<269 and c2>249:
            res="Place Guichard Bourse\nDu Travail"
        elif c1<299 and c1>279 and c2<249 and c2>229:
            res="Gare Part-Dieu\nVivier Merle"
        elif c1<309 and c1>289 and c2<222 and c2>202:
            res="Brotteaux"
        elif c1<316 and c1>296 and c2<200 and c2>180:
            res="Charpennes\nCharles Hernu"
        elif c1<194 and c1>174 and c2<95 and c2>75:
            res="Cuire"
        elif c1<170 and c1>150 and c2<148 and c2>128:
            res="Hénon"
        elif c1<190 and c1>170 and c2<171 and c2>151:
            res="Croix-Rousse"
        elif c1<206 and c1>186 and c2<192 and c2>172:
            res="Croix-Paquet"
        elif c1<208 and c1>188 and c2<216 and c2>196:
            res="Hotel De Ville\nLouis Pradel"
        elif c1<168 and c1>148 and c2<332 and c2>312:
            res="Perrache"
        elif c1<178 and c1>158 and c2<306 and c2>286:
            res="Ampère Victor Hugo"
        elif c1<208 and c1>188 and c2<242 and c2>222:
            res="Cordeliers"
        elif c1<248 and c1>228 and c2<209 and c2>189:
            res="Foch"
        elif c1<285 and c1>265 and c2<204 and c2>184:
            res="Masséna"
        elif c1<370 and c1>350 and c2<197 and c2>177:
            res="République Villeurbanne"
        elif c1<397 and c1>377 and c2<205 and c2>185:
            res="Gratte-Ciel"
        elif c1<438 and c1>418 and c2<215 and c2>195:
            res="Flachet"
        elif c1<478 and c1>458 and c2<226 and c2>206:
            res="Cusset"
        elif c1<519 and c1>499 and c2<237 and c2>217:
            res="Laurent Bonnevay Astrobalie"
        elif c1<582 and c1>562 and c2<250 and c2>230:
            res="Vaulx-en-Velin La Soie"
        return res
    def load_map(self, map_path):
        try:
            # Open the image from the directory
            image = Image.open(map_path)
            self.map_image = ImageTk.PhotoImage(image)
            self.canvas.config(width=image.width, height=image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map_image)
        except Exception as e:
            print(f"Error al cargar la imagen desde el directorio: {e}")

    def ask_input_method(self):
        # Crear una ventana emergente para preguntar al usuario cómo quiere ingresar el destino
        method_window = Toplevel(self.root)
        method_window.title("Método de Ingreso")

        # Variables de control para los botones de opción
        input_method_var = StringVar()

        # Función para manejar la elección del usuario
        def on_input_method_selected():
            input_method = input_method_var.get()
            print(f"Usuario elige ingresar: {input_method}")

            # Cerrar la ventana emergente
            method_window.destroy()

            # Procesar la elección del usuario y continuar
            if input_method == "manual":
                self.enter_coordinates_manually()
            elif input_method == "map":
                self.select_coordinates_on_map()

        # Etiqueta y botones de opción
        label = Label(method_window, text="¿Cómo quieres ingresar el destino?")
        label.pack(pady=10)

        manual_button = Radiobutton(method_window, text="Manualmente", variable=input_method_var, value="manual")
        manual_button.pack()

        map_button = Radiobutton(method_window, text="En el mapa", variable=input_method_var, value="map")
        map_button.pack()

        # Botón para confirmar la elección
        confirm_button = Button(method_window, text="Continuar", command=on_input_method_selected)
        confirm_button.pack(pady=10)

    def enter_coordinates_manually(self):
        # Habilitar los cuadros de entrada para ingresar manualmente
        self.origin_entry.config(state=tk.NORMAL)
        self.destination_entry.config(state=tk.NORMAL)
        # Botón para continuar después de ingresar manualmente
        continue_button = Button(self.main_frame, text="Continuar", command=self.continue_after_manual_input)
        continue_button.pack(pady=10)

    def select_coordinates_on_map(self):
        # Deshabilitar los cuadros de entrada manual
        self.origin_entry.config(state=tk.DISABLED)
        self.destination_entry.config(state=tk.DISABLED)

        # Llamar a la función cuando se hace clic en el lienzo
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        # Obtener las coordenadas del clic en relación con la imagen
        x, y = event.x, event.y

        if self.origin_coordinates is None:
            # Si aún no se ha seleccionado el origen, hazlo
            self.origin_coordinates = (x, y)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue", outline="blue")
            self.origin_label.config(text=f"Origen:"+self.coordenadas_a_estaciones(self.origin_coordinates))
        elif self.destination_coordinates is None:
            # Si ya se ha seleccionado el origen, selecciona el destino
            self.destination_coordinates = (x, y)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="red")
            self.destination_label.config(text=f"Destino:"+self.coordenadas_a_estaciones(self.destination_coordinates))

            # Preguntar al usuario sobre sus preferencias
            self.ask_user_preferences()

    def enter_departure_time(self):
        # Pedir al usuario que ingrese la hora de salida
        departure_time = askstring("Hora de Salida", "Ingrese la hora de salida (formato HH:MM):")
        self.departure_time = dt.datetime(2003, 6, 18, int(departure_time[0:2]), int(departure_time[3:5]), 0)
        # Puedes realizar acciones adicionales con la hora de salida ingresada, como almacenarla para su uso posterior.
        print(f"Hora de Salida ingresada: {self.departure_time}")

        # Aquí puedes agregar más funcionalidades según tus necesidades.
    def continue_after_manual_input(self):
        # Guardar las coordenadas ingresadas manualmente
        self.origin = self.origin_entry.get()
        self.destination = self.destination_entry.get()

        # Mostrar las coordenadas ingresadas manualmente
        print(f"Origen (manual): {self.origin}")
        print(f"Destino (manual): {self.destination}")
        # Continuar con otras acciones después de ingresar manualmente
        self.ask_user_preferences()

    def ask_user_preferences(self):
        # Crear una ventana emergente para la pregunta
        preferences_window = Toplevel(self.root)
        preferences_window.title("Preferencias")

        # Variables de control para los botones de opción
        self.preference_var = StringVar()

        # Función para manejar la elección del usuario
        def on_preference_selected():
            self.preference = self.preference_var.get()
            print(f"El usuario prefiere: {self.preference}")

            # Puedes realizar acciones adicionales según la preferencia del usuario
            # Por ejemplo, podrías planificar la ruta en función de su elección.

            # Cerrar la ventana emergente
            preferences_window.destroy()

            # Continuar con otras acciones después de que el usuario haya ingresado las coordenadas y preferencias
            self.continue_after_preferences()

        # Etiqueta y botones de opción
        label = Label(preferences_window, text="¿Qué es más importante para ti?")
        label.pack(pady=10)

        time_button = Radiobutton(preferences_window, text="Tiempo de salida", variable=self.preference_var, value="Tiempo de salida")
        time_button.pack()
        
        transfersTime_button = Radiobutton(preferences_window, text="Tiempo entre transbordos", variable=self.preference_var, value="Tiempo entre transbordos")
        transfersTime_button.pack()

        transfers_button = Radiobutton(preferences_window, text="Número de Transbordos", variable=self.preference_var, value="No transbordos")
        transfers_button.pack()

        # Botón para confirmar la elección
        confirm_button = Button(preferences_window, text="Confirmar", command=on_preference_selected)
        confirm_button.pack(pady=10)

    def continue_after_preferences(self):
        # Aquí puedes agregar acciones adicionales que deseas realizar después de que el usuario haya ingresado las coordenadas y preferencias.
        # Falta preguntar por el tiempo entre transbordos para poder pasarlo a la clase ini

        if self.origin_coordinates is not None and self.destination_coordinates is not None:
            print("Origen:", self.coordenadas_a_estaciones(self.origin_coordinates))
            print("Destino", self.coordenadas_a_estaciones(self.destination_coordinates))
            ini_instance = ini.Ini(self.coordenadas_a_estaciones(self.origin_coordinates), self.coordenadas_a_estaciones(self.destination_coordinates), self.preference ,self.departure_time) #aqui hay que poner la preferencia del usuario
        else:
            ini_instance = ini.Ini(self.origin, self.destination, self.preference ,self.departure_time) #aqui hay que poner la preferencia del usuario
        print("Continuar con otras acciones...")
        #ini_instance = ini.Ini(self.origin_entry.get(), self.destination_entry.get(), self.preference, 20) #aqui hay que poner la preferencia del usuario
        if(ini_instance==-1):
            print("Mongolo pedazo de inutil amorfo aprende cuando esta abierto el metro")
            

        self.root.destroy()

        """# Crear una ventana emergente para mostrar un texto predeterminado
        text_entry_window = Toplevel(self.root)
        text_entry_window.title("Ruta a Seguir")
    
        # Etiqueta con el texto predeterminado
        text_label = Label(text_entry_window, text="Ruta a seguir:", font=("Arial", 14), bg="white")
        text_label.pack(pady=10)
    
        # Texto predeterminado
        default_text = "Aquí puedes mostrar la ruta a seguir."
        text_content_label = Label(text_entry_window, text=default_text, font=("Arial", 12))
        text_content_label.pack(pady=10)"""



# Imagen del metro de Lyon
map_path = "../IA/Lyon/metro_lyon.png"

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = MapApp(root, map_path)

# Iniciar el bucle principal
root.mainloop()











