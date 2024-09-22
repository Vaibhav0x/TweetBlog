document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchBtn');

    function toggleButton() {
        if (searchInput.value.trim() === '') {
            searchButton.disabled = true;
        } else {
            searchButton.disabled = false;
        }
    }

    searchInput.addEventListener('input', toggleButton);

    toggleButton();
});