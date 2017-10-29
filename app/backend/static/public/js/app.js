$(() => {

    // Sidebar Toggler
    function sidebarToggle(toogle) {
        let sidebar = $('#sidebar'),
            padder = $('.content-padder');

        if (toogle) {
            sidebar.css({
                'display': 'block'
            });

            if ($(window).width() > 960) {
                padder.css({
                    marginLeft: sidebar.css('width')
                });
            }
        } else {
            sidebar.css({'display': 'block'});
            sidebar.css('display', 'none');
            padder.css({
                marginLeft: 0
            });
        }
    }

    $('#sidebar_toggle').click(() => {
        let sidebar = $('#sidebar');
        if (sidebar.css('display') === 'none') {
            sidebarToggle(true)
        } else {
            sidebarToggle(false)
        }
    });

    $('#articleContent').froalaEditor({
        heightMin: 400,
        toolbarButtons: ['undo', 'redo' , '|', 'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', 'outdent', 'indent', 'clearFormatting', 'insertTable', 'html'],
        quickInsertTags: [],
        charCounterCount: false
    });

    let bar = $('#progressbar')[0];

    // UIkit.upload('.imageUpload', {
    //
    //     url: '/admin/image/add',
    //     multiple: true,
    //     type: 'POST',
    //     mime: 'image/*',
    //     name: 'file',
    //
    //     loadStart: (e) => {
    //         bar.removeAttribute('hidden');
    //         bar.max =  e.total;
    //         bar.value =  e.loaded;
    //     },
    //
    //     progress: (e) => {
    //         bar.max =  e.total;
    //         bar.value =  e.loaded;
    //
    //     },
    //
    //     loadEnd: (e) => {
    //         bar.max =  e.total;
    //         bar.value =  e.loaded;
    //     },
    //
    //     completeAll: () => {
    //
    //     }
    // });

    UIkit.upload('.imageUpload', {

        url: '/admin/image/add',
        multiple: true,
        type: 'POST',
        mime: 'image/*',
        name: 'file',

        loadStart: (e) => {
            bar.removeAttribute('hidden');
            bar.max =  e.total;
            bar.value =  e.loaded;
        },

        progress: (e) => {
            bar.max =  e.total;
            bar.value =  e.loaded;

        },

        loadEnd: (e) => {
            bar.max =  e.total;
            bar.value =  e.loaded;
        },

        completeAll: (arguments) => {
            let responseType = arguments.responseJSON.cat,
                responseMessage = arguments.responseJSON.msg;

            if(responseType === 'success'){
                    UIkit.notification('<span uk-icon="icon: check"></span> ' + responseMessage, {
                        status: 'primary'
                    });
            } else {
                UIkit.notification('<span uk-icon="icon: close"></span> ' + responseMessage, {
                    status: 'danger',
                });
            }

            setTimeout(() => {
                bar.setAttribute('hidden', 'hidden');
            }, 1000);
        }
    });
});