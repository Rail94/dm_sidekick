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

    const groupId = name.toLowerCase().replace(/\s+/g, '-');

    for (let i = 1; i <= quantity; i++) {
        const newRow = document.createElement('tr');
        const displayName = i > 1 ? `${name} ${i}` : name;

        newRow.setAttribute("data-group", groupId);

        newRow.innerHTML = `
    <td>${initiative}</td>
    <td style='cursor: pointer;' 
        onclick="this.classList.toggle('strikethrough')" 
        data-bonus="${document.getElementById('bonus-initiative').value}">
        ${displayName}
    </td>
    <td>
        <input class='small-input' type="number" onkeydown="handleEnter(event, this)">
        <button onClick='sumDamage(this)' class="btn-sum">=</button>
        <span class="fw-bold">${hp}</span>
        <button class="btn btn-delete" onclick="deleteRow(this)">✖</button>
    </td>
`;
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
    document.getElementById('initiative-form').addEventListener('submit', function (e) {
        e.preventDefault();

        const { name, bonus } = getValues();
        const mode = document.getElementById("mode").value;

        let initiative;

        if (mode === "manual") {

            initiative = parseInt(document.getElementById("initiative").value) + bonus;

            if (isNaN(initiative)) {
                alert("Insert initiative value!");
                return;
            }

        } else {
            initiative = rollDice(bonus);
        }

        if (initiative < 1) {
            initiative = 1;
        }

        if (initiative > 99) {
            initiative = 99;
        }

        appendRow(name, initiative, bonus);
        sortTable();

        document.getElementById("name").value = "";
        document.getElementById("bonus-initiative").value = "";
        document.getElementById("hp").value = "";
        document.getElementById("quantity").value = 1;
        document.getElementById("initiative").value = "";

        toggleInitiative();
    });
}

function rerollAll() {
    document.getElementById('rerollButton').addEventListener('click', function () {
        const tbody = document.querySelector('#initiative-table tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));

        const groups = {};

        rows.forEach(row => {
            const groupId = row.dataset.group;
            const bonus = parseInt(row.children[1].dataset.bonus) || 0;

            if (!(groupId in groups)) {
                groups[groupId] = rollDice(bonus);
            }

            row.children[0].textContent = groups[groupId];
        });

        sortTable();
    });
}

function deleteRow(button) {
    const row = button.closest('tr');
    row.remove();
}

document.addEventListener('DOMContentLoaded', () => {
    rollInitiative();
    rerollAll();
});

function toggleInitiative() {

    const mode = document.getElementById("mode").value;
    const container = document.getElementById("initiative-container");
    const input = document.getElementById("initiative");

    if (mode === "manual") {
        container.classList.remove("d-none");
        input.disabled = false;
    } else {
        container.classList.add("d-none");
        input.disabled = true;
        input.value = "";
    }
}

document.getElementById("initiative").disabled = true;