// Ioana A Mititean
// Exercise 24.3: REST and JSON
// Cupcakes

/**
 * Front-end for cupcakes app: query the cupcakes API and handle updating of the homepage when a
 * new cupcake is added.
 */

// jQuery elements
$cupcakeList = $("#all-cupcakes")
$newCupcakeForm = $("#add-form");
$flavorInput = $("#flavor");
$sizeInput = $("#size");
$ratingInput = $("#rating");
$imageInput = $("#image");


/**
 * Retrieve list of cupcakes from API and display on page.
 */
async function updateCupcakeList() {
    $cupcakeList.empty();
}


/**
 * Handle new cupcake form submission and update homepage to display new cupcake data.
 */
async function handle_add_new_cupcake(event) {
    event.preventDefault();

    console.log("Form has been submitted");

    // TODO: make AJAX request to cupcakes API to add new cupcake using form data
    const flavor = $flavorInput.val();
    const size = $sizeInput.val();
    const rating = $ratingInput.val();
    const image = $imageInput.val();

    await updateCupcakeList();

    console.log(flavor, size, rating, image);
}


$(async function() {
    console.log("DOM loaded");

    await updateCupcakeList();
    $newCupcakeForm.on("submit", handle_add_new_cupcake);
})
