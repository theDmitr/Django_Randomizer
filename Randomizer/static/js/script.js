var random_digit_element = document.getElementById('random_digit');

var elements = document.getElementsByClassName('sign');
elements[0].addEventListener('click', refresh_number);

function refresh_number() {
    fetch('https://18ae-78-106-182-90.ngrok-free.app/random?' + new URLSearchParams({
            'start': 0,
            'end': 10000,
        }), {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        })
        .then(response => response.json())
        .then(response => random_digit_element.innerHTML = response['random_digit'])
}
