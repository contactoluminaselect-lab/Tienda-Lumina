import os
import json
import random
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class UnlimitedAutomator:
    def generate_ai_product(self):
        """Usa GPT-4 para inventar un producto tendencia y una categoría"""
        print("Consultando tendencias globales con IA...")
        
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = """Inventa un producto de dropshipping de lujo. 
        Responde SOLO en formato JSON puro con estos campos: 
        id (inventado), nombre, precio, categoria (inventa una como Fitness, Mascotas, Oficina, etc), 
        descripcion (vendedora y corta), imagen (un término de búsqueda para Unsplash)."""

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.8
        }

        try:
            response = requests.post(url, headers=headers, json=data).json()
            product_raw = json.loads(response['choices'][0]['message']['content'])
            
            # Limpiar la imagen para que sea un link real de Unsplash
            keyword = product_raw['imagen'].replace(" ", "+")
            product_raw['imagen'] = f"https://source.unsplash.com/featured/800x1000/?{keyword},{random.randint(1,1000)}"
            
            return product_raw
        except Exception as e:
            print(f"Error con IA: {e}")
            return None

    def run(self):
        filename = 'productos.json'
        
        # Cargar existentes
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try: products = json.load(f)
                except: products = []
        else:
            products = []

        # Generar 1 nuevo
        new_item = self.generate_ai_product()
        if new_item:
            # Evitar duplicados por nombre
            if not any(p['nombre'] == new_item['nombre'] for p in products):
                products.append(new_item)
                print(f"Añadido: {new_item['nombre']} en la categoría {new_item['categoria']}")

        # Guardar
        with open(filename, 'w') as f:
            json.dump(products, f, indent=4)

if __name__ == "__main__":
    if OPENAI_API_KEY:
        UnlimitedAutomator().run()
    else:
        print("Falta OPENAI_API_KEY en los Secrets.")
