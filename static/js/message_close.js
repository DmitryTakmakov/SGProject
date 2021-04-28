window.onload = function () {
    let message = $('.message');
    let ban_time = $('#id_ban_time');

    $('.link').click(function () {
        let target = event.target;
        let link_num = parseInt(target.id.replace('link-', ''));
        if (target.text == 'забанить') {
            let form_id = 'form-' + link_num;
            $('#' + form_id).prop('style', 'display:inline');
        } else {
            let button_id = 'submit-' + link_num;
            $('#' + button_id).prop('style', 'display:inline');
        }});

    $('.close').click(function () {
        message.prop('style', 'display:none');

        // window.alert(form_id);
        // window.alert($(this).attr('id'));
        // message.prop('style', 'display:none');
    });
};
