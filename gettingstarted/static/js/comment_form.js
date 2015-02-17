$(function(){
    $('.js-btn-reply').on('click', function(){
        var parentid = $(this).data('commentparentid');
        $(this).addClass('hidden');
        $('.js-comment-form').clone()
                .appendTo($(this).parent())
                .removeClass('js-comment-form');
        $(this).parent().find('.js-comment_parent_id').attr('value', parentid);
        $(this).parent().find('.js-btn-comment').attr('value', 'Reply');
    })
})