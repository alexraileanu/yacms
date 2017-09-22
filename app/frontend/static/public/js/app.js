$(() => {
    $('#commentContent').froalaEditor({
        heightMin: 200,
        heightMax: 400,
        toolbarButtons: ['undo', 'redo' , '|', 'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', 'outdent', 'indent', 'clearFormatting', 'insertTable', 'html'],
        quickInsertTags: [],
        charCounterCount: false
    });
});