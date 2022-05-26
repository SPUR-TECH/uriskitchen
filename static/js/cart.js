// Shoppingcart

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
function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    mealcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
<<<<<<< HEAD
        remove = '<div <button class="del" onclick="removeMeal(' + i + ')">X</button></div>';
=======
        remove = '<div <button class="del btn-danger" onclick="removeMeal(' + i + ')">X</button></div>';
>>>>>>> 429b5bcd27550dad57a4ee7b37fc3a0317656476
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


function order() {
    var orders = localStorage.getItem('orders');
    var ur = '/cart/';
    var orderData = {};
    orderData['orders'] = orders;
<<<<<<< HEAD
    $.ajax({
=======
    $.post({
>>>>>>> 429b5bcd27550dad57a4ee7b37fc3a0317656476
        url: ur,
        type: "POST",
        data: orderData,
        success: function (data) {
            window.location.replace('/success')
            // localStorage.setItem('orders', JSON.stringify([]));
            // localStorage.setItem('total', 0);
            print('the data was sent')
        }
    })
}