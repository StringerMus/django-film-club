const editButtons = document.getElementsByClassName("btn-edit");
const filmTitleInput = document.getElementById("id_title");
const filmYearInput = document.getElementById("id_year");
const filmGenreInput = document.getElementById("id_genre");
const filmSynopsisInput = document.getElementById("id_synopsis");
const filmDirectorInput = document.getElementById("id_director");
const filmForm = document.getElementById("filmForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality.
* 
* For each button in the `deleteButtons`:
* - Retrieves the ID on click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let movieId = e.target.getAttribute("data-movie-id");
    deleteConfirm.href = `delete_movie/${movieId}`;
    deleteModal.show();
  });
}

/** 
* For each button:
* - Retrieves the film's ID on click.
* - Fetches the content of the corresponding film.
* - Populates the fields with the films's content for editing.
* - Updates the submit button's text to "Update".
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let filmId = e.target.getAttribute("data-movie-id");
    let filmTitle = document.getElementById(`title${filmId}`).innerText;
    let filmYear = document.getElementById(`year${filmId}`).innerText;
    let filmGenre = document.getElementById(`genre${filmId}`).innerText;
    let filmSynopsis = document.getElementById(`synopsis${filmId}`).innerText;
    let filmDirector = document.getElementById(`director${filmId}`).innerText;

    filmTitleInput.value = filmTitle;
    filmYearInput.value = filmYear;
    filmGenreInput.value = filmGenre;
    filmSynopsisInput.value = filmSynopsis;
    filmDirectorInput.value = filmDirector;

    submitButton.innerText = "Update";
    filmForm.setAttribute("action", `edit_film/${filmId}`);
  });
}