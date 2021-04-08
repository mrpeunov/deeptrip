let nowDate = new Date(),
    nowDateNumber = nowDate.getDate(),
    nowMonth = nowDate.getMonth(),
    nowYear = nowDate.getFullYear(),
    container = document.getElementById('month-calendar'),
    monthContainer = container.getElementsByClassName('month-name')[0],
    yearContainer = container.getElementsByClassName('year-name')[0],
    daysContainer = container.getElementsByClassName('days')[0],
    prev = container.getElementsByClassName('prev')[0],
    next = container.getElementsByClassName('next')[0],
    monthName = ['январь','февраль','март','апрель','май','июнь',
        'июль','август','сентябрь','октябрь','ноябрь','декабрь'],
    monthNameParent = ['января','февраля','марта','апреля','мая','июня',
        'июля','августа','сентября','октября','ноября','декабря'];

let choiceMonth = nowMonth;
let choiceYear = nowYear;
let choiceDay = nowDateNumber;

function setMonthCalendar(year,month) {
    let monthDays = new Date(year, month + 1, 0).getDate(),
        monthPrefix = new Date(year, month, 0).getDay(),
        monthDaysText = '';

    monthContainer.textContent = monthName[month];
    yearContainer.textContent = year;
    daysContainer.innerHTML = '';

    if (monthPrefix > 0){
        for (let i = 1; i <= monthPrefix; i++){
            monthDaysText += '<li></li>';
        }
    }

    for (let i = 1; i <= monthDays; i++){
        monthDaysText += '<li class="day" data-day="' + i +
            '" data-month="' + month +
            '" data-year="' + year +
            '">' + i + ' </li>';
    }

    daysContainer.innerHTML = monthDaysText;



    let days = daysContainer.getElementsByTagName('li');


    //выбираем уже выбранное
    if(month === choiceMonth && year === choiceYear){
        days[monthPrefix + choiceDay - 1].classList.add('date-choice');
        update_date();
    }

    //зачеркиваем до текущего числа в этом месяце
    if (month === nowMonth && year === nowYear) {
        for (let i = 0; i <= monthDays; i++) {
            if (i < nowDateNumber) {
                days[monthPrefix + i - 1].classList.add('date-close');
            }
        }
    }

    //зачёркиваем месяца и года до сегодняшнего дня и после года от сегодняшнего дня
    if ((month < nowMonth && year === nowYear) ||
        (year < nowYear) ||
        (year > nowYear + 1) ||
        (year > nowYear && month > nowMonth)){
        for (let i = 1; i <= monthDays; i++) {
            days[monthPrefix + i - 1].classList.add('date-close');
        }
    }

    let $days = $('.day');

    $days.on('click', function () {
        choiceOnClick($(this));
    })
}

setMonthCalendar(nowYear,nowMonth);

prev.onclick = function () {
    let curDate = new Date(yearContainer.textContent,
        monthName.indexOf(monthContainer.textContent));

    curDate.setMonth(curDate.getMonth() - 1);

    let curYear = curDate.getFullYear(),
        curMonth = curDate.getMonth();

    setMonthCalendar(curYear,curMonth);
}

next.onclick = function () {
    let curDate = new Date(yearContainer.textContent,
        monthName.indexOf(monthContainer.textContent));

    curDate.setMonth(curDate.getMonth() + 1);

    let curYear = curDate.getFullYear(),
        curMonth = curDate.getMonth();

    setMonthCalendar(curYear,curMonth);
}

$('.day').on('click', function () {
    choiceOnClick($(this));
})

function choiceOnClick($elem) {
    if(!$elem.hasClass('date-close')){
        $('.day').removeClass("date-choice");
        $elem.addClass("date-choice");
        choiceDay = parseInt($elem.attr("data-day"));
        choiceMonth = parseInt($elem.attr("data-month"));
        choiceYear = parseInt($elem.attr("data-year"));
        update_date();
    }
}

function update_date() {
    $(".booking-date").html(choiceDay + " " +
            monthNameParent[choiceMonth] + " " + choiceYear);
}