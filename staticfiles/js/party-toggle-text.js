function toggleText() {
    const moreText = document.getElementById('more-text');
    const toggleButton = document.getElementById('toggle-button');

    if (moreText.classList.contains('d-none')) {
        moreText.classList.remove('d-none');
        toggleButton.innerText = 'Show Less';
    } else {
        moreText.classList.add('d-none');
        toggleButton.innerText = 'Show More';
    }
}

// When the "Click Here" button is clicked, show the volunteer form
document.getElementById("volunteerBtn").addEventListener("click", function () {
    document.getElementById("volunteerForm").style.display = "block";
});

// When the "Close" button is clicked, hide the volunteer form
document.getElementById("closeBtn").addEventListener("click", function () {
    document.getElementById("volunteerForm").style.display = "none";
});

document.getElementById('concernsBtn').addEventListener('click', function() {
    // Show the form when the button is clicked
    document.getElementById('concernsForm').style.display = 'block'; // Show form
});

document.getElementById('closeConcernsForm').addEventListener('click', function() {
    // Hide the form and show the image again when the close button is clicked
    document.getElementById('concernsImage').style.display = 'block'; // Show image again
    document.getElementById('concernsForm').style.display = 'none'; // Hide form
});


