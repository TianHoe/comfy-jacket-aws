function getUrls(input) {
    const img = document.querySelector('#preview_img');
    const removeBtn = document.querySelector('#removeBtn');
    const remove = document.querySelector('#remove_img');
    const uploadBtn = document.querySelector('#uploadBtn');
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            img.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
        removeBtn.style.display = "inline-block";
        uploadBtn.style.display = "none";
        remove.checked = false;
    }
}
function removeImg() {
    const img = document.querySelector('#preview_img');
    const removeBtn = document.querySelector('#removeBtn');
    const remove = document.querySelector('#remove_img');
    const uploadBtn = document.querySelector('#uploadBtn');
    img.src = "/static/images/default_user.png";
    removeBtn.style.display = "none";
    uploadBtn.style.display = "inline-block";
    remove.checked = true;
}