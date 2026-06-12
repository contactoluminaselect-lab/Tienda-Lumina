import os
import json
import random
import requests

# --- CONFIGURACIÓN ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LuminaAutomator:
    def get_new_products_from_ai(self):
        """Le pide a la IA que elija un producto tendencia para hoy"""
        print("Consultando tendencias con IA...")
        
        # Lista de categorías para rotar
        categorias = ["Tecnología", "Hogar", "Jardinería"]
        cat = random.choice(categorias)
        
        # En una versión real aquí llamaríamos a OpenAI para buscar en CJ
        # Por ahora, simulamos que la IA elige uno de una base de datos rotativa
        base_datos = [
            {"id": "CJ_TAB_01", "n": "Tablet Ultra Slim 2026", "p": 299, "c": "Tecnología", "d": "Potencia aeroespacial en tu bolsillo."},
            {"id": "CJ_LAMP_02", "n": "Lámpara de Gravedad Cero", "p": 125, "c": "Hogar", "d": "Iluminación que desafía la física."},
            {"id": "CJ_GARD_03", "n": "Set de Cultivo Inteligente", "p": 85, "c": "Jardinería", "d": "Tu jardín cuidado por sensores de precisión."},
            {"id": "CJ_WATCH_04", "n": "Reloj de Cristal Líquido", "p": 150, "c": "Tecnología", "d": "La elegancia del futuro en tu muñeca."}
        ]
        
        # Elegimos 2 productos al azar para que el archivo siempre cambie
        seleccion = random.sample(base_datos, 2)
        
        productos_finales = []
        for item in seleccion:
            productos_finales.append({
                "id": item["id"],
                "nombre": item["n"],
                "precio": item["p"],
                "categoria": item["c"],
                "descripcion": item["d"],
                "imagen": f"https://images.unsplash.com/photo-{random.randint(1500000, 1600000)}?w=500",
                "resenas": [
                    {"usuario": "Cliente VIP", "estrellas": 5, "comentario": "Increíble selección, calidad insuperable."},
                    {"usuario": "Lumina User", "estrellas": 5, "comentario": "El envío fue rapidísimo. Muy profesional."}
                ]
            })
        return productos_finales

    def update_store(self):
        nuevos = self.get_new_products_from_ai()
        
        with open('productos.json', 'w') as f:
            json.dump(nuevos, f, indent=4)
        
        print("¡Archivo productos.json actualizado con éxito!")

if __name__ == "__main__":
    bot = LuminaAutomator()
    bot.update_store()
