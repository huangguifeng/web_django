/**
 * Created by python on 17-9-13.
 */

        ;$(function () {
       $('.num_show').blur(function () {
        value = $(".num_show").val();
        value = parseInt(value);
        if (value >= 100) {
            value = 100;
        }
        else if (value <= 1 || isNaN(value)){
            value = 1
        }
        total();
    });

    // 加减的点击事件
    $('.num_add').delegate('a', 'click', function () {
        value = $(".num_show").val();
        value = parseInt(value);
        if ($(this).html() == "+") {
            if(value<100){
                value ++;
            }
        }
        else {
            value --;
            if (value <= 1) {
                value = 1;
            }
        }
        total();
    });

    function total() {
        $('.num_show').val(value);
        //  总价的计算
        var price = $(".show_pirze em").html();
        price = parseFloat(price);
        var sum = value * price;
        sum = sum.toFixed(2);
        $(".total em").html(sum)
    }

    // 获取购物车里的商品数量
    $.post('/cart/cart_num/', function (data) {
        $('.goods_count').html(data['cart_count'])
    });

    // 加入购物车
    var add_cart = $('.operate_btn .add_cart');
    add_cart.click(function () {

        //获取到购物车的位置
        var cart = $('.cart_name');

        // 购物车位置
        var cartoffse = cart.offset();
        var cartleft = cartoffse.left;
        var carttop = cartoffse.top;

        // 获取按钮在页面的位置
        var btnoffset = $(this).offset();
        var btnleft = btnoffset.left;
        var btntop = btnoffset.top;


        // 获取滑动的距离
        var scrollTop = $(document).scrollTop();
        var move_cart = $('.operate_btn .move_cart');

        move_cart.css({'left': btnleft + 60, 'top': btntop - scrollTop + 15}).show();

        move_cart.stop().animate({
            'left': cartleft + 170,
            'top': carttop - scrollTop + 9
        }, 1000, 'swing', function () {
            move_cart.hide();
        });


        var count = $('.num_add .num_show').val();
        var goods_id = $(this).prev().val();
        $.post('/cart/addcart/', {'goods_id': goods_id, 'count': count}, function (data) {
            //加入购物车回调
            if (data['error'] == 0) {
                window.location.href = data['path']
            } else {
                // console.log(data['cart_num']);
                $('.goods_count').html(data['cart_num'])
            }
        });
    });

});
