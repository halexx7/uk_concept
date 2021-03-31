//Получатель
var pay = [
    {
        value: "взносы на капитальный ремонт",
        um: "m2",
        standard: "1.3",
        volume: "1.4",
        pricing_plans: "1.5",
        accrued: "1.6",
        coefficient: "1.7",
        subsidies: "1.8",
        recalculations: "1.9",
        total: "1.10"
    },
    {
        value: "Услуги по расчету платы за взнос на капитальный ремонт",
        um: "m2",
        standard: "2.3",
        volume: "2.4",
        pricing_plans: "2.5",
        accrued: "2.6",
        coefficient: "2.7",
        subsidies: "2.8",
        recalculations: "2.9",
        total: "2.10"
    },
    {
        value: "Холодная вода, используемая для целей ГВС",
        um: "m3",
        standard: "3.3",
        volume: "3.4",
        pricing_plans: "3.5",
        accrued: "3.6",
        coefficient: "3.7",
        subsidies: "3.8",
        recalculations: "3.9",
        total: "3.10"
    },
    {
        value: "теплова энергия для целей ГВС",
        um: "Гкал",
        standard: "4.3",
        volume: "4.4",
        pricing_plans: "4.5",
        accrued: "4.6",
        coefficient: "4.7",
        subsidies: "4.8",
        recalculations: "4.9",
        total: "4.10"
    },
    {
        value: "Водоотведение(индив-е потребление)",
        um: "m3",
        standard: "5.3",
        volume: "5.4",
        pricing_plans: "5.5",
        accrued: "5.6",
        coefficient: "5.7",
        subsidies: "5.8",
        recalculations: "5.9",
        total: "5.10"
    },
    {
        value: "Холодное водоснабжение (индив-е потребление)",
        um: "m3",
        standard: "6.3",
        volume: "6.4",
        pricing_plans: "6.5",
        accrued: "6.6",
        coefficient: "6.7",
        subsidies: "6.8",
        recalculations: "6.9",
        total: "6.10"
    },
    {
        value: "Холодное водоснабжение (общедомовые нужды)",
        um: "m3",
        standard: "7.3",
        volume: "7.4",
        pricing_plans: "7.5",
        accrued: "7.6",
        coefficient: "7.7",
        subsidies: "7.8",
        recalculations: "7.9",
        total: "7.10"
    },
    {
        value: "Электроэнергия (день)",
        um: "кВт.ч.",
        standard: "8.3",
        volume: "8.4",
        pricing_plans: "8.5",
        accrued: "8.6",
        coefficient: "8.7",
        subsidies: "8.8",
        recalculations: "8.9",
        total: "8.10"
    },
    {
        value: "Электроэнергия(ночь)",
        um: "кВт.ч.",
        standard: "9.3",
        volume: "9.4",
        pricing_plans: "9.5",
        accrued: "9.6",
        coefficient: "9.7",
        subsidies: "9.8",
        recalculations: "9.9",
        total: "9.10"
    },
    {
        value: "Задолженность(авнс(+), недоплата (-) ОА ЭК Восток",
        um: "кВт.ч.",
        standard: "10.3",
        volume: "10.4",
        pricing_plans: "10.5",
        accrued: "10.6",
        coefficient: "10.7",
        subsidies: "10.8",
        recalculations: "10.9",
        total: "10.10"
    },
    {
        value: "Центральное отопление",
        um: "Гкал",
        standard: "11.3",
        volume: "11.4",
        pricing_plans: "11.5",
        accrued: "11.6",
        coefficient: "11.7",
        subsidies: "11.8",
        recalculations: "11.9",
        total: "11.10"
    },
    {
        value: "Вывоз твердых бытовых отходов",
        um: "m2",
        standard: "12.3",
        volume: "12.4",
        pricing_plans: "12.5",
        accrued: "12.6",
        coefficient: "12.7",
        subsidies: "12.8",
        recalculations: "12.9",
        total: "12.10"
    },
    {
        value: "Содержание и ремонт текущего лифтового хозяйства",
        um: "m2",
        standard: "13.3",
        volume: "13.4",
        pricing_plans: "13.5",
        accrued: "13.6",
        coefficient: "13.7",
        subsidies: "13.8",
        recalculations: "13.9",
        total: "13.10"
    },
    {
        value: "Установка общедомового прибора учета тепловой энергии (ОАО ТеплоТюмени)",
        um: "m2",
        standard: "14.3",
        volume: "14.4",
        pricing_plans: "14.5",
        accrued: "14.6",
        coefficient: "14.7",
        subsidies: "14.8",
        recalculations: "14.9",
        total: "14.10"
    },
    {
        value: "% за рассрочку платежа (ОДПУ) ставка рефинансирования ЦБ РФ (ОАО ТеплоТюмени)",
        um: "%",
        standard: "15.3",
        volume: "15.4",
        pricing_plans: "15.5",
        accrued: "15.6",
        coefficient: "15.7",
        subsidies: "15.8",
        recalculations: "15.9",
        total: "15.10"
    },
    {
        value: "ХВС (в целях содержания общедомового иммущества)",
        um: "m2",
        standard: "16.3",
        volume: "16.4",
        pricing_plans: "16.5",
        accrued: "16.6",
        coefficient: "16.7",
        subsidies: "16.8",
        recalculations: "16.9",
        total: "16.10"
    },
    {
        value: "Электроэнергия в целях содержания общедомового иммущества",
        um: "m2",
        standard: "17.3",
        volume: "17.4",
        pricing_plans: "17.5",
        accrued: "17.6",
        coefficient: "17.7",
        subsidies: "17.8",
        recalculations: "17.9",
        total: "17.10"
    },
    {
        value: "Содержание и ТО общедомового иммущества",
        um: "m2",
        standard: "18.3",
        volume: "18.4",
        pricing_plans: "18.5",
        accrued: "18.6",
        coefficient: "18.7",
        subsidies: "18.8",
        recalculations: "18.9",
        total: "18.10"
    },
    {
        value: "Финансовые мероприятия по решению общего собрания",
        um: "m2",
        standard: "19.3",
        volume: "19.4",
        pricing_plans: "19.5",
        accrued: "19.6",
        coefficient: "19.7",
        subsidies: "19.8",
        recalculations: "19.9",
        total: "19.10"
    }
];

