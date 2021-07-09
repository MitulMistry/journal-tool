document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.btn-edit').forEach(function(button) {
        button.onclick = function() {
            const id = button.dataset.id;
            const badge = document.querySelector(`#activity-${id}`);
            const name = badge.innerHTML;
            const span = document.querySelector(`#form-span-${id}`);
            const input = document.createElement('input');
            input.className = 'form-control edit-activity-input';
            input.setAttribute('type', 'text');
            input.setAttribute('id', `input-${id}`);
            input.setAttribute('value', name);
            span.appendChild(input);
            
            // Replace edit button's onclick listener
            button.innerHTML = 'Submit';
            button.onclick = function() {
                const edited_name = input.value;
                
                // Make API PUT request
                fetch(`/activities/${id}/edit`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        name: edited_name
                    })
                })
                .then(response => response.json())
                .then(result => {
                    console.log(result);

                    badge.innerHTML = capitalize(result['name']);
                    input.setAttribute('value', badge.innerHTML);
                });
            };
        };
    });
});

function capitalize(str) {
    return str[0].toUpperCase() + str.substring(1);
}