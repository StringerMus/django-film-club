const editButtons = document.getElementsByClassName("btn-edit");
const filmTitle = document.getElementById("id_title");
const filmYear = document.getElementById("id_year");
const filmGenre = document.getElementById("id_genre");
const filmImage = document.getElementById("id_featured_image");
const filmSynopsis = document.getElementById("id_synopsis");
const filmDirector = document.getElementById("id_director");
const reviewForm = document.getElementById("filmForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let movieId = e.target.getAttribute("data-movie-id");
    deleteConfirm.href = `delete_movie/${movieId}`;
    deleteModal.show();
  });
}

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let filmId = e.target.getAttribute("data-movie-id");
    let filmTitle = document.getElementById(`title${filmId}`).innerText;
    let filmYear = document.getElementById(`year${filmId}`).innerText;
    let filmGenre = document.getElementById(`genre${filmId}`).innerText;
    let filmImage = document.getElementById(`featured_image${filmId}`).innerText;
    let filmSynopsis = document.getElementById(`synopsis${filmId}`).innerText;
    let filmDirector = document.getElementById(`director${filmId}`).innerText;
    
    filmTitle.value = filmTitle;
    reviewText.value = reviewContent;
    filmYear.value = filmYear;
    filmGenre.value = filmGenre;
    reviewTitle.value = reviewTitleValue;
    reviewText.value = reviewContent;

    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}