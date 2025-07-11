let rotation = 0;

const button = document.getElementById("rotateButton");

button.addEventListener("click", () => {
    rotation += 360;
    button.style.transform = `rotate(${rotation}deg)`;
    button.style.transition = 'transform 0.6s ease';
    roundIncrement();
});

function roundIncrement() {
    let roundSpan = document.getElementById('round');
    const currentRound = parseInt(roundSpan.textContent);
    roundSpan.textContent = currentRound + 1;
}

function getValues() {
    const name = document.getElementById('name').value;
    const bonus = parseInt(document.getElementById('bonus-initiative').value) || 0;
    return { name, bonus };

}

function rollDice(bonus) {
    const roll = Math.floor(Math.random() * 20) + 1;
    let initiative = roll + bonus;
    if (initiative <= 0) {
        initiative = 1;
    }
    return initiative;
}

function sumDamage(button) {
    const input = button.previousElementSibling;
    const value = parseInt(input.value) || 0;

    const span = button.nextElementSibling;
    const current = parseInt(span.textContent) || 0;

    const newValue = current + value;

    span.textContent = newValue < 0 ? 0 : newValue;
}

function handleEnter(event, input) {
    if (event.key === "Enter") {
        const button = input.nextElementSibling;
        sumDamage(button);
        input.value = "";
    }
}

function appendRow(name, initiative) {
    const tbody = document.querySelector('#initiative-table tbody');
    const hp = parseInt(document.getElementById('hp').value) || 0;
    const quantity = parseInt(document.getElementById('quantity').value);

    for (let i = 1; i < quantity + 1; i++) {
        const newRow = document.createElement('tr');

        if (i > 1) {
            newRow.innerHTML = `
            <td>${initiative}</td>
            <td style='cursor: pointer;' onclick="this.classList.toggle('strikethrough')">${name + " " + i}</td>
            <td>
            <input class='small-input' type="number" onkeydown="handleEnter(event, this)">
            <button onClick='sumDamage(this)' class="btn-sum">=</button>
            <span class="fw-bold">${hp}</span>
            </td>
        `;
        } else {
            newRow.innerHTML = `
            <td>${initiative}</td>
            <td style='cursor: pointer;' onclick="this.classList.toggle('strikethrough')">${name}</td>
            <td>
            <input class='small-input' type="number" onkeydown="handleEnter(event, this)">
            <button onClick='sumDamage(this)' class="btn-sum">=</button>
            <span class="fw-bold">${hp}</span>
            </td>
        `;
        }


        tbody.appendChild(newRow);
    }
}

function sortTable() {
    const tbody = document.querySelector('#initiative-table tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((a, b) => {
        const aVal = parseInt(a.children[0].textContent);
        const bVal = parseInt(b.children[0].textContent);
        return bVal - aVal;
    });

    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
}

function rollInitiative() {
    const tbody = document.querySelector('#initiative-table tbody');

    document.getElementById('initiative-form').addEventListener('submit', function (e) {
        e.preventDefault();

        const { name, bonus } = getValues();
        const initiative = rollDice(bonus);
        appendRow(name, initiative);

        sortTable();

        this.reset();

    });
}

document.addEventListener('DOMContentLoaded', rollInitiative);