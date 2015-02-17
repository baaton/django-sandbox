$(function(){
    $('.js-btn-link').on('click', function(){
        $(location).attr('href',$(this).data('url'));
    });

    function getCookie(c_name)
    {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    $('.js-btn-delete-article').on('click', function() {
        var article_id = $(this).data('articleid');
        $.ajax({
            type: 'POST',
            url : "/addarticle/", // the endpoint
            data : { article_id : article_id }, // data sent with the delete request
            success : function(json) {
                $(location).attr('href', '/article/');
            }
        });
    });

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});