/**
 * Created by python on 17-9-19.
 */
   ;$(function(){
           var total = 0;//商品小计
           var total1 = 0; //商品总计
           var total2 = 0; //商品总金额
           var total_pay = 0; //实付款
           $('.col07').each(function () {
               var count1 = parseInt($(this).prev().text());
               var price = parseFloat($(this).prev().prev().children('span').text());
               total = count1*price;
               $(this).text(total.toFixed(2)+'元');
               total1++;
               total2+=total;
           });
           total_pay = total2 + 10;
           $('.total_goods_count').children('em').text(total1);
           $('.total_goods_count').children('b').text(total2.toFixed(2)+'元');
           $('.total_pay').children('b').text(total_pay.toFixed(2)+'元');

       });