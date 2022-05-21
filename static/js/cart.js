// Shoppingcart

// CREDIT TO TRAVERSY MEDIA FOR THE ANIMATION

const loader = document.querySelector('.loader');
const title1 = document.querySelector('.cart h1');
const title2 = document.querySelector('.cart h2');

// Animation function
function init() {
    setTimeout(() => {
        loader.style.opacity = 0;
        loader.style.display = 'none';

        title1.style.display = 'block';
        title2.style.display = 'block';
        setTimeout(() => (title1.style.opacity = 1), 50);
        setTimeout(() => (title2.style.opacity = 1), 2000);
    }, 4000);
}

init();

// Add to cart function
function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    mealcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<div class="del" onclick="removeMeal(' + i + ')">X</div>';
        mealcart.innerHTML += '<li>' + orders[i][0] + ': ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    mealtotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
}

shoppingCart();

// Remove from cart function
function removeMeal(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);

    shoppingCart();
}