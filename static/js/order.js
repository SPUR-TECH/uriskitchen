var mealcart = document.querySelector('#mealcart');
var mealtotal = document.querySelector('#mealtotal');

// add meals to order 

function addMeal(mid) {

    // Get name of meal

    var name = document.querySelector('#mealname' + mid).innerHTML;
    //  Get meal prices
    var radio = 'meal' + mid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L'
    }

    mealcart.innerHTML += '<li>' + size + ' :   ' + name + ' £' + price + '</li>';
}