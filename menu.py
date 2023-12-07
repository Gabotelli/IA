import tkinter as tk
from tkinter import Button, Entry, Label, Radiobutton, StringVar, Toplevel

import requests
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
        
        # Botón para preguntar al usuario si quiere ingresar manualmente o seleccionar en el mapa
        ask_method_button = Button(self.main_frame, text="¿Cómo quieres ingresar el destino?", command=self.ask_input_method)
        ask_method_button.pack(pady=10)

        # Intentar cargar automáticamente la imagen del mapa al iniciar
        self.load_map(map_url)

    def load_map(self, map_url):
        try:
            # Descargar la imagen desde la URL
            image = Image.open(requests.get(map_url, stream=True).raw)
            self.map_image = ImageTk.PhotoImage(image)
            self.canvas.config(width=image.width, height=image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map_image)
        except Exception as e:
            print(f"Error al cargar la imagen desde la URL: {e}")

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
            self.origin_label.config(text=f"Origen: ({x}, {y})")
        elif self.destination_coordinates is None:
            # Si ya se ha seleccionado el origen, selecciona el destino
            self.destination_coordinates = (x, y)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="red")
            self.destination_label.config(text=f"Destino: ({x}, {y})")

            # Preguntar al usuario sobre sus preferencias
            self.ask_user_preferences()

    def continue_after_manual_input(self):
        # Guardar las coordenadas ingresadas manualmente
        origin_text = self.origin_entry.get()
        destination_text = self.destination_entry.get()

        # Mostrar las coordenadas ingresadas manualmente
        print(f"Origen (manual): {origin_text}")
        print(f"Destino (manual): {destination_text}")

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

        transfers_button = Radiobutton(preferences_window, text="Número de Transbordos", variable=self.preference_var, value="Transbordos")
        transfers_button.pack()

        # Botón para confirmar la elección
        confirm_button = Button(preferences_window, text="Confirmar", command=on_preference_selected)
        confirm_button.pack(pady=10)

    def continue_after_preferences(self):
        # Aquí puedes agregar acciones adicionales que deseas realizar después de que el usuario haya ingresado las coordenadas y preferencias.
        # Falta preguntar por el tiempo entre transbordos para poder pasarlo a la clase ini
        ini_instance = ini.Ini(self.origin_entry.get(), self.destination_entry.get(), self.preference, 20) #aqui hay que poner la preferencia del usuario
        ini_instance.ini()
        if self.origin_coordinates is not None and self.destination_coordinates is not None:
            print(f"Origen: {self.origin_coordinates}")
            print(f"Destino: {self.destination_coordinates}")

        else:
            print("No se han seleccionado coordenadas en el mapa.")
        print("Continuar con otras acciones...")
    
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
map_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lyon_-_Metro_network_map.png/600px-Lyon_-_Metro_network_map.png"

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = MapApp(root, map_url)

# Iniciar el bucle principal
root.mainloop()











