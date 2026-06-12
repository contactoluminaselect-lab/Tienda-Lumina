import os
import json
import random
import requests
import time

# --- CONFIGURACIÓN DE LLAVES ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LuminaUltraAutomator:
    def __init__(self):
        self.filename = 'productos.json'
        # PLAN B: Catálogo de respaldo con imágenes HD verificadas (Unsplash)
        self.fallback_db = [
            {"nombre": "Reloj de Titanio Minimalista", "categoria": "Tecnología", "precio": 199.0, "img": "minimalist+watch"},
            {"nombre": "Lámpara de Levitación Magnética", "categoria": "Hogar", "precio": 145.0, "img": "levitating+lamp"},
            {"nombre": "Set de Café Prensa Francesa Pro", "categoria": "Hogar", "precio": 55.0, "img": "french+press"},
            {"nombre": "Cámara Mirrorless Retro", "categoria": "Tecnología", "precio": 850.0, "img": "retro+camera"},
            {"nombre": "Humidificador de Niebla Fría", "categoria": "Hogar", "precio": 45.0, "img": "humidifier"},
            {"nombre": "Auriculares Noise Cancelling", "categoria": "Tecnología", "precio": 299.0, "img": "headphones"},
            {"nombre": "Set de Jardinería de Acero", "categoria": "Jardinería", "precio": 75.0, "img": "garden+tools"},
            {"nombre": "Maceta Inteligente WiFi", "categoria": "Jardinería", "precio": 35.0, "img": "smart+plant+pot"}
        ]

    def get_ai_product(self):
        """Intenta generar un producto con OpenAI, si falla usa el Fallback"""
        if not OPENAI_API_KEY:
            print("No se detectó OPENAI_API_KEY. Usando catálogo interno...")
            return self.get_fallback_product()

        print("Consultando tendencias globales con OpenAI...")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
        
        prompt = "Crea un producto de dropshipping de lujo. Responde SOLO un objeto JSON con: id, nombre, precio (numero), categoria, descripcion, imagen (1 palabra en ingles)."

        try:
            response = requests.post(url, headers=headers, json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.8
            }, timeout=10)
            
            res_json = response.json()
            content = res_json['choices'][0]['message']['content']
            product = json.loads(content)
            
            # Formatear imagen con Unsplash
            keyword = product['imagen'].replace(" ", "")
            product['imagen'] = f"https://source.unsplash.com/featured/800x1000?{keyword}"
            return product
        except Exception as e:
            print(f"Error con OpenAI ({e}). Usando catálogo interno...")
            return self.get_fallback_product()

    def get_fallback_product(self):
        """Selecciona un producto del catálogo interno de seguridad"""
        item = random.choice(self.fallback_db)
        return {
            "id": "LUM-" + str(random.randint(1000, 9999)),
            "nombre": item["nombre"],
            "precio": item["precio"],
            "categoria": item["categoria"],
            "descripcion": "Una pieza de curaduría exclusiva seleccionada por Lumina Select para elevar su estilo de vida.",
            "imagen": f"https://source.unsplash.com/featured/800x1000?{item['img']}"
        }

    def run(self):
        # 1. Cargar productos actuales
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    products = json.load(f)
                except:
                    products = []
        else:
            products = []

        # 2. Generar el nuevo producto
        new_item = self.get_ai_product()
        
        # 3. Añadir reseñas automáticas
        new_item["resenas"] = [
            {"usuario": "Cliente Verificado", "estrellas": 5, "comentario": "Excelente calidad y diseño."},
            {"usuario": "Lumina VIP", "estrellas": 5, "comentario": "Superó mis expectativas totalmente."}
        ]
        
        # 4. Forzar cambio con marca de tiempo (Evita que GitHub ignore el archivo)
        new_item["updated_at"] = str(time.time())
        
        # 5. Añadir a la lista y mantener solo los últimos 12 para que la web cargue rápido
        products.append(new_item)
        if len(products) > 12:
            products = products[-12:]

        # 6. Guardar archivo
        with open(self.filename, 'w') as f:
            json.dump(products, f, indent=4)
        
        print(f"ÉXITO: Se ha añadido '{new_item['nombre']}' a la tienda.")

if __name__ == "__main__":
    bot = LuminaUltraAutomator()
    bot.run()
