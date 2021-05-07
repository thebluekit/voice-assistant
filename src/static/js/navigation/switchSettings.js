function setMarketSettings() {
    let switchBtn1 = document.getElementById('switch-to-add-skill-btn');
    let titleText = document.getElementById('title-text');
    let titleDescription = document.getElementById('title-description');

    titleText.innerHTML = 'Доступные навыки'
    titleDescription.innerHTML = 'Выберите понравившийся вам навык и добавтье его в свою библиотеку'
    switchBtn1.innerHTML = 'создать'
}

function setAddSkillSettings() {
    let switchBtn1 = document.getElementById('switch-to-add-skill-btn');
    let titleText = document.getElementById('title-text');
    let titleDescription = document.getElementById('title-description');

    titleText.innerHTML = 'Создание навыка'
    titleDescription.innerHTML = 'С легкостью создайте навык, который будет отвечать вашим требованиям'
    switchBtn1.innerHTML = 'маркет'
}

function changedUrl() {
    let currentAnchor = getCurrentAnchor();

    if (currentAnchor == 'add-skill-step-1') {
        loadStep1();
    } else if (currentAnchor == 'add-skill-step-2') {
        loadStep2();
    } else if (currentAnchor == 'add-skill-step-3') {
        loadStep3();
    } else if (currentAnchor == 'skill-was-uploaded') {
        uploadSkill();
    }
    if (currentAnchor == 'market' || currentAnchor == '') {
        setMarketSettings();
    } else if ((currentAnchor == 'add-skill-step-1') || (currentAnchor == 'add-skill-step-2') || (currentAnchor == 'add-skill-step-3') || (currentAnchor == 'skill-was-uploaded')) {
        setAddSkillSettings();
    }
    console.log('Current anchor:', currentAnchor)
}
window.onload = function() {
    window.addEventListener('popstate', changedUrl);
    changedUrl();

}