//Конвертим дату в формат - Январь 2021
function convertDate(item) {
    let date = new Date(Date.parse(item))

    switch(date.getMonth()){
        case 0:
            return(` Январь ${date.getFullYear()} `);
            break;
        case 1:
            return(` Февраль ${date.getFullYear()} `);
            break;
        case 2:
            return(` Март ${date.getFullYear()} `);
            break;
        case 3:
            return(` Апрель ${date.getFullYear()} `);
            break;
        case 4:
            return(` Май ${date.getFullYear()} `);
            break;
        case 5:
            return(` Июнь ${date.getFullYear()} `);
            break;
        case 6:
            return(` Июль ${date.getFullYear()} `);
            break;
        case 7:
            return(` Август ${date.getFullYear()} `);
            break;
        case 8:
            return(` Сентябрь ${date.getFullYear()} `);
            break;
        case 9:
            return(` Октябрь ${date.getFullYear()} `);
            break;
        case 10:
            return(` Ноябрь ${date.getFullYear()} `);
            break;
        case 11:
            return(` Декабрь ${date.getFullYear()} `);
            break;
    }
}

const obj ={
    'user': user[0].fields,
    'appartaments': appartaments[0].fields,
    'house': house[0].fields,
    'city': city[0].fields,
    'street': street[0].fields,
    'uk': uk[0].fields,
    'invoice': invoice[0].fields
}

var data = {
    payer: obj,
    payments: pay,
    period: convertDate(obj.invoice.period)
}


