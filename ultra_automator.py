import os
import json
import random
import time

class LuminaFinalAutomator:
    def __init__(self):
        self.filename = 'productos.json'
        # Base de datos de alta gama con imágenes garantizadas
        self.db = {
            "Tecnología": [
                {"id": "T1", "nombre": "Cámara Retro Lumina", "precio": 450, "categoria": "Tecnología", "desc": "Captura momentos con estilo vintage y sensor 4K.", "imagen": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800"},
                {"id": "T2", "nombre": "Reloj de Cuero Minimal", "precio": 180, "categoria": "Tecnología", "desc": "La esencia del tiempo en un diseño suizo.", "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"}
            ],
            "Hogar": [
                {"id": "H1", "nombre": "Lámpara Orbital", "precio": 95, "categoria": "Hogar", "desc": "Iluminación ambiental con diseño futurista.", "imagen": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800"},
                {"id": "H2", "nombre": "Silla Nórdica", "precio": 220, "categoria": "Hogar", "desc": "Comodidad y minimalismo para su espacio.", "imagen": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800"}
            ],
            "Jardín": [
                {"id": "J1", "nombre": "Maceta de Cemento Pro", "precio": 45, "categoria": "Jardín", "desc": "Diseño industrial para sus plantas favoritas.", "imagen": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800"}
            ]
        }

    def run(self):
        try:
            with open(self.filename, 'r') as f: products = json.load(f)
        except: products = []

        # Elegir un producto nuevo que no esté ya
        existing_ids = [p['id'] for p in products]
        available = []
        for cat in self.db:
            for p in self.db[cat]:
                if p['id'] not in existing_ids: available.append(p)

        if available:
            new_item = random.choice(available)
            # Normalizar nombres de campos
            new_item['descripcion'] = new_item['desc'] 
            new_item['updated'] = str(time.time())
            products.append(new_item)
            print(f"Agregado: {new_item['nombre']}")
        else:
            print("Ya tienes todos los productos actuales.")

        with open(self.filename, 'w') as f:
            json.dump(products, f, indent=4)

if __name__ == "__main__":
    LuminaFinalAutomator().run()
