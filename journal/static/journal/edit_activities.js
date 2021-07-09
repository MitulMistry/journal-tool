document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.btn-edit').forEach(function(button) {
        button.onclick = function() {
            const id = button.dataset.id;
            const text = document.querySelector(`#activity-${id}`).innerHTML;
            const span = document.querySelector(`#form-span-${id}`);
            const input = document.createElement('input');
            // input.className = 'form-control';
            input.setAttribute('type', 'text');
            input.setAttribute('id', `input-${id}`);
            input.setAttribute('value', text);
            span.appendChild(input);
        };
    });
});