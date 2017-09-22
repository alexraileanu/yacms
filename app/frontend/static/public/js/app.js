$(() => {
    $('#commentContent').froalaEditor({
        heightMin: 200,
        toolbarButtons: ['undo', 'redo' , '|', 'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', 'outdent', 'indent', 'clearFormatting', 'insertTable', 'html'],
        quickInsertTags: [],
        charCounterCount: false
    });
});