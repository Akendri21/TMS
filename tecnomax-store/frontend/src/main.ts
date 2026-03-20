interface Product {
  id: string;
  nombre: string;
  categoria: string;
  precio: number;
  imagen: string;
  descripcion?: string;
}

const API_BASE = 'http://localhost:5000/api/productos';

// ===== UTILIDADES API =====
async function apiRequest(endpoint: string, options: RequestInit = {}): Promise<Product[] | Product | null> {
  try {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) {
      if (response.status === 404) return null;
      throw new Error(`API Error: ${response.status}`);
    }
    
    return response.json();
  } catch (error) {
    console.error('API Error:', error);
    alert('Error conectando al backend. Asegúrate de que python app.py esté corriendo.');
    return [];
  }
}

async function getProductos(): Promise<Product[]> {
  return apiRequest('') as Promise<Product[]>;
}

async function saveProducto(producto: Omit<Product, 'id'>): Promise<Product | null> {
  const data = await apiRequest('', { method: 'POST', body: JSON.stringify(producto) });
  return data as Product;
}

async function updateProducto(id: string, data: Partial<Product>): Promise<Product | null> {
  const updated = await apiRequest(`/${id}`, { method: 'PUT', body: JSON.stringify(data) });
  return updated as Product;
}

async function deleteProducto(id: string): Promise<boolean> {
  const response = await apiRequest(`/${id}`, { method: 'DELETE' });
  return true;
}

// ===== ELEMENTOS DOM =====
const navBtns = document.querySelectorAll('.nav-btn') as NodeListOf<HTMLButtonElement>;
const sections = document.querySelectorAll('.section');
const filterBtns = document.querySelectorAll('.filter-btn') as NodeListOf<HTMLButtonElement>;

const productIdEl = document.getElementById('productId') as HTMLInputElement;
const prodName = document.getElementById('prodName') as HTMLInputElement;
const prodCategory = document.getElementById('prodCategory') as HTMLSelectElement;
const prodPrice = document.getElementById('prodPrice') as HTMLInputElement;
const prodImage = document.getElementById('prodImage') as HTMLInputElement;
const prodDesc = document.getElementById('prodDesc') as HTMLInputElement;
const addProductBtn = document.getElementById('addProductBtn') as HTMLButtonElement;
const cancelEditBtn = document.getElementById('cancelEditBtn') as HTMLButtonElement;
const productsTableBody = document.getElementById('productsTableBody') as HTMLElement;

const searchText = document.getElementById('searchText') as HTMLInputElement;
const filterCategory = document.getElementById('filterCategory') as HTMLSelectElement;
const filterMinPrice = document.getElementById('filterMinPrice') as HTMLInputElement;
const filterMaxPrice = document.getElementById('filterMaxPrice') as HTMLInputElement;
const applySearchFilters = document.getElementById('applySearchFilters') as HTMLButtonElement;
const resetSearchFilters = document.getElementById('resetSearchFilters') as HTMLButtonElement;
const searchTableBody = document.getElementById('searchTableBody') as HTMLElement;

const offersTableBody = document.getElementById('offersTableBody') as HTMLElement;
const offersContainer = document.getElementById('offersContainer') as HTMLElement;

// Modal
const modal = document.getElementById('productModal') as HTMLElement;
const modalImage = document.getElementById('modalImage') as HTMLImageElement;
const modalName = document.getElementById('modalName') as HTMLElement;
const modalCategory = document.getElementById('modalCategory') as HTMLElement;
const modalPrice = document.getElementById('modalPrice') as HTMLElement;
const modalDesc = document.getElementById('modalDesc') as HTMLElement;
const closeModalBtn = document.getElementById('closeModalBtn') as HTMLButtonElement;

let editingId: string | null = null;
let currentFilter: string = 'todos';

// ===== MODAL =====
function abrirModal(producto: Product): void {
  modalImage.src = producto.imagen || 'https://placehold.co/300x300?text=No+image';
  modalImage.onerror = () => modalImage.src = 'https://placehold.co/300x300?text=Error';
  modalName.textContent = producto.nombre;
  modalCategory.textContent = producto.categoria;
  modalPrice.textContent = producto.precio.toLocaleString();
  modalDesc.textContent = producto.descripcion || 'Sin descripción';
  modal.style.display = 'flex';
}

