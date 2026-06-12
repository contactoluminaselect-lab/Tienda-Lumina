import os
import json
import random
import time

class LuminaProAutomator:
    def __init__(self):
        self.filename = 'productos.json'
        # BANCO DE IMÁGENES PREMIUM (Links directos de Unsplash que NUNCA fallan)
        self.premium_pool = {
            "Tecnología": [
                {"n": "Smartwatch V3 Diamond", "p": 125, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800"},
                {"n": "Cámara Mirrorless Pro", "p": 850, "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=800"},
                {"n": "Teclado Mecánico Zen", "p": 145, "img": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?q=80&w=800"}
            ],
            "Hogar": [
                {"n": "Lámpara Orbital Minimal", "p": 89, "img": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?q=80&w=800"},
                {"n": "Prensa Francesa Cobre", "p": 45, "img": "https://images.unsplash.com/photo-1544190153-060cb6277f67?q=80&w=800"},
                {"n": "Silla Nórdica Ergo", "p": 210, "img": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?q=80&w=800"}
            ],
            "Jardinería": [
                {"n": "Kit Botánico de Acero", "p": 75, "img": "https://images.unsplash.com/photo-1617576621334-4291ef387ae4?q=80&w=800"},
                {"n": "Maceta Inteligente WiFi", "p": 35, "img": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=800"}
            ],
            "Belleza": [
                {"n": "Rodillo de Jade Puro", "p": 25, "img": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?q=80&w=800"},
                {"n": "Set de Cuidado Orgánico", "p": 55, "img": "https://images.unsplash.com/photo-1556228720-195a672e8a03?q=80&w=800"}
            ]
        }

    def run(self):
        # 1. Cargar inventario actual
        try:
            with open(self.filename, 'r') as f: products = json.load(f)
        except: products = []

        # 2. Seleccionar categoría y producto al azar del banco de confianza
        cat = random.choice(list(self.premium_pool.keys()))
        item = random.choice(self.premium_pool[cat])

        # Evitar duplicados exactos
        if not any(p['nombre'] == item['n'] for p in products):
            new_prod = {
                "id": "LUM-" + str(random.randint(100, 999)),
                "nombre": item["n"],
                "precio": item["p"],
                "categoria": cat,
                "descripcion": "Excelencia y diseño para su vida cotidiana. Calidad garantizada.",
                "imagen": item["img"],
                "timestamp": str(time.time()),
                "resenas": [
                    {"usuario": "M. Valdés", "estrellas": 5, "comentario": "Increíble diseño."},
                    {"usuario": "Cliente Lumina", "estrellas": 5, "comentario": "Calidad inmejorable."}
                ]
            }
            products.append(new_prod)
            # Mantener catálogo fresco (últimos 15)
            if len(products) > 15: products = products[-15:]

            with open(self.filename, 'w') as f:
                json.dump(products, f, indent=4)
            print(f"Producto publicado: {item['n']}")
        else:
            print("El producto ya existe.")

if __name__ == "__main__":
    LuminaProAutomator().run()
