var desertcart = document.querySelector('#desertcart');
var deserttotal = document.querySelector('#deserttotal');

// add deserts to order 

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

    var desertcart = document.querySelector('#desertcart');

    deserttotal.innerHTML = 'Total:  £' + total + ' ';
    desertcart.innerHTML += '<li>' + size + ' :   ' + name + ' £' + price + '</li>';
}

function desertshoppingCart() {
    var orders = JSON.parse(sessionStorage.getItem('orders'));
    var total = sessionStorage.getItem('total');
    var cartSize = orders.length;

    desertcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        desertcart.innerHTML += '<li>' + orders[i][0] + ' :   ' + orders[i][1] + ' £' + orders[i][2] + '</li>';
    }
    deserttotal.innerHTML = 'Total:  £' + total + ' ';
}

desertshoppingCart();