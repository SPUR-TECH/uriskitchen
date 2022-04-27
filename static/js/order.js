var orders = JSON.parse(localStorage.getItem('order'));
var total = localStorage.getItem('total');

if (orders === null || orders === undefined) {
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total === null || total === undefined) {
    localStorage.setItem('total', 0);
    total = 0(localStorage.getItem('total'));
}

var cart = document.querySelector("#cart")
cart.innerHTML = orders.length;