var desertcart = document.querySelector('#desertcart');
var deserttotal = document.querySelector('#deserttotal');

// Add deserts to order 

function addDesert(desertid) {

    // Get name of desert

    var name = document.querySelector('#desertname' + desertid).innerHTML;

    //  Get desert prices

    var radio = 'desert' + desertid;
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

    // Save items in local storage so it will delete when user leaves the site

    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Update items in cart

    var cart = document.querySelector("#cart")
    cart.innerHTML = orders.length;

    var desertcart = document.querySelector('#desertcart');

    remove = '<div class="del" onclick="removeDesert(' + cartSize + ')">X</div>';
    deserttotal.innerHTML = 'Total:  £' + total + ' ';
    desertcart.innerHTML += '<li>' + size + ' :   ' + name + ' £' + price + ' ' + remove + '</li>';
}

function desertshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    desertcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        remove = '<div class="del" onclick="removeDesert(' + i + ')">X</div>';
        desertcart.innerHTML += '<li>' + orders[i][0] + ' :   ' + orders[i][1] + ' £' + orders[i][2] + ' ' + remove + '</li>';
    }
    deserttotal.innerHTML = 'Total:  £' + total + ' ';
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
}

desertshoppingCart();

function removeDesert(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    desertshoppingCart();
}