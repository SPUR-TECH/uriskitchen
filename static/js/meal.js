var mealcart = document.querySelector('#mealcart');
var mealtotal = document.querySelector('#mealtotal');

// add meals to order 

function addMeal(mealid) {

    // Get name of meal

    var name = document.querySelector('#mealname' + mealid).innerHTML;

    //  Get meal prices

    var radio = 'meal' + mealid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L'
    }

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    // Save items in local storage

    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    console.log(`MEALS ORDERS: ${orders}`);

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Update items in cart

    var cart = document.querySelector("#cart")
    cart.innerHTML = orders.length;

    remove = '<button class="del" onclick="removeMeal(' + cartSize + ')">X</button>';
    mealtotal.innerHTML = 'Total:  £' + total + ' ';
    mealcart.innerHTML += '<li>' + size + ' : ' + name + ' £' + price + ' ' + remove + '</li>';
}

function mealshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    mealcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<button class="del" onclick="removeMeal(' + i + ')">X</button>';
        mealcart.innerHTML += '<li>' + orders[i][0] + ': ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    mealtotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
}

mealshoppingCart();

function removeMeal(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);

    mealshoppingCart();
}