# --- IMPORT DE BIBLIOTECAS ---
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import pygame
import time
import os

# --- CONFIGURACIÓN DE SONIDO ---
try:
    pygame.mixer.init()
    pygame.mixer.music.load("cafe-music-163375.mp3")
    pygame.mixer.music.play(-1)
    print("🎵 Música de fondo iniciada correctamente.")
except Exception as e:
    print(f"No se pudo reproducir la música: {e}")

# --- DATOS DE LA APLICACIÓN ---
menu = {
    "Café Americano": 2.50,
    "Latte": 3.00,
    "Croissant": 1.75,
    "Pastel de Chocolate": 4.50,
    "Té Verde": 2.25
}

pedido_actual = []
total_actual = 0.0
num_pedido = 0

# --- FUNCIONES ---
def agregar_producto(producto):
    global total_actual
    pedido_actual.append(producto)
    total_actual += menu[producto]
    print(f"Añadido: {producto.upper()} | Total actual: ${total_actual:.2f}")

def mostrar_total():
    global total_actual, pedido_actual, num_pedido
    if pedido_actual:
        num_pedido += 1
        print(f"Pedido #{num_pedido} → {pedido_actual} | Total: ${total_actual:.2f}")
        print("¡Gracias por tu compra! ☕✨")
        total_actual = 0.0
        pedido_actual = []
    else:
        print("ERROR: No pediste nada. :c")

def resetear_orden():
    global total_actual, pedido_actual
    pedido_actual = []
    total_actual = 0.0
    print("Se ha reseteado tu pedido ☕")

# --- CONFIGURACIÓN DE LA VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Cafetería - Universidad Nacional")
ventana.geometry("700x550")
ventana.configure(bg="#f5f0e6")

# --- POSTER DIGITAL (PITCH VISUAL) ---
poster_frame = tk.Frame(ventana, bg="#f7f3ed", relief="flat")
poster_frame.pack(fill="x", pady=15)

# Logo centrado
logo_path = "logo.png"
try:
    logo_img = Image.open(logo_path).resize((180, 180))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(poster_frame, image=logo_photo, bg="#f7f3ed")
    logo_label.image = logo_photo
    logo_label.pack(pady=(10, 5))
except:
    logo_label = tk.Label(poster_frame, text="☕", font=("Helvetica", 60), bg="#f7f3ed")
    logo_label.pack(pady=(10, 5))

# Título principal
titulo_pitch = tk.Label(
    poster_frame,
    text="CAFÉ UNAL - Tu momento, tu café",
    font=("Helvetica", 22, "bold"),
    bg="#f7f3ed",
    fg="#3e2723"
)
titulo_pitch.pack()

# --- MENÚ DE PRODUCTOS ---
titulo_label = ttk.Label(ventana, text="Menú de Cafetería", font=("Helvetica", 18, "bold"))
titulo_label.pack(pady=10)

menu_frame = ttk.Frame(ventana)
menu_frame.pack(pady=10)

ttk.Button(menu_frame, text="Café Americano", command=lambda: agregar_producto("Café Americano")).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(menu_frame, text="Latte", command=lambda: agregar_producto("Latte")).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(menu_frame, text="Croissant", command=lambda: agregar_producto("Croissant")).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(menu_frame, text="Pastel de Chocolate", command=lambda: agregar_producto("Pastel de Chocolate")).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(menu_frame, text="Completar Orden", command=mostrar_total).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(menu_frame, text="Intentar de nuevo", command=resetear_orden).grid(row=2, column=0, padx=5, pady=5)

# --- ANIMACIÓN SIMPLE ---
try:
    taza_img = Image.open("coffee.png").resize((80, 80))
    taza_photo = ImageTk.PhotoImage(taza_img)
    taza_label = tk.Label(ventana, image=taza_photo, bg="#f5f0e6")
    taza_label.place(x=0, y=440)
except:
    taza_label = tk.Label(ventana, text="☕", font=("Arial", 40), bg="#f5f0e6")
    taza_label.place(x=0, y=440)

def mover_taza():
    x = 0
    direccion = 1
    while True:
        if x >= 620:
            direccion = -1
        elif x <= 0:
            direccion = 1
        x += direccion * 5
        taza_label.place(x=x, y=440)
        time.sleep(0.05)

threading.Thread(target=mover_taza, daemon=True).start()

# --- INICIAR LA APP ---
ventana.mainloop()