// Добавим верхнюю часть Шапки
$('.header__top').append(
    `<p class="header__top--payer"> За <span style="font-weight: bold; font-size: 1.6rem;">${data.period}</span>Плательщик: ${data.payer.user.name} </p>
    <p> Адрес: ${data.payer.street.street}, д.${data.payer.house.number}</p>
    <p> Площащь: ${data.payer.appartaments.sq_appart} м2 Количество проживающих: ${data.payer.appartaments.num_owner}</p>
    <p> Управляющая компания: ${data.payer.invoice.data.uk}</p>`,
);

// Добавим среднюю часть Шапки
$('.header__center').append(
    `<p> получатель платежа: ${data.payer.uk.name}, ${data.payer.uk.requisites}  </p>
     <p> Адрес сайта: <span class="text__period"> ${data.payer.uk.web_addr} </span></p>
     <p> лицевой счет: ${data.payer.user.personal_account} сумма к оплате: <span class="text__sum"> 4872,86 р.</span></p>`
);

$('.header__bottom').append('<table style="width: 606px;"></table>');

$('.header__bottom > table').append(
    `<tr>
        <th>Задолженность/Аванс</th>
        <th>Начислено за месяц</th>
        <th>Перерасчеты</th><th>Субсидии**</th>
        <th>Оплачено в тек.месяце</th>
        <th>Итого к оплате</th>
    </tr>`
);

$('.header__bottom > table').append(
    `<tr class="text__center">
        <td>5480,86</td>
        <td>5601,08</td>
        <td>-313,66</td>
        <td>414,56</td>
        <td>5480,86</td>
        <td>4872,86</td>
    </tr>`
);


// добавим Таблицу расчетов что - за что
$('.body__content').append('<table></table>');

// добавим шапку
$('.body__content > table').append(
    `<tr>
        <th>Виды услуг</th>
        <th>Ед.изм.</th>
        <th>Норматив</th>
        <th>Объем</th>
        <th>Тариф</th>
        <th>Начисленно<br>руб.</th>
        <th>коэф-т<br>руб.</th>
        <th>Субсидии<br>руб.</th>
        <th>Перерасчет<br>руб.</th>
        <th>Итого<br>за расчетный<br>период</th>
    </tr>`
);

// Пройдем циклом по всем элементам массива и сгенерируем строки таблицы
data.payments.forEach(function (item, i, arr) {
    $('.body__content > table').append(
        `<tr>
        <td class="pad__table">${item.value}</td>
        <td class="text__center  pad__table">${item.um}</td>
        <td class="text__right  pad__table">${item.standard}</td>
        <td class="text__right  pad__table">${item.volume}</td>
        <td class="text__right  pad__table">${item.pricing_plans}</td>
        <td class="text__right  pad__table">${item.accrued}</td>
        <td class="text__right  pad__table">${item.coefficient}</td>
        <td class="text__right  pad__table">${item.subsidies}</td>
        <td class="text__right  pad__table">${item.recalculations}</td>
        <td class="text__right  pad__table">${item.total}</td>
    </tr>`
    );
});

//Итого
$('.body__content > table').append(
    `<tr class="table__bold">
        <td colspan="9" style="font-weight: bold;">Итого за расчетный период: </td>
        <td class="text__right  pad__table">4872,86</td>
    </tr>`
);


//Слушаем кнопку Печать
$('#invoice-print').on('click', (function(){
    print();
}));

//Слушаем кнопку Созранить PDF
$('#invoice-pdf').on('click', (function() {
    //Сохраняем в ПДФ
    var pdf = new jsPDF('p', 'pt', 'a4');
    var pdfContainer = document.querySelector('.content');

    //Конвертим в JPEG и сохраняем в PDF
    //Опция scale - задает масштаб относительно разрешения устройства,
    //используем для увеличения разшения pdf
    html2canvas(pdfContainer, {background: "white", scale: 4}).then(function(canvas) {
        pdf.addImage(canvas, "jpeg", 20, 20, 557, 0);
        pdf.save('TEST.pdf');
    });
}));