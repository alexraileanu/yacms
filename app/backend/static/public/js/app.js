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
    });
});