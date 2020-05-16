$(document).ready(function () {
    $('.admin').on('click',function(){    
    $('.admin-login').toggle(500);
    });
    $('.faculty').on('click',function(){    
        $('.faculty-login').toggle(500);
    });
    $('button').on('click',function(){
        alert(this.className)
    })
});
window.onload = function(){
    $('.admin-login').hide();
    $('.faculty-login').hide();
}