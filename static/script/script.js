$(document).ready(function() {
    $('div.sidebar').hide(0);
    $('div.logo').hide(0);
    $('div.add-todo').hide(0);
    $('div.todo-item').hide(0);
    $('div.sidebar').slideDown(750);
    $('div.logo').fadeIn(1000);
    $('div.add-todo').fadeIn(1250);
    $('div.todo-item').fadeIn(1500);
});
