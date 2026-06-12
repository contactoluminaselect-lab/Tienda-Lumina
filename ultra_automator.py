import os
import json
import random
import time
import requests

# --- CONFIGURACIÓN ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LuminaProAutomator:
    def __init__(self):
        self.filename = 'productos.json'
        # BANCO DE IMÁGENES HD (Links directos que siempre funcionan y son variados)
        self.image_bank = {
            "Tecnología": [
                "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800",
                "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800",
                "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=800",
                "https://images.unsplash.com/photo-1491933382434-500287f9b54b?w=800",
                "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800"
            ],
            "Hogar": [
                "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800",
                "https://images.unsplash.com/photo-1544190153-060cb6277f67?w=800",
                "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800",
                "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800",
                "https://images.unsplash.com/photo-1583847268964-b28dc2f51ac9?w=800"
            ],
            "Jardinería": [
                "https://images.unsplash.com/photo-1617576621334-4291ef387ae4?w=800",
                "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800",
                "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800"
            ]
        }

    def get_unique_product(self, existing_names):
        """Genera un producto con nombre e imagen que no se repita"""
        categorias = list(self.image_bank.keys())
        cat = random.choice(categorias)
        
        # Nombres elegantes para combinar
        prefijos = ["Lumina", "Zen", "Aura", "Elite", "Horizon", "Neo"]
        objetos = {
            "Tecnología": ["Smartwatch", "Proyector 4K", "Auriculares Pro", "Cámara Hub"],
            "Hogar": ["Lámpara Orbital", "Prensa Francesa", "Difusor Essential", "Silla Nórdica"],
            "Jardinería": ["Kit Botánico", "Maceta WiFi", "Sensor de Cultivo"]
        }
        
        nombre = random.choice(prefijos) + " " + random.choice(objetos[cat])
        
        # Evitar repetir nombre
        if nombre in existing_names:
            nombre += " " + str(random.randint(2, 9))

        return {
            "id": "LUM-" + str(int(time.time())) + str(random.randint(1,99)),
            "nombre": nombre,
            "precio": random.randint(45, 499),
            "categoria": cat,
            "descripcion": "Selección de alta gama curada por Lumina Select para elevar su estilo de vida.",
            "imagen": random.choice(self.image_bank[cat])
        }

    def run(self):
        # 1. Leer inventario actual
        try:
            with open(self.filename, 'r') as f: products = json.load(f)
        except: products = []

        existing_names = [p['nombre'] for p in products]

        # 2. Crear y añadir producto nuevo
        new_item = self.get_unique_product(existing_names)
        products.append(new_item)
        
        # 3. Limitar catálogo a 12 productos para que no se vea desordenado
        if len(products) > 12:
            products = products[-12:]

        # 4. Guardar
        with open(self.filename, 'w') as f:
            json.dump(products, f, indent=4)
        print(f"Producto '{new_item['nombre']}' añadido con éxito.")

if __name__ == "__main__":
    LuminaProAutomator().run()
