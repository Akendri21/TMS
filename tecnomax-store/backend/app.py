from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir frontend local

DATA_FILE = 'productos.json'

def load_productos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_productos(productos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=2, ensure_ascii=False)

# Inicializar con 60 productos si no existe
productos_iniciales = [
    # MÓVILES (10)
    {"id": "MOV1", "nombre": "iPhone 15 Pro Max", "categoria": "Móvil", "precio": 90930, "imagen": "https://images.unsplash.com/photo-1695048133142-1a20484d2568?w=200&h=200&fit=crop", "descripcion": "Apple A17 Pro, 256GB, Titanio azul"},
    {"id": "MOV2", "nombre": "Samsung Galaxy S24 Ultra", "categoria": "Móvil", "precio": 83930, "imagen": "https://images.unsplash.com/photo-1706854575454-95e5e566d6c6?w=200&h=200&fit=crop", "descripcion": "Pantalla Dynamic AMOLED 2X, 512GB, S Pen"},
    {"id": "MOV3", "nombre": "Xiaomi 14 Pro", "categoria": "Móvil", "precio": 62930, "imagen": "https://images.unsplash.com/photo-1707234482698-2e2c4e1b3e7a?w=200&h=200&fit=crop", "descripcion": "Leica Summilux, Snapdragon 8 Gen 3"},
    {"id": "MOV4", "nombre": "Google Pixel 8 Pro", "categoria": "Móvil", "precio": 69930, "imagen": "https://images.unsplash.com/photo-1696426065168-5f2f0e6a7b0b?w=200&h=200&fit=crop", "descripcion": "Cámara con IA, Android 14, 128GB"},
    {"id": "MOV5", "nombre": "OnePlus 12", "categoria": "Móvil", "precio": 59430, "imagen": "https://images.unsplash.com/photo-1706049392767-1f9f1e1a1b1b?w=200&h=200&fit=crop", "descripcion": "Hasselblad, 16GB RAM, 256GB"},
    {"id": "MOV6", "nombre": "Motorola Edge 40 Pro", "categoria": "Móvil", "precio": 55930, "imagen": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=200&h=200&fit=crop", "descripcion": "Pantalla pOLED 165Hz, 125W carga"},
    {"id": "MOV7", "nombre": "Sony Xperia 1 V", "categoria": "Móvil", "precio": 83930, "imagen": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=200&h=200&fit=crop", "descripcion": "Pantalla 4K HDR, cámara profesional"},
    {"id": "MOV8", "nombre": "Nothing Phone (2)", "categoria": "Móvil", "precio": 48930, "imagen": "https://images.unsplash.com/photo-1678912348975-3d4c5b1a5b1a?w=200&h=200&fit=crop", "descripcion": "Glyph Interface, Snapdragon 8+"},
    {"id": "MOV9", "nombre": "Realme GT 5 Pro", "categoria": "Móvil", "precio": 52430, "imagen": "https://images.unsplash.com/photo-1686943976712-7e5b8f7b2c1a?w=200&h=200&fit=crop", "descripcion": "Carga 240W, cámara periscopio"},
    {"id": "MOV10", "nombre": "Huawei P60 Pro", "categoria": "Móvil", "precio": 76930, "imagen": "https://images.unsplash.com/photo-1686943976812-5f8b1f3b1c2a?w=200&h=200&fit=crop", "descripcion": "Cámara XMAGE, HarmonyOS"},
    # TVs (10)
    {"id": "TV1", "nombre": "LG OLED C3 65\"", "categoria": "TV", "precio": 139930, "imagen": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=200&h=200&fit=crop", "descripcion": "OLED evo, 4K, 120Hz, Smart TV"},
    {"id": "TV2", "nombre": "Samsung QLED Q80C 55\"", "categoria": "TV", "precio": 90930, "imagen": "https://images.unsplash.com/photo-1601944179066-29786cb9d32a?w=200&h=200&fit=crop", "descripcion": "Quantum HDR, 4K, 120Hz"},
    {"id": "TV3", "nombre": "Sony Bravia XR A80L 55\"", "categoria": "TV", "precio": 104930, "imagen": "https://images.unsplash.com/photo-1612428970260-2f7b0a1c3c0b?w=200&h=200&fit=crop", "descripcion": "OLED, Cognitive Processor XR, Google TV"},
    {"id": "TV4", "nombre": "Panasonic TX-65MZ980", "categoria": "TV", "precio": 125930, "imagen": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d6?w=200&h=200&fit=crop", "descripcion": "OLED 4K, HDR10+, Dolby Atmos"},
    {"id": "TV5", "nombre": "Philips OLED+908 55\"", "categoria": "TV", "precio": 153930, "imagen": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=200&h=200&fit=crop", "descripcion": "Ambilight, 4K, 120Hz, 5ª Gen P5"},
    {"id": "TV6", "nombre": "TCL C845 65\"", "categoria": "TV", "precio": 69930, "imagen": "https://images.unsplash.com/photo-1601944179066-29786cb9d32a?w=200&h=200&fit=crop", "descripcion": "QLED Mini-LED, 4K, 144Hz"},
    {"id": "TV7", "nombre": "Hisense U8K 55\"", "categoria": "TV", "precio": 62930, "imagen": "https://images.unsplash.com/photo-1612428970260-2f7b0a1c3c0b?w=200&h=200&fit=crop", "descripcion": "Mini-LED, 4K, 144Hz, Dolby Vision"},
    {"id": "TV8", "nombre": "Xiaomi TV Q2 55\"", "categoria": "TV", "precio": 41930, "imagen": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d6?w=200&h=200&fit=crop", "descripcion": "QLED, 4K, Google TV, 60Hz"},
    {"id": "TV9", "nombre": "Sharp 4T-C65GN1X", "categoria": "TV", "precio": 59430, "imagen": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=200&h=200&fit=crop", "descripcion": "4K, Android TV, HDR10"},
    {"id": "TV10", "nombre": "Vizio MQX 50\"", "categoria": "TV", "precio": 48930, "imagen": "https://images.unsplash.com/photo-1601944179066-29786cb9d32a?w=200&h=200&fit=crop", "descripcion": "QLED, 4K, 120Hz, SmartCast"},
    # CONSOLAS (10)
    {"id": "CON1", "nombre": "Sony PlayStation 5", "categoria": "Consola", "precio": 38430, "imagen": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=200&h=200&fit=crop", "descripcion": "PS5 estándar, 825GB SSD, mando DualSense"},
    {"id": "CON2", "nombre": "Xbox Series X", "categoria": "Consola", "precio": 38430, "imagen": "https://images.unsplash.com/photo-1621259182978-fbf931c6d5b3?w=200&h=200&fit=crop", "descripcion": "1TB SSD, 4K, 120Hz, Game Pass"},
    {"id": "CON3", "nombre": "Nintendo Switch OLED", "categoria": "Consola", "precio": 24430, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "Pantalla OLED 7\", 64GB, Joy-Con"},
    {"id": "CON4", "nombre": "Steam Deck 512GB", "categoria": "Consola", "precio": 45430, "imagen": "https://images.unsplash.com/photo-1678912348975-3d4c5b1a5b1a?w=200&h=200&fit=crop", "descripcion": "PC portátil, 512GB NVMe, APU AMD"},
    {"id": "CON5", "nombre": "PlayStation 5 Digital", "categoria": "Consola", "precio": 31430, "imagen": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=200&h=200&fit=crop", "descripcion": "Edición digital, 825GB SSD"},
    {"id": "CON6", "nombre": "Xbox Series S", "categoria": "Consola", "precio": 20930, "imagen": "https://images.unsplash.com/photo-1621259182978-fbf931c6d5b3?w=200&h=200&fit=crop", "descripcion": "512GB SSD, digital, 1440p"},
    {"id": "CON7", "nombre": "Nintendo Switch Lite", "categoria": "Consola", "precio": 13930, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "Portátil, 32GB, azul"},
    {"id": "CON8", "nombre": "ASUS ROG Ally", "categoria": "Consola", "precio": 48930, "imagen": "https://images.unsplash.com/photo-1678912342350-5d9d9c5c4c7a?w=200&h=200&fit=crop", "descripcion": "PC portátil gaming, Z1 Extreme"},
    {"id": "CON9", "nombre": "Logitech G Cloud", "categoria": "Consola", "precio": 20930, "imagen": "https://images.unsplash.com/photo-1678912342350-5d9d9c5c4c7a?w=200&h=200&fit=crop", "descripcion": "Cloud gaming, Android, 7\""},
    {"id": "CON10", "nombre": "Atari VCS", "categoria": "Consola", "precio": 17430, "imagen": "https://images.unsplash.com/photo-1678912342350-5d9d9c5c4c7a?w=200&h=200&fit=crop", "descripcion": "Clásica, 500GB, juegos retro"},
    # VIDEOJUEGOS (10)
    {"id": "VID1", "nombre": "The Legend of Zelda: Tears of the Kingdom", "categoria": "Videojuego", "precio": 4830, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "Nintendo Switch, Aventura"},
    {"id": "VID2", "nombre": "FIFA 24", "categoria": "Videojuego", "precio": 4130, "imagen": "https://images.unsplash.com/photo-1625805866449-5f7c8c7b8b1b?w=200&h=200&fit=crop", "descripcion": "PS5/Xbox/PC, Fútbol"},
    {"id": "VID3", "nombre": "God of War Ragnarök", "categoria": "Videojuego", "precio": 4830, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "PS5, Acción/Aventura"},
    {"id": "VID4", "nombre": "Call of Duty: Modern Warfare III", "categoria": "Videojuego", "precio": 4830, "imagen": "https://images.unsplash.com/photo-1625805866449-5f7c8c7b8b1b?w=200&h=200&fit=crop", "descripcion": "PS5/Xbox/PC, FPS"},
    {"id": "VID5", "nombre": "Spider-Man 2", "categoria": "Videojuego", "precio": 4830, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "PS5, Mundo abierto"},
    {"id": "VID6", "nombre": "Mario Kart 8 Deluxe", "categoria": "Videojuego", "precio": 3430, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "Nintendo Switch, Carreras"},
    {"id": "VID7", "nombre": "Elden Ring", "categoria": "Videojuego", "precio": 4130, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "PS5/Xbox/PC, RPG"},
    {"id": "VID8", "nombre": "Minecraft", "categoria": "Videojuego", "precio": 2030, "imagen": "https://images.unsplash.com/photo-1625805866449-5f7c8c7b8b1b?w=200&h=200&fit=crop", "descripcion": "Multiplataforma, Construcción"},
    {"id": "VID9", "nombre": "Fortnite", "categoria": "Videojuego", "precio": 0, "imagen": "https://images.unsplash.com/photo-1625805866449-5f7c8c7b8b1b?w=200&h=200&fit=crop", "descripcion": "Gratuito, Battle Royale"},
    {"id": "VID10", "nombre": "Grand Theft Auto V", "categoria": "Videojuego", "precio": 2730, "imagen": "https://images.unsplash.com/photo-1618332676613-f5f7f5e5c5b2?w=200&h=200&fit=crop", "descripcion": "PS5/Xbox/PC, Acción"},
    # PCs (10)
    {"id": "PC1", "nombre": "Alienware Aurora R16", "categoria": "PC", "precio": 174930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "Intel i9, RTX 4090, 32GB RAM"},
    {"id": "PC2", "nombre": "HP Omen 45L", "categoria": "PC", "precio": 153930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i7, RTX 4080, 32GB RAM, 1TB SSD"},
    {"id": "PC3", "nombre": "Lenovo Legion Tower 7i", "categoria": "PC", "precio": 139930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i7, RTX 4070 Ti, 16GB RAM"},
    {"id": "PC4", "nombre": "ASUS ROG Strix GA35", "categoria": "PC", "precio": 195930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "Ryzen 9, RTX 4090, 64GB RAM"},
    {"id": "PC5", "nombre": "MSI Trident X", "categoria": "PC", "precio": 132930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i7, RTX 4070, 16GB RAM"},
    {"id": "PC6", "nombre": "Acer Predator Orion 3000", "categoria": "PC", "precio": 90930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i5, RTX 3060, 16GB RAM"},
    {"id": "PC7", "nombre": "Corsair Vengeance i7400", "categoria": "PC", "precio": 160930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i9, RTX 4080, 32GB RAM"},
    {"id": "PC8", "nombre": "Razer Tomahawk", "categoria": "PC", "precio": 181930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i9, RTX 4090, 32GB RAM"},
    {"id": "PC9", "nombre": "Origin PC Millennium", "categoria": "PC", "precio": 230930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "Ryzen 9, RTX 4090, 64GB RAM"},
    {"id": "PC10", "nombre": "Dell XPS Desktop", "categoria": "PC", "precio": 104930, "imagen": "https://images.unsplash.com/photo-1603487742131-4160ec2b4a8c?w=200&h=200&fit=crop", "descripcion": "i7, RTX 3060, 16GB RAM"},
    # LAPTOPS (10)
    {"id": "LAP1", "nombre": "MacBook Pro 16\" M3", "categoria": "Laptop", "precio": 174930, "imagen": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=200&h=200&fit=crop", "descripcion": "M3 Max, 48GB RAM, 1TB SSD"},
    {"id": "LAP2", "nombre": "Dell XPS 15", "categoria": "Laptop", "precio": 132930, "imagen": "https://images.unsplash.com/photo-1593642634367-d91a135587b5?w=200&h=200&fit=crop", "descripcion": "Intel i9, RTX 4060, 32GB RAM"},
    {"id": "LAP3", "nombre": "HP Spectre x360 14\"", "categoria": "Laptop", "precio": 104930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i7, 16GB RAM, 1TB SSD, OLED"},
    {"id": "LAP4", "nombre": "Lenovo ThinkPad X1 Carbon", "categoria": "Laptop", "precio": 125930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i7, 16GB RAM, 512GB SSD"},
    {"id": "LAP5", "nombre": "ASUS ROG Zephyrus G14", "categoria": "Laptop", "precio": 111930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "Ryzen 9, RTX 4060, 16GB RAM"},
    {"id": "LAP6", "nombre": "Acer Swift 3", "categoria": "Laptop", "precio": 48930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "Ryzen 5, 8GB RAM, 512GB SSD"},
    {"id": "LAP7", "nombre": "Microsoft Surface Laptop 5", "categoria": "Laptop", "precio": 90930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i5, 16GB RAM, 256GB SSD"},
    {"id": "LAP8", "nombre": "Razer Blade 15", "categoria": "Laptop", "precio": 160930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i7, RTX 4070, 16GB RAM"},
    {"id": "LAP9", "nombre": "Gigabyte Aorus 17", "categoria": "Laptop", "precio": 146930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i9, RTX 4080, 32GB RAM"},
    {"id": "LAP10", "nombre": "MSI Prestige 14", "categoria": "Laptop", "precio": 83930, "imagen": "https://images.unsplash.com/photo-1588872657578-7e9e1b4b7b1a?w=200&h=200&fit=crop", "descripcion": "i7, 16GB RAM, 512GB SSD"}
]

if not os.path.exists(DATA_FILE):
    save_productos(productos_iniciales)
    print(f"✅ Inicializados {len(productos_iniciales)} productos en {DATA_FILE}")

@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify(load_productos())

@app.route('/api/productos', methods=['POST'])
def create_producto():
    data = request.json
    if not all(k in data for k in ['nombre', 'categoria', 'precio', 'imagen']):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    data['id'] = f"T{int(datetime.now().timestamp()*1000)%10000000 + len(load_productos())}"
    productos = load_productos()
    productos.append(data)
    save_productos(productos)
    return jsonify(data), 201

@app.route('/api/productos/<id>', methods=['PUT'])
def update_producto(id):
    data = request.json
    productos = load_productos()
    for i, p in enumerate(productos):
        if p['id'] == id:
            productos[i].update(data)
            save_productos(productos)
            return jsonify(productos[i])
    return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/api/productos/<id>', methods=['DELETE'])
def delete_producto(id):
    productos = load_productos()
    productos = [p for p in productos if p['id'] != id]
    save_productos(productos)
    return jsonify({'deleted': id})

if __name__ == '__main__':
    print("🚀 Backend Flask iniciando en http://localhost:5000")
    print("📱 API endpoints: /api/productos (GET/POST)")
    print("   PUT/DELETE: /api/productos/<id>")
    app.run(debug=True, port=5000)

