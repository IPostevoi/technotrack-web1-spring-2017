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

        //
        //
        // $(window).on('scroll', function () {
        //     if ($(document).scrollTop() >= $('#menubar').height()) {
        //         $('.col-md-8.col-md-pull-4').removeClass('col-md-8 col-md-pull-4').addClass('col-md-10 col-md-offset-1');
        //     } else {
        //         $('.col-md-10.col-md-offset-1').removeClass('col-md-10 col-md-offset-1').addClass('col-md-8 col-md-pull-4');
        //     }
        // })


        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });


        $(document).on('click', 'a.ajaxlike', function (e) {
            var blog = $(this).data();
            $.ajax({
                url: blog.url,
                method: 'post',
                dataType: 'json',
                success: function (data) {
                    $(".likes-count-" + (blog.blogid)).html(" " + data);
                    $(".glyphicon.glyphicon-heart-empty." + (blog.blogid)).removeClass("glyphicon glyphicon-heart-empty " + (blog.blogid)).addClass("glyphicon glyphicon-heart " + (blog.blogid));
                }

            })
        });

        $(".col-md-10.col-md-offset-1.comments-div").each(function () {

            $(this).load($(this).data('url'));
        });

        window.setInterval(function () {
                    $(".col-md-10.col-md-offset-1.comments-div").each(function () {

            $(this).load($(this).data('url'));
        });
        }, 2000);


        $(document).on('click', 'a.btn.btn-primary.add-comment', function () {
            var data = $(this).data();
        });


        $(document).on('click', 'a.edit-blog-ref', function () {
            var data = $(this).data();
            // $(".modal-body.edit-blog." + data.blogid).each(function () {
                $(".modal-body.edit-blog").load(data['url']);
            });



        $(document).on('submit', '.ajaxform', function () {

            var form = $(this).data();
            $.ajax({
                url: form['url'],
                method: 'POST',
                data: $(this).serialize(),
                success: function(data) {
                                    location.reload();
                                }
        });
            return false;
        });




    });