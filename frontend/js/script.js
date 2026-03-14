// Mock AJAX calls with backend logic
function signup() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    // You can connect this to Python backend via fetch/post
    alert("Sign up successful for " + email);
    window.location.href = "login.html";
}

function logout() {
    alert("Logged out!");
    window.location.href = "login.html";
}

function addProduct() {
    let name = document.getElementById("name").value;
    let sku = document.getElementById("sku").value;
    let category = document.getElementById("category").value;
    let unit = document.getElementById("unit").value;
    let reorder = document.getElementById("reorder").value;

    alert(`Product added: ${name} (${sku})`);
}

function receiveStock() {
    let sku = document.getElementById("receiveSKU").value;
    let warehouse = document.getElementById("receiveWarehouse").value;
    let qty = document.getElementById("receiveQty").value;

    alert(`Received ${qty} of ${sku} at ${warehouse}`);
}

function deliverStock() {
    let sku = document.getElementById("deliverSKU").value;
    let warehouse = document.getElementById("deliverWarehouse").value;
    let qty = document.getElementById("deliverQty").value;

    alert(`Delivered ${qty} of ${sku} from ${warehouse}`);
}

function transferStock() {
    let sku = document.getElementById("transferSKU").value;
    let fromW = document.getElementById("fromWarehouse").value;
    let toW = document.getElementById("toWarehouse").value;
    let qty = document.getElementById("transferQty").value;

    alert(`Transferred ${qty} of ${sku} from ${fromW} to ${toW}`);
}