$(function () {
    $('.gallery').gallery();
});

$(function () {
    $('.calender').pignoseCalender({
        multiple: true,
        select: function (date, obj) {
            obj.calender.parent().next().show().text('You selected ' +
                (date[0] === null ? 'null' : date[0].format('YYYY-MM-DD')) +
                '~' +
                (date[1] === null ? 'null' : date[1].format('YYYY-MM-DD')) +
                '.');
        }
    });
});
