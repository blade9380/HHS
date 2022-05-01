
"use strict";

const wordEl = document.getElementById('word');
const wrongLettersEl = document.getElementById('wrong-letters');
const playAgainBtn = document.getElementById('play-button');
const popup = document.getElementById('popup-container');
const notification = document.getElementById('notification-container');
const finalMessage = document.getElementById('final-message');
const finalMessageRevealWord = document.getElementById('final-message-reveal-word');

const figureParts = document.querySelectorAll('.figure-part');

const words = ['blue', 'red', 'purple', 'pink', 'orange']
let selectedWord = words[Math.floor(Math.random() * words.length)];

let playable = true;

let correctLetters = [];
let wrongLetters = [];

// Show hidden word
function displayWord() {
	wordEl.innerHTML = `
	${selectedWord.split('').map(letter => `
	<span class="letter">
	${correctLetters.includes(letter) ? letter : ''}</span>`
	).join('')}`;

	// Add Congratulations

	// console.log(wordEl.innerHTML);
	// console.log(wordEl.innerText);
	// console.log(innerWord);
	const innerWord = wordEl.innerText.replace(/\n/g, '');
	if(innerWord === selectedWord) {
	 var source = "../static/mixkit-correct-answer-reward-952.mp3"
 var audio = document.createElement("audio");
 //
 audio.autoplay = true;
 //
 audio.load()
 audio.addEventListener("load", function() {
     audio.play();
 }, true);
 audio.src = source;
	setTimeout(function() {
  stopConfetti();
}, 3000);
		finalMessage.innerText = `Congratulations!, the word: ${selectedWord}`;
		startConfetti();
		finalMessageRevealWord.innerText = '';
		popup.style.display = 'flex';
		playable = false;
	}
}

// Update the wrong letters
function updateWrongLettersEl() {
	wrongLettersEl.innerHTML = `
	${wrongLetters.length > 0 ? '<p>Wrong</p>' : ''}
	${wrongLetters.map(letter => `<span>${letter}</span>`)}
	`;

	figureParts.forEach((part, index) => {
		const errors = wrongLetters.length;
		if(index < errors) {
			part.style.display = 'block';
		}
		else {
			part.style.display = 'none';
		}
	});

	if(wrongLetters.length === figureParts.length) {
		 var source = "../static/mixkit-wrong-answer-fail-notification-946.mp3"
 var audio = document.createElement("audio");
 //
 audio.autoplay = true;
 //
 audio.load()
 audio.addEventListener("load", function() {
     audio.play();
 }, true);
 audio.src = source;
		finalMessage.innerHTML = 'You lost,';
		finalMessageRevealWord.innerHTML = `the word: ${selectedWord}`;
		popup.style.display = 'flex';
		playable = false;
	}
}

// Show notification
function showNotification() {
	notification.classList.add('show');
	setTimeout(() => {
		notification.classList.remove('show');
	}, 2000);
}

// Keydown letter press
window.addEventListener('keydown', e => {
	if (playable) {
		if (e.keyCode >= 65 && e.keyCode <= 90) {
			const letter = e.key.toLowerCase();
			if (selectedWord.includes(letter)) {
				if (!correctLetters.includes(letter)) {
					correctLetters.push(letter);
					displayWord();
				} else {
					showNotification();
				}
			} else {
				if (!wrongLetters.includes(letter)) {
					wrongLetters.push(letter);
					updateWrongLettersEl();
				} else {
					showNotification();
				}
			}
		}
	}
});

displayWord();

// Restart game and play again

playAgainBtn.addEventListener('click', () => {
	playable = true;
	correctLetters.splice(0);
	// correctLetters = [];
	wrongLetters.splice(0);
	// wrongLetters = [];
	selectedWord = words[Math.floor(Math.random() * words.length)];
	displayWord();
	updateWrongLettersEl();
	popup.style.display = 'none';
})


