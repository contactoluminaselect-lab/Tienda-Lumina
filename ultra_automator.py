import os
import json
import random

class LuminaPersistenceAutomator:
    def __init__(self):
        # Base de datos maestra con imágenes verificadas
        self.master_db = {
            "Tecnología": [
                {"id": "TECH_01", "nombre": "Teclado Mecánico Retro", "precio": 125.0, "categoria": "Tecnología", "descripcion": "Estética vintage con switches profesionales.", "imagen": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=800"},
                {"id": "TECH_02", "nombre": "Cámara de Seguridad 360", "precio": 89.0, "categoria": "Tecnología", "descripcion": "Visión nocturna y seguimiento por IA.", "imagen": "https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?w=800"},
                {"id": "TECH_03", "nombre": "Auriculares de Madera", "precio": 199.0, "categoria": "Tecnología", "descripcion": "Acústica natural y diseño premium.", "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800"}
            ],
            "Hogar": [
                {"id": "HOME_01", "nombre": "Prensa Francesa Oro", "precio": 45.0, "categoria": "Hogar", "descripcion": "Acero inoxidable con acabado en oro rosa.", "imagen": "https://images.unsplash.com/photo-1544190153-060cb6277f67?w=800"},
                {"id": "HOME_02", "nombre": "Lámpara Minimalista", "precio": 75.0, "categoria": "Hogar", "descripcion": "Luz cálida regulable para ambientes modernos.", "imagen": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800"}
            ],
            "Jardinería": [
                {"id": "GARD_01", "nombre": "Kit Botánico de Acero", "precio": 65.0, "categoria": "Jardinería", "descripcion": "Herramientas de grado profesional.", "imagen": "https://images.unsplash.com/photo-1617576621334-4291ef387ae4?w=800"}
            ],
            "Belleza": [
                {"id": "BEA_01", "nombre": "Set de Cuidado Facial", "precio": 55.0, "categoria": "Belleza", "descripcion": "Extractos orgánicos para una piel radiante.", "imagen": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800"}
            ]
        }

    def update_json(self):
        filename = 'productos.json'
        
        # 1. Intentar leer productos existentes
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    current_products = json.load(f)
                except:
                    current_products = []
        else:
            current_products = []

        # 2. Elegir un producto nuevo al azar de la DB que NO esté ya en la web
        all_ids = [p['id'] for p in current_products]
        available_categories = list(self.master_db.keys())
        
        # Intentar buscar uno nuevo
        new_prod = None
        for _ in range(10): # 10 intentos para encontrar uno no repetido
            cat = random.choice(available_categories)
            candidate = random.choice(self.master_db[cat])
            if candidate['id'] not in all_ids:
                new_prod = candidate
                break
        
        if new_prod:
            # Añadir reseñas ficticias
            new_prod["resenas"] = [
                {"usuario": "M. Torres", "estrellas": 5, "comentario": "Impresionante calidad."},
                {"usuario": "Lumina Fan", "estrellas": 5, "comentario": "El diseño es de otro nivel."}
            ]
            current_products.append(new_prod)
            print(f"Añadido nuevo producto: {new_prod['nombre']}")
        else:
            print("No hay productos nuevos para añadir hoy.")

        # 3. Guardar la lista actualizada (acumulativa)
        with open(filename, 'w') as f:
            json.dump(current_products, f, indent=4)

if __name__ == "__main__":
    bot = LuminaPersistenceAutomator()
    bot.update_json()
