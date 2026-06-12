import os
import json
import random
import requests
import time

# --- CONFIGURACIÓN DE IA ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LuminaInfiniteAutomator:
    def __init__(self):
        self.filename = 'productos.json'
        # Categorías en las que la IA puede buscar
        self.categorias = ["Tecnología de Lujo", "Hogar Minimalista", "Jardinería Zen", "Belleza Premium", "Accesorios de Viaje"]

    def generate_product_with_ai(self):
        """Usa OpenAI para crear un producto único que no existe en la tienda"""
        if not OPENAI_API_KEY:
            return None

        print("Generando producto único con Inteligencia Artificial...")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
        
        cat = random.choice(self.categorias)
        prompt = f"Inventa un producto premium de dropshipping para la categoría '{cat}'. Responde SOLO un objeto JSON con: id (inventado), nombre, precio (entre 50 y 500), categoria, descripcion (elegante), imagen_keyword (1 palabra en ingles para buscar una foto)."

        try:
            response = requests.post(url, headers=headers, json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.9
            }, timeout=15).json()
            
            content = response['choices'][0]['message']['content']
            product = json.loads(content)
            
            # Buscamos una imagen real en Unsplash basada en la palabra clave de la IA
            keyword = product.get('imagen_keyword', 'luxury').replace(" ", "")
            # Usamos un ID aleatorio para que la foto cambie siempre
            rand_id = random.randint(1, 1000)
            product['imagen'] = f"https://images.unsplash.com/photo-{1500000000000 + rand_id}?w=800&auto=format&fit=crop"
            
            # Sistema de respaldo de imágenes si la IA no da buena palabra clave
            img_map = {
                "Tecnología": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800",
                "Hogar": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800",
                "Jardinería": "https://images.unsplash.com/photo-1617576621334-4291ef387ae4?w=800",
                "Belleza": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?w=800"
            }
            # Si el link generado es inestable, usamos uno de alta calidad
            for c in img_map:
                if c in product['categoria']:
                    product['imagen'] = img_map[c]

            return product
        except Exception as e:
            print(f"Error generando producto: {e}")
            return None

    def run(self):
        # 1. Cargar lo que ya existe
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try: products = json.load(f)
                except: products = []
        else:
            products = []

        # 2. Generar un producto nuevo
        new_item = self.generate_product_with_ai()
        
        if new_item:
            # 3. Evitar duplicados por nombre
            if not any(p['nombre'] == new_item['nombre'] for p in products):
                new_item['updated'] = str(time.time())
                products.append(new_item)
                
                # 4. Establecer un límite sano de 50 productos para que la web no pese mucho
                if len(products) > 50:
                    products = products[-50:]
                
                with open(self.filename, 'w') as f:
                    json.dump(products, f, indent=4)
                print(f"Añadido con éxito: {new_item['nombre']}")
        else:
            print("No se pudo generar un producto nuevo en este ciclo.")

if __name__ == "__main__":
    LuminaInfiniteAutomator().run()
