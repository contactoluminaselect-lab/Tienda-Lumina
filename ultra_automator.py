import os
import json
import time
import random

class SimpleAutomator:
    def run(self):
        file = 'productos.json'
        
        # 1. Leer lo que hay
        try:
            with open(file, 'r') as f: products = json.load(f)
        except: products = []

        # 2. Inventar un producto súper rápido (Plan B infalible)
        nombres = ["Reloj", "Lámpara", "Cámara", "Cargador", "Difusor", "Set Belleza", "Auriculares"]
        escogido = random.choice(nombres)
        
        new_item = {
            "id": "LUM-" + str(int(time.time())), # ID único por tiempo
            "nombre": escogido + " Edition " + str(random.randint(1,99)),
            "precio": random.randint(30, 400),
            "categoria": random.choice(["Tecnología", "Hogar", "Belleza"]),
            "descripcion": "Selección premium de Lumina Select.",
            "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"
        }

        # 3. AÑADIR (Aquí estaba el error, ahora forzamos el append)
        products.append(new_item)
        
        # Guardar solo los últimos 20 para no romper la web
        if len(products) > 20:
            products = products[-20:]

        with open(file, 'w') as f:
            json.dump(products, f, indent=4)
        print(f"Producto {new_item['nombre']} guardado.")

if __name__ == "__main__":
    SimpleAutomator().run()
