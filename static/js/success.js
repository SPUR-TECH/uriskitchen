// Success cart

// // CREDIT TO TRAVERSY MEDIA FOR THE ANIMATION

var loader = document.querySelector('.loader');
var success_title = document.querySelector('.success-cart h1');
var success_title2 = document.querySelector('.success-cart h2');
var success_email = document.querySelector('.success-email');

// Animation function
function init() {
    setTimeout(function () {
        loader.style.opacity = 0;
        loader.style.display = 'none';

        success_title.style.display = 'block';
        success_title2.style.display = 'block';
        success_email.style.display = 'block';
        setTimeout(function () {
            return success_email.style.opacity = 1;
        }, 2000);
        setTimeout(function () {
            return success_title.style.opacity = 1;
        }, 50);
        setTimeout(function () {
            return success_title2.style.opacity = 1;
        }, 2000);
    }, 4000);
}

init();

// Add to cart function
function successCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    successcart.innerHTML = '';
    for (var i = 0; i < cartSize; i++) {
        remove = '<div <button class="success-del" onclick="removeMeal(' + i + ')">X</button></div>';
        successcart.innerHTML += '<li>' + orders[i][0] + ': ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    successtotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
}

successCart();

function clearOrder() {
    localStorage.setItem('orders', JSON.stringify([]));
    localStorage.setItem('total', 0);
    document.querySelector('#cart').innerHTML = '0';
}

var emptyBasket = setTimeout(clearOrder, 50);