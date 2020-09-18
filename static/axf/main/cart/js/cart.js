$(function () {
    $('.addToCart').click(function () {
        var $button = $(this);
        var g_id = $button.attr('goodsid')

        $.get('/axfcart/addToCart/',
            {'g_id': g_id},
            function (data) {
                $button.prev().html(data['c_goods_num']);
            })
    })

    $('.subCart').click(function () {
        var $button = $(this)
        var g_id = $button.next().next().attr('goodsid')

        $.get('/axfcart/subCart/',
            {'g_id': g_id},
            function (data) {
                $button.next().html(data['c_goods_num']);
                if ($button.next().html() == 0){
                    $button.attr('disabled', true)
                }
            })
    })

    $('.addCart').click(function () {
        var $button = $(this)
        var cart_id = $button.parent().parent().attr('cartid')
        $.post(
            '/axfcart/addCart/',
            {'cart_id': cart_id},
            function (data) {
                $button.prev().html(data['c_goods_num'])
                $('#total_price').html(data['total_price']);
            })
    })

    $('.subToCart').click(function () {
        var $button = $(this)
        var cart_id = $button.parent().parent().attr('cartid')
        $.post(
            '/axfcart/subToCart/',
            {'cart_id': cart_id},
            function (data) {
                if (data['c_goods_num'] > 0) {
                    $button.next().html(data['c_goods_num'])
                } else {
                    $button.parent().parent().remove()
                }
                $('#total_price').html(data['total_price']);
            })
    })


    $('.confirm').click(function () {
        var $div = $(this)
        var cartid = $div.parent().attr('cartid')
        $.post(
            '/axfcart/changeStatus/',
            {'cartid': cartid},
            function (data) {
                if (data['c_is_select']) {
                    $div.find('span').find('span').html('✓')
                } else {
                    $div.find('span').find('span').html('')
                }
                if (data['is_all_select']) {
                    $('.all_select').find('span').find('span').html('✓')
                } else {
                    $('.all_select').find('span').find('span').html('')
                }
                $('#total_price').html(data['total_price']);
            }
        )
    })

    $('.all_select').click(function () {
        var select_list = []
        var unselect_list = []

        $('.confirm').each(function () {
            var cartid = $(this).parent().attr('cartid')
            if ($(this).find('span').find('span').html()) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }
        })

        if (unselect_list.length == 0) {
            $.ajax({
                url: '/axfcart/allSelect/',
                data: {'cartid_list': select_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('');
                    $('.all_select').find('span').find('span').html('');
                    $('#total_price').html(data['total_price']);

                }
            })
        } else {
            $.ajax({
                url: '/axfcart/allSelect/',
                data: {'cartid_list': unselect_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('✓');
                    $('.all_select').find('span').find('span').html('✓');
                    $('#total_price').html(data['total_price']);
                }
            })
        }
    })


})