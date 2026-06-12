import os
import json
import random
import requests
import time

# --- CONFIGURACIÓN DE LLAVES (SE SAKAN DE GITHUB SECRETS) ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CJ_API_KEY = os.getenv("CJ_API_KEY")

class LuminaUltraAutomator:
    def __init__(self):
        self.filename = 'productos.json'

    def get_real_product_from_cj(self):
        """Busca productos reales en el catálogo de CJ Dropshipping"""
        print("Conectando con CJ Dropshipping API...")
        
        # Si no hay API Key de CJ, usamos una lista de respaldo de alta calidad
        if not CJ_API_KEY:
            return self.get_fallback_product()

        url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"
        headers = {"CJ-Access-Token": CJ_API_KEY}
        params = {"pageSize": 50, "categoryName": random.choice(["Electronic", "Home", "Jewelry"])}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            data = response.json()
            if data['code'] == 200 and data['data']['list']:
                raw_prod = random.choice(data['data']['list'])
                return {
                    "id": raw_prod['productSku'],
                    "nombre": raw_prod['productName'],
                    "precio": float(raw_prod['sellPrice']) * 2.5, # Margen de ganancia
                    "categoria": raw_prod['categoryName'],
                    "descripcion": "Producto de alta gama seleccionado por nuestra IA.",
                    "imagen": raw_prod['productImage']
                }
        except:
            return self.get_fallback_product()

    def beautify_with_ai(self, product):
        """Usa OpenAI para que el nombre y la descripción suenen a marca de lujo"""
        if not OPENAI_API_KEY:
            return product

        print(f"Mejorando '{product['nombre']}' con Inteligencia Artificial...")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
        
        prompt = f"Eres el redactor de una tienda de lujo llamada Lumina Select. Transforma este producto: Nombre: {product['nombre']}. Crea un nombre corto y elegante, y una descripción sofisticada. Responde SOLO un JSON con: nombre, descripcion."

        try:
            resp = requests.post(url, headers=headers, json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }).json()
            
            ai_data = json.loads(resp['choices'][0]['message']['content'])
            product['nombre'] = ai_data['nombre']
            product['descripcion'] = ai_data['descripcion']
            return product
        except:
            return product

    def get_fallback_product(self):
        """Productos de respaldo con imágenes HD que nunca fallan si la API falla"""
        items = [
            {"id": "CJ-WATCH-99", "nombre": "Reloj Minimalista", "categoria": "Tecnología", "precio": 150.0, "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800"},
            {"id": "CJ-LAMP-88", "nombre": "Lámpara Orbital", "categoria": "Hogar", "precio": 89.0, "imagen": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800"},
            {"id": "CJ-BAG-77", "nombre": "Bolso de Cuero Curado", "categoria": "Accesorios", "precio": 210.0, "imagen": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800"}
        ]
        return random.choice(items)

    def run(self):
        # 1. Cargar inventario actual
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try: products = json.load(f)
                except: products = []
        else:
            products = []

        # 2. Obtener y mejorar producto
        new_item = self.get_real_product_from_cj()
        new_item = self.beautify_with_ai(new_item)
        
        # 3. Añadir reseñas
        new_item["resenas"] = [
            {"usuario": "M. Valdés", "estrellas": 5, "comentario": "Una pieza excepcional, muy recomendada."},
            {"usuario": "Lumina Client", "estrellas": 5, "comentario": "Calidad premium en cada detalle."}
        ]
        new_item["timestamp"] = time.time()

        # 4. Evitar duplicados y guardar
        if not any(p['id'] == new_item['id'] for p in products):
            products.append(new_item)
            # Mantener máximo 15 productos para que la web vuele
            if len(products) > 15: products = products[-15:]
            
            with open(self.filename, 'w') as f:
                json.dump(products, f, indent=4)
            print(f"PRODUCTO PUBLICADO: {new_item['nombre']}")
        else:
            print("El producto ya existe en el catálogo.")

if __name__ == "__main__":
    LuminaUltraAutomator().run()
