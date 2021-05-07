function getCurrentDate() {
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();

    let d = yyyy + '-' + mm + '-' + dd;
    return d;
}

window.skillObj = {
    "skillName": null,
    "skillDescription": null,
    "phrases": [],
    "skillConstants": [],
    "skillScript": null,
    "skillDate": getCurrentDate(),
    "skillStep": 1
}

function loadStep1() {
    let phraseNameElement = null;

    let checkExistInputPhraseName = setInterval(function() {
        phraseNameElement = document.getElementById('skill-name-input');
        if (phraseNameElement != undefined) {
            if (window.skillObj["skillName"] !== null) {
                phraseNameElement.value = window.skillObj["skillName"];
            }

            phraseNameElement.addEventListener('input', function() {
                let phraseText = phraseNameElement.value;
                window.skillObj['skillName'] = phraseText;
            });
            clearInterval(checkExistInputPhraseName);
        }
    }, 100);

    let checkExistInputPhraseDescription = setInterval(function() {
        phraseDescriptionElement = document.getElementById('skill-description-input');
        if (phraseDescriptionElement != undefined) {
            if (window.skillObj["skillDescription"] !== null) {
                phraseDescriptionElement.value = window.skillObj["skillDescription"];
            }
            phraseDescriptionElement.addEventListener('input', function() {
                let phraseText = phraseDescriptionElement.value;
                window.skillObj['skillDescription'] = phraseText;
            });
            clearInterval(checkExistInputPhraseDescription);
        }
    }, 100);

    nextArrow.addEventListener('click', function(event) {
        console.log(window.skillObj)
    });
}