$(function () {
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#all_type_container').toggle()

        $('#sort_rule_container').css('display', 'none')
        $('#sort_rule').find('span').attr('class', 'glyphicon glyphicon-chevron-down')
    })

    $('#sort_rule').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#sort_rule_container').toggle()

        $('#all_type_container').css('display', 'none')
        $('#all_type').find('span').attr('class', 'glyphicon glyphicon-chevron-down')
    })
})