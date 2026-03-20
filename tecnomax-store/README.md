# 📱 TecnoMax Store - Aplicación Moderna

## 🎯 🚀 EJECUCIÓN AUTOMÁTICA (1 comando!)

### Windows

```bash
setup.bat
```

### Linux/Mac

```bash
chmod +x setup.sh
./setup.sh
```

**¡Eso es todo!** Se instala, compila y levanta backend/frontend automáticamente.

---

## 🛠️ Estructura

```
tecnomax-store/
├── backend/          # Python Flask API
├── frontend/         # TypeScript + SCSS Frontend
├── setup.bat         # 🚀 Windows 1-click
├── setup.sh          # 🚀 Linux/Mac 1-click
├── .gitignore
└── README.md
```

## 🔧 Modo Desarrollador (desde frontend/)

```bash
cd frontend
npm install
npm run dev:all  # Backend + Frontend concurrently
```

## 📊 URLs

- **Backend API**: <http://localhost:5000/api/productos>
- **Frontend App**: <http://localhost:3000/dist/index.html>
- **Test API**: `curl http://localhost:5000/api/productos | jq '.[0]'`

---

## 🏗️ Instalación Manual (si prefieres)

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 2. Frontend

```bash
cd frontend
npm install
npm run build
# Abrir dist/index.html
```

### 3. Dev completo

```bash
cd frontend
npm run dev:all
```

---

## 🔧 Scripts Disponibles (frontend/package.json)

| Script | Descripción |
|--------|-------------|
| `npm run build` | Compila TS→JS + SCSS→CSS |
| `npm run dev` | Live-server + watch (frontend solo) |
| `npm run dev:all` | Backend + Frontend concurrently |
| `npm run backend` | Solo backend (desde frontend/) |

---

## 📋 Funcionalidades

- ✅ **CRUD** productos (API persistente JSON)
- ✅ **Filtros** categoría/productos
- ✅ **Búsqueda** avanzada (texto/precio/categoría)
- ✅ **Ofertas** <18,150 DOP
- ✅ **Modal** detalles (click fila)
- ✅ **Diseño** Heavy Metal Tech (idéntico)
- ✅ **Datos**: 60 productos reales DOP (1EUR=70DOP)

## 🛑 Notas Técnicas

- **Backend**: Flask + CORS + JSON persistente
- **Frontend**: TypeScript strict + SCSS variables/mixins
- **Comunicación**: fetch localhost:5000 (CORS ✅)
- **Puerto Frontend**: 3000 (live-server)
- **Verificación**: Scripts chequean Node/Python

## 🎉 ¡Disfruta tu TecnoMax Store moderna! ⚡

**Preguntas?** Todo documentado arriba. ¡Ejecuta `setup.bat` y listo!
