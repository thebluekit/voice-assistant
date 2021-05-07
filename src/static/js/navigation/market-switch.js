function switchPageInfo() {
    let currentRoute = getCurrentAnchor();
    if (currentRoute == '' || currentRoute == 'market') {
        goToAnchor('add-skill-step-1');
        // setAddSkillSettings();
    } else {
        goToAnchor('market');
        // setMarketSettings();
    }

}

let switchBtn = document.getElementById('switch-to-add-skill-btn');
switchBtn.addEventListener("click", switchPageInfo);