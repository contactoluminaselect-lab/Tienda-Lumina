import os
import json
import random
import time

class LuminaAutomator:
    def run(self):
        filename = 'productos.json'
        
        # Productos base con imágenes estables
        pool = [
            {"id": "A1", "nombre": "Reloj Minimalista", "categoria": "Tecnología", "precio": 150, "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"},
            {"id": "A2", "nombre": "Lámpara Zen", "categoria": "Hogar", "precio": 85, "imagen": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800"},
            {"id": "A3", "nombre": "Cámara Vintage", "categoria": "Tecnología", "precio": 210, "imagen": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800"},
            {"id": "A4", "nombre": "Silla Nórdica", "categoria": "Hogar", "precio": 120, "imagen": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800"}
        ]
        
        # Seleccionar 3 al azar
        selected = random.sample(pool, 3)
        
        # AGREGAR MARCA DE TIEMPO (Para forzar a GitHub a ver un cambio)
        for p in selected:
            p['timestamp'] = str(time.time())

        with open(filename, 'w') as f:
            json.dump(selected, f, indent=4)
        print("Archivo productos.json generado con éxito.")

if __name__ == "__main__":
    LuminaAutomator().run()
