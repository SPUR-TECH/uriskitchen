// Success cart

// // CREDIT TO TRAVERSY MEDIA FOR THE ANIMATION

const loader = document.querySelector('.loader');
const success_title = document.querySelector('.success-cart h1');
const success_title2 = document.querySelector('.success-cart h2');

// Animation function
function init() {
    setTimeout(() => {
        loader.style.opacity = 0;
        loader.style.display = 'none';

        success_title.style.display = 'block';
        success_title2.style.display = 'block';
        setTimeout(() => (success_title.style.opacity = 1), 50);
        setTimeout(() => (success_title2.style.opacity = 1), 2000);
    }, 4000);
}

init();

// Add to cart function
function successCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    successcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<div <button class="success-del" onclick="removeMeal(' + i + ')">X</button></div>';
        successcart.innerHTML += '<li>' + orders[i][0] + ': ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    successtotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
}

successCart();