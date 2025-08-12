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
