/**
 * Created by python on 17-9-19.
 */
   ;$(function () {
        {{ no_null|safe }}
        var name = $.cookie('name');
        $('.login_info').show();
        $('.em0').html(name);
        $('.login_btn').hide();

        $('.login_info').mouseover(function () {
            $('.em0').hide();
            $('.em1').html(name);
            $('.em3').show();
        })
        $('.login_info').mouseout(function () {
            $('.em0').show();
            $('.em3').hide();

        });
    });