const cart_item_number = document.getElementById('cart_item_number')
function add_to_cart(product_id){
    fetch(`http://127.0.0.1:8000/cart/add-to-cart/${product_id}`)
    .then(response => response.json())
    .then(data => cart_item_number.innerHTML++)
}