// static/js/main.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const fileInput = document.querySelector('input[type="file"]');

    if (!form || !fileInput) {
        return; // Not on prediction page
    }

    form.addEventListener("submit", function (e) {
        if (!fileInput.files || fileInput.files.length === 0) {
            e.preventDefault();
            alert("Please select an image before submitting.");
            return false;
        }

        const file = fileInput.files[0];
        const allowedTypes = ["image/jpeg", "image/png", "image/jpg"];

        if (!allowedTypes.includes(file.type)) {
            e.preventDefault();
            alert("Invalid file type. Please upload a JPG or PNG image.");
            return false;
        }

        const maxSizeMB = 5;
        const maxSizeBytes = maxSizeMB * 1024 * 1024;

        if (file.size > maxSizeBytes) {
            e.preventDefault();
            alert("File too large. Maximum allowed size is 5 MB.");
            return false;
        }
    });
});
