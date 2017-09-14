$(function () {


    // {# 计算当前页面的商品品种数 #}
    function fn_sumList() {
        var sum_price_list = $('.cart_list_td ').find('.col07');
        var sum_len = sum_price_list.length;
        $('.total_count').find('em').html(sum_len);
    };
    fn_sumList();

    // {# 计算总数量 #}
    function fn_num_zong() {
        var num_zong = 0;
        $('.num_show').each(function (i) {
            if ($('.cart_list_td .col01 input').eq(i).prop('checked')) {
                num_zong += parseInt($('.num_show').eq(i).val());
            }
        });
        $('.settlements .col03 b').html(num_zong);
        return num_zong;
    };
    num_zong = fn_num_zong();

    // {# 计算总价格 #}
    function fn_price_zong() {
        var price_zong = 0;
        $('.num_show').each(function (i) {
            prices = parseFloat(fn_count_num($('.num_show').eq(i))).toFixed(2);
            price_zong = parseFloat(price_zong) + parseFloat(prices)
            price_zong = price_zong.toFixed(2);
        });
        $('.settlements .col03 em').html(price_zong);
        return price_zong;
    };
    price_zong = fn_price_zong();

    // {# 勾选商品的操作 #}
    $('.cart_list_td .col01 input').click(function () {
        var this_zong = parseInt($(this).parent().parent().find('.num_show').val());
        var this_price = fn_count_num($(this).parent().parent().find('.num_show'));
        var price_zong = $('.settlements .col03 em').html();
        var num_zong = parseInt($('.settlements .col03 b').html());
        if ($(this).prop('checked')) {
            $(this).prop('checked', true);
            num_zong += this_zong;
            price_zong = parseFloat(price_zong) + parseFloat(this_price);
        }
        else {
            $(this).prop('checked', false);
            num_zong -= this_zong;
            price_zong -= this_price;
        }
        // {# 显示总数量 #}
        $('.settlements .col03 b').html(num_zong);
        // {# 显示总价格 #}
        $('.settlements .col03 em').html(price_zong.toFixed(2));
    });

    // {# 全选 #}
    $('.settlements .col01 input').click(function () {
        if ($(this).prop('checked')) {
            $('.col01 input').prop('checked', true);
            $('.settlements .col03 b').html(fn_num_zong());
            $('.settlements .col03 em').html(fn_price_zong().toFixed(2));
        }
        else {
            $('.col01 input').prop('checked', false);
            $('.settlements .col03 b').html(num_zong = 0);
            $('.settlements .col03 em').html(price_zong = 0);
        }
    });


    // {# 获取数量 value框 #}
    function fn_value(th) {
        num_show = $(th).parent().find('.num_show');
        add_val = parseInt($(num_show).val());
        return add_val
    };

    // {# 获取单价 #}
    function fn_price(th) {
        var price = $(th).parent().parent().parent().find('.col05').html();
        var get_price = parseFloat(price);
        return get_price
    };

    // {# 小计价格数 #}
    function fn_count_num(th) {
        var get_price = fn_price(th);
        var get_num = fn_value(th);
        get_price *= get_num;
        get_price = get_price.toFixed(2);
        return get_price;
    };

    // {# 小计 #}
    function fn_count(th) {
        var get_price = fn_count_num(th);
        var get_num = fn_value(th);
        if (get_num > 0 && get_num < 1000) {
            $(th).parent().parent().parent().find('.col07').html(get_price + '元');
        }
        else {
            alert('请输入0-1000之间的数');
        }
    };
    $('.num_show').each(function () {
        fn_count(this);
    });


    // {# 失去焦点 计算 #}
    $('.num_show').blur(function () {
        // {# 价格小计 #}
        fn_count(this);
        // {# 计算总价格 #} {# 计算总数量 #}
        var snum_zong = 0;
        var sprice_zong = 0;
        $('.cart_list_td .col01 input').each(function (i) {
            // {# 勾选的才计算 #}
            if ($('.cart_list_td .col01 input').eq(i).prop('checked')) {
                sprice_zong += parseFloat(fn_count_num($('.num_show').eq(i)));
                snum_zong += parseInt(fn_value($('.num_show').eq(i)));
            }
        });
        $('.settlements .col03 em').html(sprice_zong.toFixed(2));
        $('.settlements .col03 b').html(snum_zong);

        var goods_num = $(this).val();
        console.log(goods_num)
        var goods_id = $(this).parent().parent().parent().find('.col08 input').val();
         $.post('/cart/cart_add/',{'goods_id':goods_id,"goods_num":goods_num,'code':1},function (data) {

             //回调函数

        });


    });


    // {# 点击加号 计算 #}
    $('.cart_list_td').delegate('.add', 'click', function () {
        // {# 输入框+1 #}
        fn_value(this);
        if (add_val < 999) {
            $(num_show).val(add_val + 1);
            if ($(this).parent().parent().parent().find('.col01 input').prop('checked')) {
                fn_num_zong();
                var price_zong = parseFloat($('.settlements .col03 em').html());
                price_zong += parseFloat(fn_price(this));
                // {# 总计价格 #}
                $('.settlements .col03 em').html(price_zong.toFixed(2));
            }
        }
        else {
            alert('商品数量不能大于999');
        }
        // {# 小计价格 #}
        fn_count(this);
        var goods_id = $(this).parent().parent().parent().find('.col08 input').val();
         $.post('/cart/cart_add/',{'goods_id':goods_id,'goods_num':1,'code':0},function (data) {

             //回调函数
        });



    });

    // {# 点击减号 计算 #}
    $('.cart_list_td').delegate('.minus', 'click', function () {
        // {# 输入框-1 #}
        fn_value(this);
        if (add_val > 1) {
            $(num_show).val(add_val - 1);
            if ($(this).parent().parent().parent().find('.col01 input').prop('checked')) {
                fn_num_zong();
                var price_zong = parseFloat($('.settlements .col03 em').html());
                price_zong -= parseFloat(fn_price(this));
                // {# 总计价格 #}
                $('.settlements .col03 em').html(price_zong.toFixed(2));
            }
        }
        else {
            alert('商品数量必须大于0');
        }
        // {# 小计价格 #}
        fn_count(this);


        // /点击减号，数据库删除一件商品
        var goods_id = $(this).parent().parent().parent().find('.col08 input').val();
         $.post('/cart/cart_add/',{'goods_id':goods_id,'goods_num':1,'code':2},function (data) {

             //回调函数

        });


    });

    // {#删除商品#}
    $('.cart_list_td .col08 a').click(function () {
        $(this).parent().parent().remove();
        fn_num_zong();  //总数计算
        fn_sumList();　　//商品件数
        var sprice_zong = 0;　//金额
        $('.cart_list_td .col01 input').each(function (i) {
            // {# 勾选的才计算 #}
            if ($('.cart_list_td .col01 input').eq(i).prop('checked')) {
                sprice_zong += parseFloat(fn_count_num($('.num_show').eq(i)));
            }
        });
        $('.settlements .col03 em').html(sprice_zong.toFixed(2));
        //点击删除　购物车的商品
        var goods_id = $(this).next().val();
        $.post('/cart/cart_del/',{'goods_id':goods_id},function (data) {
            //回调函数

        });

    });


});