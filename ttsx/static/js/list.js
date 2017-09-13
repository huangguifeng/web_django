/**
 * Created by python on 17-9-13.
 */



//列表页点击加入购物车
;$(function () {





    //点击加入购物车
    $('.add_goods').click(function () {

        var cart =$('.cart_name');

        // 购物车位置
        var cartoffse =  cart.offset();
        var cartleft = cartoffse.left;
        var carttop = cartoffse.top;

        // 获取按钮在页面的位置
        var btnoffset = $(this).offset();
        var btnleft = btnoffset.left;
        var btntop = btnoffset.top;
        // 获取滑动的距离
        var scrollTop = $(document).scrollTop();
        var move_cart = $('.move_cart');

        move_cart.css({'left':btnleft,'top':btntop-scrollTop}).show();

        move_cart.stop().animate({
                    'left': cartleft + 170,
                    'top': carttop - scrollTop + 9
                },1000,'swing',function () {
                    move_cart.hide();
                });

        var url = $(this).parent().siblings('a').attr('href');
        goods_id = url.split('/');
        // console.log(goods_id)
        $.post('/cart/addcart/',{'goods_id':goods_id[1]},function (data) {
                 //加入购物车回调
            if (data['error']==0){
                window.location.href=data['path']
            }else {
                console.log(data['cart_num'])
                $('.goods_count').html(data['cart_num'])
            }
        })

    })

});