/**
 * Created by bakla410 on 17.04.17.
 */

$(document).ready(
    function () {
        $(window).on('scroll', function () {
            if ($(document).scrollTop() >= $('#menubar').height()) {
                $('.col-md-8.col-md-pull-4').removeClass('col-md-8 col-md-pull-4').addClass('col-md-10 col-md-offset-1');
                $("#menubar").hide();
            } else {
                $('.col-md-10.col-md-offset-1').removeClass('col-md-10 col-md-offset-1').addClass('col-md-8 col-md-pull-4');
                $("#menubar").show();
            }
        });
    });