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
            ['font', ['bold', 'underline', 'italic', 'clear']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['table', ['table']],
            ['insert', ['link']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    });

    $('.summernote').summernote({
        height: 200, // set editor height
        minHeight: 200, // set minimum height of editor
        maxHeight: 340, // set maximum height of editor
        airMode: false,
        disableDragAndDrop: true,
        toolbar: [],
        // focus: true // set focus to editable area after initializing summernote
        placeholder: '',

    });

    $("#survey-description-main .note-resizebar").removeClass("note-resizebar")
    $('#survey-description-main .note-editable').attr('contenteditable', false);

    $(".accordion_search_bar").on("keypress click input", function () {
        let search_id = $(this).attr('id');

        let input = $(this).val();
        input = input.toLowerCase();

        // console.log('phenomena of staying up late among fsktm students'.includes(input))
        // console.log('financial impact of covid -19 on um students'.includes(input))

        let x = $('.card.' + search_id + ' span.survey_title') // document.getElementsByClassName("survey_title")
        let y = $('.card.' + search_id + ' textarea.summernote') // document.getElementsByClassName('summernote')
        let z = $('.card.' + search_id + ' input.PIC_name') // document.getElementsByClassName('PIC_name')

        for (i = 0; i < x.length; i++) {
            if (!x[i].innerHTML.toLowerCase().includes(input) && !y[i].innerHTML.toLowerCase().includes(input) && !z[i].value.toLowerCase().includes(input)) {
                // console.log(x[i].innerHTML.toLowerCase());
                // console.log(y[i].innerHTML.toLowerCase())
                // console.log(z[i].innerHTML.toLowerCase())
                // console.log(x[i].parentNode.parentNode.parentNode.parentNode.parentNode.id)
                $("#" + x[i].parentNode.parentNode.parentNode.parentNode.parentNode.id).hide()
            }
            else {
                // console.log(x[i].innerHTML.toLowerCase())
                // console.log(y[i].innerHTML.toLowerCase())
                // console.log(z[i].innerHTML.toLowerCase())
                // console.log(x[i].parentNode.parentNode.parentNode.parentNode.parentNode.id)
                $("#" + x[i].parentNode.parentNode.parentNode.parentNode.parentNode.id).show()
            }
        }
    });

    var iso = new Date().toISOString();
    var minDate = iso.substring(0, iso.length - 14);

    $("#expiry-date").attr("min", minDate);

});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})