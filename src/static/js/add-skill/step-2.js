function getWordsFromPhrase(phrase) {
    words = phrase.match(/[a-zA-Zа-яА-Я]+/g);
    setWords(words);
}

function setWords(words) {
    let wordsElem = document.getElementById('words-of-phrase');
    let propDescription = document.getElementById('prop-description');

    wordsElem.innerHTML = '';
    if (words != null) {
        for (let word of words) {
            let wordElem = `<span class="word-of-phrase" onclick="wordClicked(this)">${word}</span>`
            wordsElem.innerHTML += wordElem
        }
        propDescription.classList.remove('none-visability');
    } else {
        propDescription.classList.add('none-visability');
    }

}

function wordClicked(elem) {
    elem.classList.toggle('word-clicked');
}

function addPhrase() {
    let phraseElem = document.getElementById('phrase-input');
    phraseElem.value = '';
    let wordsElem = document.getElementById('words-of-phrase');
    wordsElem.innerHTML = '';

    window.skillObj['phrases'].push(window.currentPhrase);
    updatePhrases(window.skillObj['phrases']);


    window.currentPhrase = {}

}

function editPhrase() {
    let phraseElem = document.getElementById('phrase-input');
    phraseElem.value = '';
    let wordsElem = document.getElementById('words-of-phrase');
    wordsElem.innerHTML = '';

    window.skillObj['phrases'][window.editPhraseIndex] = window.currentPhrase;
    updatePhrases(window.skillObj['phrases']);

    window.currentPhrase = {}
    window.editPhraseIndex = -1;
}

function removePhrase() {
    if (window.editPhraseIndex != -1) {
        window.skillObj['phrases'].splice(window.editPhraseIndex, 1);
        updatePhrases(window.skillObj['phrases']);
        window.currentPhrase = {}
        window.editPhraseIndex = -1;

        let propDescription = document.getElementById('prop-description');
        let removeBtn = document.getElementById('remove-skill-btn');
        let phraseElem = document.getElementById('phrase-input');
        let wordsElem = document.getElementById('words-of-phrase');

        phraseElem.readOnly = false;
        phraseElem.value = '';
        wordsElem.innerHTML = '';
        propDescription.classList.add('none-visability');
        removeBtn.classList.add('none-visability');

    }

}

function updatePhrases(phrases) {
    let phrasesElem = document.getElementById('phrases-container');
    phrasesElem.innerHTML = ''
    for (let phrase of phrases) {
        phrasesElem.innerHTML += `<p class="phrase" onclick="modifyPhrase(this)">${phrase['phrase']}</p>`
    }
}

function modifyPhrase(element) {
    let phraseElement = document.getElementById('phrase-input');

    let removeBtn = document.getElementById('remove-skill-btn');
    removeBtn.classList.remove('none-visability');


    phraseElement.value = element.innerHTML;
    getWordsFromPhrase(phraseElement.value);
    for (let i = 0; i < window.skillObj['phrases'].length; i++) {

        if (window.skillObj['phrases'][i]['phrase'] == element.innerHTML) {
            window.editPhraseIndex = i;
            break;
        }
    }
}

function addSkillProp() {
    let wordsElems = document.getElementsByClassName('word-clicked');
    let btn = document.getElementById('add-smth-btn');
    let propDescription = document.getElementById('prop-description');
    let props = []
    for (let wordElem of wordsElems) {
        props.push(wordElem.innerHTML);
    }

    let phraseE = document.getElementById('phrase-input');

    while (wordsElems.length) wordsElems[0].classList.remove('word-clicked');
    if (btn.innerHTML.indexOf('action') + 1) {

        btn.innerHTML = 'Добавить entity';
        propDescription.innerHTML = 'Шаг 2. Выберите entity фразы';

        let phrase = phraseE.value;
        phraseE.readOnly = true;
        window.currentPhrase['phrase'] = phrase;
        window.currentPhrase['action'] = props;
    } else if (btn.innerHTML.indexOf('entity') + 1) {
        btn.innerHTML = 'Добавить context';
        propDescription.innerHTML = 'Шаг 3. Выберите context фразы';

        window.currentPhrase['entity'] = props;
    } else if (btn.innerHTML.indexOf('context') + 1) {
        btn.innerHTML = 'Добавить action';
        propDescription.innerHTML = 'Шаг 1. Выберите action фразы';
        window.currentPhrase['context'] = props;
        if (window.editPhraseIndex == -1) {
            addPhrase();
        } else {
            editPhrase();
        }

        phraseE.readOnly = false;
        propDescription.classList.add('none-visability');

        let removeBtn = document.getElementById('remove-skill-btn');
        removeBtn.classList.add('none-visability');
        console.log(window.skillObj['phrases'])
    }

}

function loadStep2() {
    window.skillObj["skillStep"] = 2;

    let checkExistInputPhrase = setInterval(function() {
        let phraseElement = document.getElementById('phrase-input');
        if (phraseElement != undefined) {
            phraseElement.addEventListener('input', function() {
                let phraseText = phraseElement.value;
                getWordsFromPhrase(phraseText);
            });
            clearInterval(checkExistInputPhrase);
        }
    }, 100);

    let checkExistPhrasesElem = setInterval(function() {
        let phrasesElem = document.getElementById('phrases-container');
        if (phrasesElem != undefined) {
            phrasesElem.style.maxHeight = phrasesElem.offsetHeight.toString() + "px";
            clearInterval(checkExistPhrasesElem);
        }
    }, 100);


    let checkExistBtn = setInterval(function() {
        let addBtn = document.getElementById('add-smth-btn');
        if (addBtn != undefined) {
            addBtn.addEventListener('click', function() {
                addSkillProp();
            });
            clearInterval(checkExistBtn);
        }
    }, 100);

    let checkExistContainer = setInterval(function() {
        let container = document.getElementById('phrases-container');
        if (container != undefined) {
            updatePhrases(window.skillObj['phrases']);
            clearInterval(checkExistContainer);
        }
    }, 100);

    window.currentPhrase = {};
    window.editPhraseIndex = -1;
}