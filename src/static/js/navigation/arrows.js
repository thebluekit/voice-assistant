let prevArrow = document.getElementById('arrow-prev');
let nextArrow = document.getElementById('arrow-next');

prevArrow.addEventListener('click', function(event) {
    let currentRoute = getCurrentAnchor();
    if (currentRoute == '' || currentRoute == 'market') {
        clearSkills();
        window.skillShow[0] -= 4;
        window.skillShow[1] -= 4;
        setSkills();
    } else if (currentRoute == 'add-skill-step-1') {} else {
        history.back()
    }
});

nextArrow.addEventListener('click', function(event) {
    let currentRoute = getCurrentAnchor();
    if (currentRoute == '' || currentRoute == 'market') {
        clearSkills();
        window.skillShow[0] += 4;
        window.skillShow[1] += 4;
        setSkills();
    } else if (currentRoute == 'add-skill-step-1') {
        goToAnchor('add-skill-step-2');
    } else if (currentRoute == 'add-skill-step-2') {
        goToAnchor('add-skill-step-3');
    } else if (currentRoute == 'add-skill-step-3') {
        goToAnchor('skill-was-uploaded');
    }
});