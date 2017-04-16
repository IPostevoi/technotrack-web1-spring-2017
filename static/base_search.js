/**
 * Created by bakla410 on 16.04.17.
 */
$(document).ready(
    function () {

        for (var key in get_blogs) {
            var value = get_blogs[key];
            //alert(get_blogs[0].title);
        }

        var i = 0;
        var array = new Array();
        while (i < get_blogs.length) {
            blog_obg = new Object();
            blog_obg["title"] = get_blogs[i]["title"];
            blog_obg["website-link"] = "/blogs/blog/" + get_blogs[i]["id"]
            array.push(blog_obg);
            i++;
        }

        var options = {

            data: array,

            getValue: "title",

            list: {
                match: {
                    enabled: true
                }
            },

            template: {
                maxNumberOfElements: 10,
                type: "links",
                fields: {
                    link: "website-link"
                }
            }
        };

        $("#search-form").easyAutocomplete(options);

        $(window).on('scroll', function () {
            if ($(document).scrollTop() >= $('#menubar').height()) {
                $('.col-md-8.col-md-pull-4').removeClass('col-md-8 col-md-pull-4').addClass('col-md-10 col-md-offset-1');
            } else {
                $('.col-md-10.col-md-offset-1').removeClass('col-md-10 col-md-offset-1').addClass('col-md-8 col-md-pull-4');
            }
        })

    })