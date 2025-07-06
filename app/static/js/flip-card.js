window.addEventListener("load", function () {
    const card = document.getElementById("cardFlip");
    if (card) {
        setTimeout(() => {
            card.style.transform = "rotateY(180deg)";
        }, 300); // ritardo per maggiore effetto visivo
    }
});