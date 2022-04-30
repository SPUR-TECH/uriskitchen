var mealcart = document.querySelector('#mealcart');
var mealtotal = document.querySelector('#mealtotal');

// add meals to order 

function addMeal(mid) {

    // Get name of meal

    var name = document.querySelector('#mealname' + mid).innerHTML;
    mealcart.innerHTML += '<li>' + name + '</li>';
}