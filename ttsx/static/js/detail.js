/**
 * Created by python on 17-9-13.
 */
        ;$(function () {
             // 加减的点击事件
            var value = $(".num_show").val();
            value = parseInt(value);
            $('.num_add').delegate('a', 'click', function () {
                if ($(this).html() == "+") {
                    value += 1;
                } else {
                    value -= 1;
                    if (value <= 1) {
                        value = 1;
                    }
                }
                $('.num_show').val(value);


                // 总价的计算
                var price = $(".show_pirze em").html();
                price = parseFloat(price);
                var sum = value *price;
                sum = sum.toFixed(2);
                $(".total em").html(sum)
            });








        });
