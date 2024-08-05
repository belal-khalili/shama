const cart_item_number = document.getElementById('cart_item_number')
function add_to_cart(product_id){
    console.log(product_id)
    fetch(`http://127.0.0.1:8000/cart/add-to-cart/${product_id}`)
    .then(response => response.json())
    .then((json) => {if (json.status == 'success') {cart_item_number.innerHTML++} else {console.log('item not found')}});
}

    function updateCartItemQuantity(cartItemId, action) {
        fetch('http://127.0.0.1:8000/cart/update-cart-item-quantity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `cart_item_id=${cartItemId}&action=${action}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'updated') {
                document.getElementById(`cart-item-${cartItemId}`).value = data.quantity;
                // location.reload()
            } else if (data.status === 'deleted') {
                document.getElementById(`cart-item-element-${cartItemId}`).remove();
                // location.reload()
            } else {
                console.error(data.message);
            }
        });
    } ;

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

