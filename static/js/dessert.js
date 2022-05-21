var dessertcart = document.querySelector('#dessertcart');
var dessertotal = document.querySelector('#desserttotal');

// Add desserts to order 

function addDessert(dessertid) {

    // Get name of dessert

    var name = document.querySelector('#dessertname' + dessertid).innerHTML;

    //  Get dessert prices

    var radio = 'dessert' + dessertid;
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

    orders[cartSize] = [size, name, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Update items in cart

    var cart = document.querySelector("#cart")
    cart.innerHTML = orders.length;

    var dessertcart = document.querySelector('#dessertcart');

    remove = '<div class="del" onclick="removedessert(' + cartSize + ')">X</div>';
    desserttotal.innerHTML = 'Total:  £' + total + ' ';
    dessertcart.innerHTML += '<li>' + size + ' :   ' + name + ' £' + price + ' ' + remove + '</li>';
}

function dessertshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    dessertcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<div class="del" onclick="removedessert(' + i + ')">X</div>';
        dessertcart.innerHTML += '<li>' + orders[i][0] + ' :   ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    desserttotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
}

dessertshoppingCart();

function removedessert(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    dessertshoppingCart();
}