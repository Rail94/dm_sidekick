document.addEventListener("DOMContentLoaded", () => {
    function setupTab(speciesId, buttonId) {
        const speciesSelect = document.getElementById(speciesId);
        const generateBtn = document.getElementById(buttonId);

        speciesSelect.addEventListener("change", () => {
            generateBtn.disabled = false;
        });
    }

    setupTab("speciesSelect", "generateBtn");
    setupTab("speciesSelectNorse", "generateBtnNorse", "norse");
});

function filterTable() {

    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();

    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {

        const text = row.innerText.toLowerCase();

        if (text.includes(filter)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}