function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked') ? document.querySelector('[name=drink]:checked').value : '';
    //присваивается значение переменной, иначе пустое значение

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar 
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj) 
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб.`;
        document.querySelector('#pay').style.display = 'block';
    })
}

function pay() {
    const card_num = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const name = document.querySelector('[name=name]').value;

    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;

    const obj = {
        "method": "pay",
        "params": {
            card: card_num,
            cvv: cvv,
            name: name,
            milk: milk,
            sugar: sugar,
            price: document.querySelector('#price').textContent.split('Цена напитка: ')[1].split(' руб.')[0]  // Добавляем рассчитанную цену в объект params
        //.split('Цена напитка: ') разделяет текстовое содержимое на массив строк, используя "Цена напитка: " как разделитель. 
        //Это нужно для удаления первой части текста, чтобы осталось только значение цены.
        // [1] выбирает второй элемент (индекс 1) из результирующего массива.
        //.split(' руб.') разделяет полученное значение на массив строк, используя " руб." как разделитель. Это нужно для удаления текста " руб." в конце значения цены.
        //[0] выбирает первый элемент (индекс 0) из результирующего массива, чтобы получить итоговое значение цены напитка.
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#price').innerHTML = `Ошибка: ${data.error}`;
        } else {
            document.querySelector('#price').innerHTML = data.result;
            document.querySelector('#pay').style.display = 'none';  // Скрываем блок оплаты после успешной оплаты
            document.querySelector('#refund').style.display = 'block';  // Показываем кнопку "Отмена оплаты" после успешной оплаты
        }
    });
}

function refund() {
    const card_num = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const name = document.querySelector('[name=name]').value;

    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;

    const obj = {
        "method": "refund",
        "params": {
            card: card_num,
            cvv: cvv,
            name: name,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#price').innerHTML = `Ошибка: ${data.error}`;
        } else {
            document.querySelector('#price').innerHTML = data.result;
            document.querySelector('#refund').style.display = 'none';  // Скрываем кнопку "Отмена оплаты"
            document.querySelector('#pay').style.display = 'block';  // Показываем блок оплаты после успешного возврата
        }
    });
}