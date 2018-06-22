$(document).ready(function(){
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },

        timezone: 'local',
        selectable: true,
        selectHelper: true,

        editable: true,
        eventLimit: true,

        events: [
            {
                title: "Test event 1",
                url: 'http://google.com/',
                start: new Date('2018-06-02T09:00'),
                end: new Date('2018-06-02T19:00'),
                id: 1
            },
            {
                title: "Test Event 2",
                start: new Date('2018-06-28T09:00'),
                end: new Date('2018-06-28T19:00'),
                id: 1
            }
        ]


    })
});
