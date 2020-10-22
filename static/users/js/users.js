const profileForm = document.getElementById('profile-form');
const btnUpdateForm = document.getElementById('update-button');
const btnFinishUpdate = document.getElementById('update');

btnUpdateForm.addEventListener('click', function (event) {
    event.preventDefault();

    profileForm.classList.remove('d-none');
});

btnFinishUpdate.addEventListener('submit', function (event) {
    event.preventDefault();

    profileForm.classList.add('d-none');
})