// buscador.js
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var searchTerm = document.getElementById('searchInput').value;
    // Implementa aquí tu lógica de búsqueda
});

// inicio sesion.js
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    // Aquí puedes agregar la lógica de validación de credenciales
});
