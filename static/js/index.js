const copyButton = document.getElementById('copy');
const generateButton = document.getElementById('generate');
const loadingNotification = document.getElementById('load-notif');
const download_button = document.getElementById('download');

download_button.addEventListener('click', function () { window.location = '/download_password'; alert('OK')});

copyButton.addEventListener('click', function () {
	const password = document.getElementById('password').value;
	navigator.clipboard.writeText(password)
		.then(() => {
			alert('Password copied to clipboard');
		})
		.catch(err => {
			console.error('Failed to copy text: ', err);
		});
});

generateButton.addEventListener('click', function () {
	loadingNotification.style.display = 'block';
	const length = parseInt(document.getElementById('length').value);
	const uppercase = document.getElementById('uppercase').checked;
	const lowercase = document.getElementById('lowercase').checked;
	const numbers = document.getElementById('numbers').checked;
	const symbols = document.getElementById('symbols').checked;

	fetch('/generate_password', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({
			quantity: 1,
			length: length,
			uppercase: uppercase.toString(),
			lowercase: lowercase.toString(),
			numbers: numbers.toString(),
			symbols: symbols.toString(),
		})
	})
		.then(response => response.text())
		.then(data => {
			document.getElementById("password").value = data;
			loadingNotification.style.display = 'none';
		})
		.catch(error => {
			console.error('Error:', error);
			loadingNotification.style.display = 'none';
		});
});
