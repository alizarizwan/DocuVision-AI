async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file first!");
        return;
    }

    // Show loading animation
    document.getElementById("loading").classList.remove("hidden");

    let formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Error processing document!");
        }

        const data = await response.json();

        // Hide loading animation
        document.getElementById("loading").classList.add("hidden");

        // Display results
        document.getElementById("extractedText").innerText = data.extracted_text;
        document.getElementById("category").innerText = `Predicted Category: ${data.category}`;

    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while processing the document.");
        document.getElementById("loading").classList.add("hidden");
    }
}
