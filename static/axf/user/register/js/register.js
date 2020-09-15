$(function () {
    flagusername = false
    flagpassword = false
    flagemail = false

    $('#exampleInputUsername').blur(function () {
        var username = $(this).val();
        var reg = /^[a-zA-Z0-9]{6,8}$/;
        var c = reg.test(username);
        if (c) {
            $.getJSON('/axfuser/checkname/',{username:username},function (data) {
                if (data['status'] == 200){
                    $('#usernameinfo').html(data['message']).css('color', 'green')
                    flagusername = true
                }else {
                    $('#usernameinfo').html(data['message']).css('color', 'red')
                }

            })

        } else {
            $('#usernameinfo').html('请输入6-8位英文或数字').css('color', 'red')
        }
    })

    $('#exampleInputEmail1').blur(function () {
        var email = $(this).val()
        var reg = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
        var c = reg.test(email)
        if (c) {
            $('#emailinfo').html('')
            flagemail = true
        }else {
            $('#emailinfo').html('请输入正确的邮箱').css('color', 'red')
        }
    })

    $('#exampleInputPassword2').blur(function () {
        var password1 = $('#exampleInputPassword1').val()
        var password2 = $(this).val()
        if (password1 == password2) {
            $('#passwordinfo2').html('密码一致').css('color', 'green')
            flagpassword = true
        } else {
            $('#passwordinfo2').html('密码不一致').css('color', 'red')
        }
    })

    $('form').submit(function () {
        var username = $('#exampleInputUsername').val()
        if (!username) {
            $('#usernameinfo').html('用户名不能为空').css('color', 'red')
            return false
        }

        var password = $('#exampleInputPassword1').val()
        if (!password) {
            $('#passwordinfo1').html('密码不能为空').css('color', 'red')
            return false;
        }

        var email = $('#exampleInputEmail1').val()
        if (!email){
            $('#emailinfo').html('邮箱不能为空').css('color', 'red')
            return false
        }
        var c = flagpassword & flagusername & flagemail

        if (c) {
            return true
        } else {
            return false
        }

    })
})