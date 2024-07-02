document.addEventListener('DOMContentLoaded', function() {
    // This event fires once the DOM is fully loaded
    console.log('DOM fully loaded and parsed');

    // Example: Add an event listener to the "Learn More" link
    document.querySelector('.hng-internship a').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action (opening the link directly)
        alert('Opening HNG Internship website...');

        // Open the HNG Internship website in a new tab/window
        window.open('https://hng.tech', '_blank');
    });
});
