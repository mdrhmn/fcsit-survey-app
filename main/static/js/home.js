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