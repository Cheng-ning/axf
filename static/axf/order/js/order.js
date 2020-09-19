$(function () {
    $('#make_order').click(function () {
        $.get(
            '/axforder/makeorder/',
            function (data) {
                window.location.href='/axforder/orderDetail/?orderid='+data['orderid'];
            }
        )
    })
})