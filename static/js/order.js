var orders = JSON.parse(sessionStorage.getItem('order'));
var total = sessionStorage.getItem('total');

if (orders === null || orders === undefined) {
    sessionStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(sessionStorage.getItem('orders'));
}

if (total === null || total === undefined) {
    sessionStorage.setItem('total', 0);
    total = 0(sessionStorage.getItem('total'));
}

var cart = document.querySelector("#cart")
cart.innerHTML = orders.length;