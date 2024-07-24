// Fetch and display the products from the API
/*fetch('/api/candles')
    .then(response => response.json())
    .then(data => {
        const productList = document.getElementById('product-list');
        data.forEach(candle => {
            const productDiv = document.createElement('div');
            productDiv.classList.add('product');
            productDiv.innerHTML = `
                <h3>${candle.name}</h3>
                <p>${candle.description}</p>
                <p>Price: $${candle.price.toFixed(2)}</p>
                <p>Quantity: ${candle.quantity}</p>
            `;
            productList.appendChild(productDiv);
        });
    })
    .catch(error => console.error('Error fetching products:', error));*/
