function increaseQty() {
    let qtyInput = document.getElementById("quantity");
    qtyInput.value = parseInt(qtyInput.value) + 1;
}

function decreaseQty() {
    let qtyInput = document.getElementById("quantity");
    if (parseInt(qtyInput.value) > 1) {
        qtyInput.value = parseInt(qtyInput.value) - 1;
    }
}
// Global bana do
window.increaseQty = increaseQty;
window.decreaseQty = decreaseQty;