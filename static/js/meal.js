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

    var orders = JSON.parse(sessionStorage.getItem('orders'));
    var total = sessionStorage.getItem('total');
    var cartSize = orders.length;

    // Save items in session storage so it will delete when user leaves the site

    orders[cartSize] = [name, size, price];
    sessionStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    sessionStorage.setItem('total', total);

    // Update items in cart

    var cart = document.querySelector("#cart")
    cart.innerHTML = orders.length;

    var mealcart = document.querySelector('#mealcart');

    mealtotal.innerHTML = 'Total:  £' + total + ' ';
    mealcart.innerHTML += '<li>' + size + ' :   ' + name + ' £' + price + '</li>';
}

function mealshoppingCart() {
    var orders = JSON.parse(sessionStorage.getItem('orders'));
    var total = sessionStorage.getItem('total');
    var cartSize = orders.length;

    mealcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        mealcart.innerHTML += '<li>' + orders[i][0] + ' :   ' + orders[i][1] + ' £' + orders[i][2] + '</li>';
    }
    mealtotal.innerHTML = 'Total:  £' + total + ' ';
}

mealshoppingCart();