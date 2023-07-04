
// Función para buscar productos
function buscarProductos() {
  // Obtener el valor del campo de búsqueda
  var searchTerm = document.querySelector('#search-box input').value.toLowerCase();
  
  // Obtener todos los productos
  var productos = document.querySelectorAll('.product');
  
  // Recorrer los productos y ocultar/mostrar según el término de búsqueda
  productos.forEach(function(producto) {
    var nombreProducto = producto.querySelector('.product-name').textContent.toLowerCase();
    
    if (nombreProducto.includes(searchTerm)) {
      producto.style.display = 'block';
    } else {
      producto.style.display = 'none';
    }
  });
}

// Función para añadir un producto al carrito
function agregarAlCarrito(event) {
  var producto = event.target.parentNode;
  var nombreProducto = producto.querySelector('.product-name').textContent;
  
  // Aquí puedes implementar la lógica para agregar el producto al carrito en la base de datos
  // Por ahora, simplemente lo agregaremos visualmente al carrito
  
  var itemCarrito = document.createElement('div');
  itemCarrito.className = 'product';
  itemCarrito.innerHTML = `
    <img src="${producto.querySelector('img').src}" alt="${nombreProducto}">
    <div class="product-name">${nombreProducto}</div>
    <div class="product-price">${producto.querySelector('.product-price').textContent}</div>
    <button class="remove-from-cart">Eliminar</button>
  `;
  
  document.querySelector('#cart').appendChild(itemCarrito);
  
  // Añadir evento para eliminar el producto del carrito
  itemCarrito.querySelector('.remove-from-cart').addEventListener('click', eliminarDelCarrito);
}

// Función para eliminar un producto del carrito
function eliminarDelCarrito(event) {
  var itemCarrito = event.target.parentNode;
  
  // Aquí puedes implementar la lógica para eliminar el producto del carrito en la base de datos
  // Por ahora, simplemente lo eliminaremos visualmente del carrito
  
  itemCarrito.parentNode.removeChild(itemCarrito);
}

// Función para generar la factura y finalizar la compra
function finalizarCompra(event) {
  event.preventDefault();
  
  var nombre = document.querySelector('#checkout-form input[type="text"]').value;
  var email = document.querySelector('#checkout-form input[type="email"]').value;
  
  // Aquí puedes implementar la lógica para generar la factura y finalizar la compra en la base de datos
  
  alert('¡Compra realizada!\n\nFactura generada:\n\nNombre: ' + nombre + '\nEmail: ' + email);
  
  // Limpiar el carrito y el formulario de compra
  document.querySelector('#cart').innerHTML = '';
  document.querySelector('#checkout-form').reset();
}

// Asignar los eventos a los elementos correspondientes
document.querySelector('#search-box button').addEventListener('click', buscarProductos);

var productos = document.querySelectorAll('.product');
productos.forEach(function(producto) {
  producto.querySelector('button').addEventListener('click', agregarAlCarrito);
});

var itemsCarrito = document.querySelectorAll('#cart .product');
itemsCarrito.forEach(function(itemCarrito) {
  itemCarrito.querySelector('.remove-from-cart').addEventListener('click', eliminarDelCarrito);
});

document.querySelector('#checkout-form').addEventListener('submit', finalizarCompra);
