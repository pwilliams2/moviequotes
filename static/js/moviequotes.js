//$("#toggle-edit").click(function() {
//   $(".edit-actions").toggleClass("hidden");
//});

var rh = rh || {}; //If rh namespace already exists, use it.
rh.mq = rh.mq || {};

rh.mq.editing = false

rh.mq.enableButtons = function () {
    $("#toggle-edit").click(function () {
        if (rh.mq.editing) {
            rh.mq.editing = false;
            $(".edit-actions").addClass("hidden");  // Hide the buttons
            $(this).html("Edit");
        } else {
            rh.mq.editing = true;
            $(".edit-actions").removeClass("hidden") // Show the buttons
            $(this).html("Done");
        }
    });

    $("#add-quote").click(function () {
        $("#insert-quote-modal .modal-title").html("Add a MovieQuote");
        $(".modal-footer button[type=submit]").html("Add Quote");
         $("#quote").val("");
         $("#movie").val("");
        $(".entity-key").val("").prop("disabled", true);
    });

    $(".edit-movie-quote").click(function () {
        $("#insert-quote-modal .modal-title").html("Edit this MovieQuote");
        $(".modal-footer button[type=submit]").html("Edit Quote");

        quote = $(this).find(".quote").text();
        movie = $(this).find(".movie").text();
        entityKey = $(this).find(".entity-key").text();

        $("#quote").val(quote);
        $("#movie").val(movie);
        $("#entity_key").val(entityKey).prop("disabled", false);
    })

};

rh.mq.attachEventHandlers = function(){
    $("#insert-quote-modal").on('shown.bs.modal',function() {
        $("#quote-input").focus();
    });
};

$(document).ready(function () {
    rh.mq.enableButtons();
    rh.mq.attachEventHandlers();
});