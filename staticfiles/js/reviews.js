const editButtons = document.getElementsByClassName("btn-edit");
const reviewTitle = document.getElementById("id_title");
const reviewText = document.getElementById("id_content");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality.
* 
* For each button:
* - Retrieves the review's ID on click.
* - Fetches the content of the review.
* - Populates the fields with the review's content for editing.
* - Updates the submit button's text to "Update".
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    let reviewTitleValue = document.getElementById(`title${reviewId}`).innerText;
    
    reviewTitle.value = reviewTitleValue;
    reviewText.value = reviewContent;

    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

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
    let reviewId = e.target.getAttribute("review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}