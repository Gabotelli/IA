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
        self.main_marco = tk.Frame(root)
        self.main_marco.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Crear un marco para contener la imagen
        self.imagen_marco = tk.Frame(self.main_marco)
        self.imagen_marco.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear un lienzo (Canvas) para mostrar la imagen
        self.lienzo = tk.Canvas(self.imagen_marco)
        self.lienzo.pack(fill=tk.BOTH, expand=True)
        # Agregar un botón para ingresar la hora de salida
        boton_introducir_tiempo = Button(self.main_marco, text="Hora de Salida", command=self.introducir_tiempo_salida)
        boton_introducir_tiempo.pack(pady=10)
        # Botón para preguntar al usuario si quiere ingresar manualmente o seleccionar en el mapa
        boton_preguntar_metodo = Button(self.main_marco, text="¿Cómo quieres ingresar el destino?", command=self.metodo_de_introduccion)
        boton_preguntar_metodo.pack(pady=10)
        # Coordenadas del origen y destino ingresadas por el usuario
        self.origen_coordenadas = None
        self.destino_coordenadas = None
        #Origen y destino
        self.origen=""
        self.destino=""
        # Cuadros de entrada para las coordenadas
        self.origen_entry = Entry(self.main_marco, width=10)
        self.origen_entry.pack(pady=5)

        self.destino_entry = Entry(self.main_marco, width=10)
        self.destino_entry.pack(pady=5)

        # Agregar etiquetas para mostrar mensajes
        self.origen_etiqueta = tk.Label(self.main_marco, text="Origen:", font=("Arial", 14), bg="white")
        self.origen_etiqueta.pack(pady=5)

        self.destino_etiqueta = tk.Label(self.main_marco, text="Destino:", font=("Arial", 14), bg="white")
        self.destino_etiqueta.pack(pady=5)
        
        # Preferencia del usuario
        self.preferencia_var = None
        self.preferencia = None
        #Variable hora de salida
        self.hora_de_partida=None

        # Etiqueta para mostrar la hora de salida
        self.hora_etiqueta = tk.Label(self.main_marco, text="Hora de Salida: ", font=("Arial", 14), bg="white")
        self.hora_etiqueta.pack(pady=5)

        # Intentar cargar automáticamente la imagen del mapa al iniciar
        self.cargar_mapa(map_url)
    #Asocia a cada estacion un rango de coordenadas donde ser seleccionada
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
            res="Monplaisir - Lumière"
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
            res="Stade De Gerland"
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
            res="Laurent Bonnevay Astroballe"
        elif c1<582 and c1>562 and c2<250 and c2>230:
            res="Vaulx-en-Velin La Soie"
        return res
    def cargar_mapa(self, map_path):
        try:
            # Abre la imagen desde el directorio
            imagen = Image.open(map_path)
            self.imagen_mapa = ImageTk.PhotoImage(imagen)
            self.lienzo.config(width=imagen.width, height=imagen.height)
            self.lienzo.create_image(0, 0, anchor=tk.NW, image=self.imagen_mapa)
        except Exception as e:
            print(f"Error al cargar la imagen desde el directorio: {e}")

    def metodo_de_introduccion(self):
        # Crear una ventana emergente para preguntar al usuario cómo quiere ingresar el destino
        method_ventana = Toplevel(self.root)
        method_ventana.title("Método de Ingreso")

        # Variables de control para los botones de opción
        metodo_introducido_var = StringVar()

        # Función para manejar la elección del usuario
        def metodo_seleccionado():
            metodo_introducido = metodo_introducido_var.get()
            print(f"Usuario elige ingresar: {metodo_introducido}")

            # Cerrar la ventana emergente
            method_ventana.destroy()

            # Procesar la elección del usuario y continuar
            if metodo_introducido == "manual":
                self.introducir_coordenadas_manualmente()
            elif metodo_introducido == "map":
                self.seleccionar_coordenadas_en_el_map()

        # Etiqueta y botones de opción
        etiqueta = Label(method_ventana, text="¿Cómo quieres ingresar el destino?")
        etiqueta.pack(pady=10)

        manual_button = Radiobutton(method_ventana, text="Manualmente", variable=metodo_introducido_var, value="manual")
        manual_button.pack()

        map_button = Radiobutton(method_ventana, text="En el mapa", variable=metodo_introducido_var, value="map")
        map_button.pack()

        # Botón para confirmar la elección
        confirm_button = Button(method_ventana, text="Continuar", command=metodo_seleccionado)
        confirm_button.pack(pady=10)

    def introducir_coordenadas_manualmente(self):
        # Habilitar los cuadros de entrada para ingresar manualmente
        self.origen_entry.config(state=tk.NORMAL)
        self.destino_entry.config(state=tk.NORMAL)
        # Botón para continuar después de ingresar manualmente
        continue_button = Button(self.main_marco, text="Continuar", command=self.continuar_despues_de_introducir_manualmente)
        continue_button.pack(pady=10)

    def seleccionar_coordenadas_en_el_map(self):
        # Deshabilitar los cuadros de entrada manual
        self.origen_entry.config(state=tk.DISABLED)
        self.destino_entry.config(state=tk.DISABLED)

        # Llamar a la función cuando se hace clic en el lienzo
        self.lienzo.bind("<Button-1>", self.click_en_la_imagen)

    def click_en_la_imagen(self, event):
        # Obtener las coordenadas del clic en relación con la imagen
        x, y = event.x, event.y

        if self.origen_coordenadas is None:
            # Si aún no se ha seleccionado el origen, hazlo
            self.origen_coordenadas = (x, y)
            self.lienzo.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue", outline="blue")
            self.origen_etiqueta.config(text=f"Origen:"+self.coordenadas_a_estaciones(self.origen_coordenadas))
        elif self.destino_coordenadas is None:
            # Si ya se ha seleccionado el origen, selecciona el destino
            self.destino_coordenadas = (x, y)
            self.lienzo.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="red")
            self.destino_etiqueta.config(text=f"Destino:"+self.coordenadas_a_estaciones(self.destino_coordenadas))

            # Preguntar al usuario sobre sus preferencias
            self.pregunta_preferencias_usuario()

    def introducir_tiempo_salida(self):
        # Pedir al usuario que ingrese la hora de salida
        hora_de_partida = askstring("Hora de Salida", "Ingrese la hora de salida (formato HH:MM):")

        # Convertir la hora ingresada a un objeto datetime
        self.hora_de_partida = dt.datetime(2003, 6, 18, int(hora_de_partida[0:2]), int(hora_de_partida[3:5]), 0)
        print("La hora seleccionada es ", self.hora_de_partida)

        # Mostrar la hora de salida en la etiqueta
        self.hora_etiqueta.config(text=f"Hora de Salida: {hora_de_partida}")

        # Aquí puedes agregar más funcionalidades según tus necesidades.
    def continuar_despues_de_introducir_manualmente(self):
        # Guardar las coordenadas ingresadas manualmente
        self.origen = self.origen_entry.get()
        self.destino = self.destino_entry.get()

        # Mostrar las coordenadas ingresadas manualmente
        print(f"Origen (manual): {self.origen}")
        print(f"Destino (manual): {self.destino}")
        # Continuar con otras acciones después de ingresar manualmente
        self.pregunta_preferencias_usuario()

    def pregunta_preferencias_usuario(self):
        # Crear una ventana emergente para la pregunta
        ventana_preferencias = Toplevel(self.root)
        ventana_preferencias.title("Preferencias")

        # Variables de control para los botones de opción
        self.preferencia_var = StringVar()

        # Función para manejar la elección del usuario
        def manejo_preferencia_seleccionada():
            self.preferencia = self.preferencia_var.get()
            print(f"El usuario prefiere: {self.preferencia}")

            # Cerrar la ventana emergente
            ventana_preferencias.destroy()

            # Continuar con otras acciones después de que el usuario haya ingresado las coordenadas y preferencias
            self.calculo_y_muestra_del_mejor_camino()

        # Etiqueta y botones de opción
        etiqueta = Label(ventana_preferencias, text="¿Qué es más importante para ti?")
        etiqueta.pack(pady=10)

        boton_duracion = Radiobutton(ventana_preferencias, text="Duración del viaje", variable=self.preferencia_var, value="Duración del viaje")
        boton_duracion.pack()

        boton_transbordos = Radiobutton(ventana_preferencias, text="Número de Transbordos", variable=self.preferencia_var, value="No transbordos")
        boton_transbordos.pack()

        # Botón para confirmar la elección
        boton_confirmacion = Button(ventana_preferencias, text="Confirmar", command=manejo_preferencia_seleccionada)
        boton_confirmacion.pack(pady=10)
    def mostrar_mensaje_en_etiqueta(self, mensaje):
        # Crear una nueva ventana para mostrar el mensaje
        mensaje_ventana = Toplevel(self.root)
        mensaje_ventana.title("Mensaje")

        # Crear un Label para mostrar el mensaje
        etiqueta = Label(mensaje_ventana, text=mensaje, font=("Arial", 14), bg="white")
        etiqueta.pack(pady=10)

        # Iniciar el bucle principal de la ventana de mensaje
        mensaje_ventana.mainloop()

    def enseñar_segunda_imagen(self, second_map_path):
        try:
            # Abrir la segunda imagen desde el directorio
            segunda_imagen = Image.open(second_map_path)
            mapa_segunda_imagen = ImageTk.PhotoImage(segunda_imagen)

            # Crear una nueva ventana para la segunda imagen
            ventana_segunda_imagen = Toplevel(self.root)
            ventana_segunda_imagen.title("Segunda Imagen")

            # Crear un lienzo (Canvas) para mostrar la segunda imagen
            segundo_lienzo = tk.Canvas(ventana_segunda_imagen)
            segundo_lienzo.pack(fill=tk.BOTH, expand=True)
            segundo_lienzo.config(width=segunda_imagen.width, height=segunda_imagen.height)
            segundo_lienzo.create_image(0, 0, anchor=tk.NW, image=mapa_segunda_imagen)

            # Iniciar el bucle principal de la ventana de la segunda imagen
            ventana_segunda_imagen.mainloop()
        except Exception as e:
            print(f"Error al cargar la segunda imagen desde el directorio: {e}")

    def calculo_y_muestra_del_mejor_camino(self):
        #Si se han seleccionado las estaciones en el mapa se hace la conversion de coordenadas a estacioness
        if self.origen_coordenadas is not None and self.destino_coordenadas is not None:
            self.origen=self.coordenadas_a_estaciones(self.origen_coordenadas)
            self.destino=self.coordenadas_a_estaciones(self.destino_coordenadas)
            print("Origen:", self.origen)
            print("Destino", self.destino)
            #Se ejecuta el algoritmo
            ini_instance = ini.Ini(self.origen, self.destino, self.preferencia ,self.hora_de_partida)
        else:
            #Se ejecuta el algoritmo
            ini_instance = ini.Ini(self.origen, self.destino, self.preferencia ,self.hora_de_partida)

        if(ini_instance.ini()==-1):
            # Mostrar el mensaje sobre el estado del metro
            metro_status_mensaje ="El metro está cerrado a esta hora."
            self.mostrar_mensaje_en_etiqueta(metro_status_mensaje)
        # Mostrar la segunda imagen después de cerrar la aplicación principal
        second_map_path = "../IA/Lyon/recorrido_final.png"
        self.enseñar_segunda_imagen(second_map_path)



# Imagen del metro de Lyon
map_path = "../IA/Lyon/metro_lyon.png"

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = MapApp(root, map_path)

# Iniciar el bucle principal
root.mainloop()











