// Part Two - Movie App!
// Build an application that uses jQuery to do the following:
// - Contains a form with two inputs for a title and rating along with a button to submit the form.
// - When the form is submitted, capture the values for each of the inputs and append them to the
//   DOM along with a button to remove each title and rating from the DOM.
// - When the button to remove is clicked, remove each title and rating from the DOM.

$('#submitter').on('click', function(e){
    e.preventDefault();
    let title = $('.form-input').eq(0).val();
    let rating = $('.form-input').eq(1).val();
    const para = $('<p>', {text: `Title: ${title}, Rating: ${rating} `});
    const btn = $('<button>', {text: 'Remove'}).on('click', function(e){
        $(this).parent().remove();
    });
    $('form').append(para.append(btn));
    $("#movieForm").trigger("reset");
});
