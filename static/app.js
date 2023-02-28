// Ioana A Mititean
// Exercise 24.3: REST and JSON
// Cupcakes

/**
 * Front-end for cupcakes app: query the cupcakes API and handle updating of the homepage when a
 * new cupcake is added.
 */

// jQuery elements
$cupcakeSection = $("#all-cupcakes")
$newCupcakeForm = $("#add-form");
$flavorInput = $("#flavor");
$sizeInput = $("#size");
$ratingInput = $("#rating");
$imageInput = $("#image");


/**
 * Retrieve list of cupcakes from API and display on page.
 */
async function updateCupcakeSection() {
    $cupcakeSection.empty();
    console.log("Updating cupcake list");

    const getResp = await axios.get("/api/cupcakes");
    console.log(getResp.data);

    const cupcakes = getResp.data["cupcakes"];

    // Display cupcake data for each cupcake on page
    let $cupcakeData;
    for (const cupcake of cupcakes) {
        $cupcakeData = $(
            `<div>
                <img src="${cupcake["image"]}" style="width:20%">
            </div>
            <div style="margin-bottom:30px">
                <b>Flavor: ${cupcake["flavor"]}</b>
                <ul>
                    <li>Size: ${cupcake["size"]}</li>
                    <li>Rating: ${cupcake["rating"]}</li>
                </ul>
            </div>`);

        $cupcakeSection.append($cupcakeData);
    }
}


/**
 * Handle new cupcake form submission and update homepage to display new cupcake data.
 */
async function handle_add_new_cupcake(event) {
    event.preventDefault();

    const flavor = $flavorInput.val();
    const size = $sizeInput.val();
    const rating = $ratingInput.val();
    const image = $imageInput.val();

    await axios.post("/api/cupcakes", { flavor, size, rating, image });
    await updateCupcakeSection();

    $(this).trigger("reset");
}


$(async function() {
    await updateCupcakeSection();
    $newCupcakeForm.on("submit", handle_add_new_cupcake);
})
