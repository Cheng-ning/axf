$(function () {
    var flagcode = false

    $('#changeImage').click(function () {
        $(this).attr('src', '/axfuser/get_code/'+Math.random())
    })

    $('#changeimg').click(function () {
        $('#changeImage').attr('src', '/axfuser/get_code/'+Math.random())
    })

    $('#imgCode').blur(function () {
        var imgcode = $(this).val()
        $.getJSON('/axfuser/checkcode/', {imgcode : imgcode}, function (data) {
            if (data['status'] == 201){
                $('#message').html(data['msg'])
            } else {
                $('#message').html('')
                flagcode = true
            }

        })
    })

    $('form').submit(function () {
        var username = $('#exampleInputname').val()
        if (!username) {
            $('#message').html('请输入用户名')
            return false
        }

        var password = $('#exampleInputPassword').val()
        if (!password) {
            $('#message').html('请输入密码')
            return false
        }

        var imgcode = $('#imgCode').val()
        if (!imgcode) {
            $('#message').html('请输入验证码')
            return false
        }

        if (flagcode) {
            return true
        } else {
            return false
        }
    })
})