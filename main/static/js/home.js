var $select1 = $("#year"),
    $select2 = $("#course-code"),
    $options = $select2.find("option");

$select1
    .on("change", function () {
        $select2.html($options.filter('[type="' + this.value + '"]'));
        $select2.selectpicker("refresh");
    })
    .trigger("change");

$(document).ready(function () {

    if ($(this).val() === "" || $(this).val() === "Not set") {

        // $("#course-code").prop("disabled", true);
        $("#course-code").selectpicker("refresh");

    } else {
        // $("#course-code").prop("disabled", true);
        $("#course-code").selectpicker("refresh");
    }

    $("#year").change(function () {

        if ($(this).val() === "Not set" || $(this).val() === "") {
            // $("#course-code").prop("disabled", true);
            $("#course-code").selectpicker("refresh");

        } else {
            // $("#course-code").prop("disabled", true);
            $("#course-code").selectpicker("refresh");
        }
    });

});


$(document).ready(function () {
    $('#summernote').summernote({
        height: 200, // set editor height
        minHeight: 200, // set minimum height of editor
        maxHeight: 340, // set maximum height of editor
        // focus: true // set focus to editable area after initializing summernote
        placeholder: 'Enter description',

        toolbar: [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['table', ['table']],
            // ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    });

    $('.summernote').summernote({
        height: 200, // set editor height
        minHeight: 200, // set minimum height of editor
        maxHeight: 340, // set maximum height of editor
        airMode: true,
        // focus: true // set focus to editable area after initializing summernote
        placeholder: '',

    });

    $('#survey-description-main .note-editable').attr('contenteditable', false);  


});