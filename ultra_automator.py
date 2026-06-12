import os
import json
import random

class LuminaMasterAutomator:
    def get_all_categories_products(self):
        print("Sincronizando catálogo global multicategoría...")
        
        # Base de datos maestra por categorías
        db = {
            "Tecnología": [
                {"id": "TECH_01", "nombre": "Teclado Mecánico Retro", "precio": 120.0, "desc": "Estética vintage con switches profesionales. Iluminación ámbar.", "img": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=800"},
                {"id": "TECH_02", "nombre": "Cámara de Seguridad 360", "precio": 85.0, "desc": "Visión nocturna y seguimiento por IA. Control total desde su smartphone.", "img": "https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?w=800"}
            ],
            "Hogar": [
                {"id": "HOME_01", "nombre": "Prensa Francesa de Cobre", "precio": 45.0, "desc": "Doble pared de aislamiento. El café perfecto con un diseño icónico.", "img": "https://images.unsplash.com/photo-1544190153-060cb6277f67?w=800"},
                {"id": "HOME_02", "nombre": "Humidificador Ultrasónico", "precio": 55.0, "desc": "Silencioso y elegante. Mejora la calidad del aire con estilo.", "img": "https://images.unsplash.com/photo-1585671962215-4733ff0ad011?w=800"}
            ],
            "Jardinería": [
                {"id": "GARD_01", "nombre": "Set de Herramientas Minimalista", "precio": 65.0, "desc": "Acero inoxidable pulido y mangos de fresno. Durabilidad eterna.", "img": "https://images.unsplash.com/photo-1617576621334-4291ef387ae4?w=800"},
                {"id": "GARD_02", "nombre": "Maceta de Auto-riego", "precio": 30.0, "desc": "Tecnología capilar para que sus plantas siempre tengan agua.", "img": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800"}
            ],
            "Belleza": [
                {"id": "BEAUTY_01", "nombre": "Rodillo de Jade Premium", "precio": 25.0, "desc": "Piedra auténtica para masaje facial. Reduce la inflamación al instante.", "img": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=800"},
                {"id": "BEAUTY_02", "nombre": "Set de Brochas Pro", "precio": 40.0, "desc": "Fibras sintéticas de alta gama. Acabado profesional en cada aplicación.", "img": "https://images.unsplash.com/photo-1522338242992-e1a54906a8da?w=800"}
            ]
        }
        
        # El robot selecciona 2 categorías al azar y 1 producto de cada una
        cats_elegidas = random.sample(list(db.keys()), 3)
        productos_hoy = []
        
        for cat in cats_elegidas:
            prod = random.choice(db[cat])
            # Añadimos reseñas dinámicas
            prod["resenas"] = [
                {"usuario": "Cliente Verificado", "estrellas": 5, "comentario": "Excelente producto, la calidad de Lumina Select se nota."},
                {"usuario": "User Premium", "estrellas": 5, "comentario": "Llegó muy bien empaquetado y funciona de maravilla."}
            ]
            productos_hoy.append(prod)
            
        return productos_hoy

    def update_store(self):
        nuevos_productos = self.get_all_categories_products()
        with open('productos.json', 'w') as f:
            json.dump(nuevos_productos, f, indent=4)
        print("¡Tienda Global actualizada! Categorías y Fotos sincronizadas.")

if __name__ == "__main__":
    bot = LuminaMasterAutomator()
    bot.update_store()
