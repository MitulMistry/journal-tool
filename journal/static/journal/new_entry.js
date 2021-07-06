document.addEventListener('DOMContentLoaded', function() {
    enable_tooltips();
    set_current_datetime();
})

function enable_tooltips() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
}

function set_current_datetime() {
    const input_date = document.querySelector('#input-date');
    const input_time = document.querySelector('#input-time');    
    const date = new Date();

    const date_string = `${date.getFullYear()}-${format_zero(date.getMonth() + 1)}-${format_zero(date.getDate())}`;

    input_date.value = date_string;
    input_date.setAttribute('max', date_string);
    input_time.value = `${format_zero(date.getHours())}:${format_zero(date.getMinutes())}`;
}

// Format number to ensure leading zero (1 becomes 01)
function format_zero(val) {
    return `${val < 10 ? 0: ''}${val}`;
}