document.addEventListener('DOMContentLoaded', function() {
    enable_tooltips();
    set_current_datetime();
    initialize_add_activity();
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

function initialize_add_activity() {
    document.querySelector('#add-activity-btn').onclick = function() {

        const form = document.querySelector('#add-activity-form');
        const name = form.value;

        fetch('/activities/new', {
            method: 'POST',
            body: JSON.stringify({
                name: name
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);

            // Check if id and name of newly created activity are returned in response
            if ('id' in result && 'name' in result) {            
                const element_id = `btn-activity-${result['id']}`;

                const checkbox = document.createElement('input');
                checkbox.setAttribute('type', 'checkbox');
                checkbox.className = 'btn-check';
                checkbox.id = element_id;
                checkbox.setAttribute('autocomplete', 'off');
                checkbox.setAttribute('checked', '');

                const label = document.createElement('label');
                label.className = 'btn btn-activity btn-sm';
                label.setAttribute('for', element_id);
                label.innerHTML = capitalize(result['name']);
                
                const div = document.querySelector('#activities-list-div');
                div.appendChild(checkbox);
                div.appendChild(label);

                form.value = '';
            }
        });
    };
}

function capitalize(str) {
    return str[0].toUpperCase() + str.substring(1);
}