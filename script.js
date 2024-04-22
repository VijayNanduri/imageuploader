document.getElementById('fileInput').addEventListener('change', function(event) {
    console.log("File selected!"); // Add this line to log when a file is selected
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const image = new Image();
            image.src = e.target.result;
            document.getElementById('imageContainer').appendChild(image);
            // Use AJAX to upload the file to the server
            uploadFile(file);
        };
        reader.readAsDataURL(file);
    }
});


function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.error('Error:', error));
}


function clearFiles() {
    // Clear the imageContainer
    document.getElementById('imageContainer').innerHTML = '';

    // Send a POST request to the /clear route to remove files from the server
    fetch('/clear', {
        method: 'POST'
    })
    .then(() => console.log('Files cleared'))
    .catch(error => console.error('Error clearing files:', error));
}


