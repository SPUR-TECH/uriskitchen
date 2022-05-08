// Shoppingcart

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
    var ur = '/thai/cart'
    var orderData = {};
    orderData['orders'];
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        success: function (data) {
            console.log('The data was sent')
        }
    })
}