closeModalBtn.onclick = () => modal.style.display = 'none';
modal.onclick = (e) => { if (e.target === modal) modal.style.display = 'none'; };

// ===== RENDER TABLES =====
async function renderProducts(): Promise<void> {
  const productos = await getProductos();
  let filtered = productos;
  if (currentFilter !== 'todos') {
    filtered = productos.filter(p => p.categoria === currentFilter);
  }

  productsTableBody.innerHTML = '';
  filtered.forEach(p => {
    const tr = document.createElement('tr');
    tr.dataset.id = p.id;
    tr.onclick = (e) => {
      const target = e.target as HTMLElement;
      if (target.tagName === 'BUTTON') return;
      abrirModal(p);
    };
    tr.innerHTML = `
      <td><img src="${p.imagen || 'https://placehold.co/50x50?text=No+img'}" alt="${p.nombre}" class="product-img" onerror="this.src='https://placehold.co/50x50?text=Error'"></td>
      <td>${p.nombre}</td>
      <td>${p.categoria}</td>
      <td>${p.precio.toLocaleString()} DOP</td>
      <td>${p.descripcion || ''}</td>
      <td>
        <button class="btn-small btn-secondary" onclick="event.stopPropagation(); editProduct('${p.id}')">✏️ Editar</button>
        <button class="btn-small btn-danger" onclick="event.stopPropagation(); deleteProduct('${p.id}')">🗑️ Eliminar</button>
      </td>
    `;
    productsTableBody.appendChild(tr);
  });
}

function renderSearch(productos: Product[]): void {
  searchTableBody.innerHTML = '';
  productos.forEach(p => {
    const tr = document.createElement('tr');
    tr.dataset.id = p.id;
    tr.onclick = () => abrirModal(p);
    tr.innerHTML = `
      <td><img src="${p.imagen || 'https://placehold.co/50x50?text=No+img'}" alt="${p.nombre}" class="product-img" onerror="this.src='https://placehold.co/50x50?text=Error'"></td>
      <td>${p.nombre}</td>
      <td>${p.categoria}</td>
      <td>${p.precio.toLocaleString()} DOP</td>
      <td>${p.descripcion || ''}</td>
    `;
    searchTableBody.appendChild(tr);
  });
}

async function renderOffers(): Promise<void> {
  const productos = await getProductos();
  const ofertas = productos.filter(p => p.precio < 18150);
  
  offersTableBody.innerHTML = '';
  if (ofertas.length === 0) {
    offersTableBody.innerHTML = '<tr><td colspan="5" style="text-align:center; padding:2rem;">No hay ofertas en este momento</td></tr>';
  } else {
    ofertas.forEach(p => {
      const tr = document.createElement('tr');
      tr.dataset.id = p.id;
      tr.onclick = () => abrirModal(p);
      tr.innerHTML = `
        <td><img src="${p.imagen || 'https://placehold.co/50x50?text=No+img'}" alt="${p.nombre}" class="product-img" onerror="this.src='https://placehold.co/50x50?text=Error'"></td>
        <td>${p.nombre}</td>
        <td>${p.categoria}</td>
        <td>${p.precio.toLocaleString()} DOP</td>
        <td>${p.descripcion || ''}</td>
      `;
      offersTableBody.appendChild(tr);
    });
  }
  
  offersContainer.innerHTML = ofertas.length ? 
    `<div class="alert-card" style="background:#1f4a33;">🔥 Hay ${ofertas.length} productos con precio bajo.</div>` : '';
}

