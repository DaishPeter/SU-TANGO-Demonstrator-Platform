document.addEventListener('DOMContentLoaded', () => {
    updateGrid();

    const gridSizeSelector = document.getElementById('gridSize');
    gridSizeSelector.addEventListener('change', updateGrid);
});

function updateGrid() {
    const grid = document.getElementById('glyphGrid');
    if (!grid) {
        console.warn('glyphGrid container not found');
        return;
    }
    const gridSize = parseInt(document.getElementById('gridSize').value);
    grid.innerHTML = '';
    grid.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;

    for (let i = 0; i < gridSize * gridSize; i++) {
        const canvas = document.createElement('canvas');
        canvas.className = 'glyph-canvas';
        canvas.width = 64;
        canvas.height = 64;
        canvas.dataset.index = i;
        canvas.onclick = () => handleGlyphClick(i);
        grid.appendChild(canvas);
        renderGlyph(canvas, i);
    }

    const targetCanvas = document.getElementById('targetGlyph');
    if (targetCanvas) {
        renderGlyph(targetCanvas, 'T'); // 'T' for Target or any label you prefer
    }

}

function handleGlyphClick(index) {
    console.log(`Glyph ${index + 1} clicked`);
    // Future: update latent vector, re-render grid, etc.
}
function renderGlyph(canvas, label) {
    const ctx = canvas.getContext('2d');

    // Background
    ctx.fillStyle = '#f0f0f0';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Glyph label
    ctx.fillStyle = '#333';
    ctx.font = 'bold 20px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(label, canvas.width / 2, canvas.height / 2);

    // Optional border
    ctx.strokeStyle = '#ccc';
    ctx.strokeRect(0, 0, canvas.width, canvas.height);
}


function showFlashMessage(text) {
    const flash = document.getElementById('flashMessage');
    flash.textContent = text;
    flash.classList.remove('d-none');

    setTimeout(() => {
        flash.classList.add('d-none');
    }, 2000); // Hide after 2 seconds
}



const glyphHistory = [];

function handleGlyphClick(index) {
    const label = `Glyph ${index + 1}`;
    showFlashMessage(`${label} clicked`);

    glyphHistory.push(label);
    renderHistory();
}

function renderHistory() {
    const container = document.getElementById('glyphHistory');
    container.innerHTML = '';

    glyphHistory.forEach((label, i) => {
        const item = document.createElement('div');
        item.className = 'glyph-history-item text-center';
        item.innerHTML = `
            <canvas width="85" height="60"></canvas>
            <div class="small mt-1">${i}</div>
        `;
        container.appendChild(item);

        const canvas = item.querySelector('canvas');
        renderGlyph(canvas, label); // Or use label if you prefer
    });
}
