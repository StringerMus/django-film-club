const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-outline-danger");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let movieId = e.target.getAttribute("movie_id");
    deleteConfirm.href = `delete_movie/${movieId}`;
    deleteModal.show();
  });
}