// ===== CRUD =====
async function guardarProducto(): Promise<boolean> {
  const nombre = prodName.value.trim();
  const categoria = prodCategory.value;
  const precio = parseFloat(prodPrice.value);
  const imagen = prodImage.value.trim();
  const descripcion = prodDesc.value.trim();

  if (!nombre || !categoria || isNaN(precio) || precio < 0 || !imagen) {
    alert('Completa todos los campos obligatorios.');
    return false;
  }

  const productoData: Omit<Product, 'id'> = { nombre, categoria, precio, imagen, descripcion };

  if (editingId) {
    const updated = await updateProducto(editingId, productoData);
    if (updated) {
      cancelarEdicion();
      await renderProducts();
      return true;
    }
  } else {
    const created = await saveProducto(productoData);
    if (created) {
      limpiarFormulario();
      await renderProducts();
      return true;
    }
  }
  return false;
}

addProductBtn.onclick = guardarProducto;

window.deleteProducto = async (id: string): Promise<void> => {
  if (confirm('¿Eliminar producto?')) {
    await deleteProducto(id);
    if (editingId === id) cancelarEdicion();
    await renderProducts();
  }
};

window.editProduct = async (id: string): Promise<void> => {
  const productos = await getProductos();
  const p = productos.find(p => p.id === id);
  if (!p) return;

  editingId = id;
  productIdEl.value = p.id;
  prodName.value = p.nombre;
  prodCategory.value = p.categoria;
  prodPrice.value = p.precio.toString();
  prodImage.value = p.imagen;
  prodDesc.value = p.descripcion || '';
  addProductBtn.textContent = '✏️ Actualizar producto';
  cancelEditBtn.style.display = 'inline-block';
};

function cancelarEdicion(): void {
  editingId = null;
  productIdEl.value = '';
  addProductBtn.textContent = '➕ Agregar producto';
  cancelEditBtn.style.display = 'none';
  limpiarFormulario();
}

cancelEditBtn.onclick = cancelarEdicion;

function limpiarFormulario(): void {
  prodName.value = '';
  prodCategory.value = 'Móvil';
  prodPrice.value = '';
  prodImage.value = '';
  prodDesc.value = '';
}

// ===== FILTROS BÚSQUEDA =====
async function aplicarFiltrosBusqueda(): Promise<void> {
  const productos = await getProductos();
  let filtered = productos;

  const texto = searchText.value.trim().toLowerCase();
  const categoria = filterCategory.value;
  const min = parseFloat(filterMinPrice.value);
  const max = parseFloat(filterMaxPrice.value);

  if (texto) {
    filtered = filtered.filter(p => 
      p.nombre.toLowerCase().includes(texto) ||
      (p.descripcion && p.descripcion.toLowerCase().includes(texto))
    );
  }
  if (categoria) {
    filtered = filtered.filter(p => p.categoria === categoria);
  }
  if (!isNaN(min)) {
    filtered = filtered.filter(p => p.precio >= min);
  }
  if (!isNaN(max)) {
    filtered = filtered.filter(p => p.precio <= max);
  }

  renderSearch(filtered);
}

applySearchFilters.onclick = aplicarFiltrosBusqueda;

resetSearchFilters.onclick = async () => {
  searchText.value = '';
  filterCategory.value = '';
  filterMinPrice.value = '';
  filterMaxPrice.value = '';
  const productos = await getProductos();
  renderSearch(productos);
};

// ===== FILTROS CATEGORÍA PRODUCTOS =====
filterBtns.forEach(btn => {
  btn.onclick = () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.dataset.filter!;
    renderProducts();
  };
});

// ===== NAVEGACIÓN =====
navBtns.forEach(btn => {
  btn.onclick = async (e) => {
    const target = (e.target as HTMLElement).dataset.section!;
    navBtns.forEach(b => b.classList.remove('active'));
    (e.target as HTMLElement).classList.add('active');
    sections.forEach(s => s.classList.remove('active'));
    (document.getElementById(target + 'Section') as HTMLElement).classList.add('active');
    
    if (target === 'offers') await renderOffers();
    if (target === 'products') await renderProducts();
    if (target === 'search') {
      const productos = await getProductos();
      renderSearch(productos);
    }
  };
});

// ===== INICIALIZAR =====
async function init(): Promise<void> {
  await renderProducts();
}
init();

