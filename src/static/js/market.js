window.skillShow = [0, 4];

function clearSkills() {
    let skillsContainer = document.getElementById('app');
    skillsContainer.innerHTML = '';
}

function addSkillView(skillIndex, skillDate, skillName, skillDescription, skillColor) {
    let skillsContainer = document.getElementById('app');
    let skillHTML = `<div class="skill-box">
    <div class="skill-content ${skillColor}">
        <h1 class="skill-number">${skillIndex}</h1>
        <div class="skill-description">
            <p class="skill-date">${skillDate}</p>
            <h2 class="skill-name">${skillName}</h2>
            <p class="skill-description-text">${skillDescription}</p>
        </div>
    </div>
    <div class="skill-options">
        <div class="options-box" id="edit-skill" onclick='editSkill(this)'>
            <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 477.873 477.873" style="enable-background:new 0 0 477.873 477.873;" xml:space="preserve">
                <path d="M392.533,238.937c-9.426,0-17.067,7.641-17.067,17.067V426.67c0,9.426-7.641,17.067-17.067,17.067H51.2
                    c-9.426,0-17.067-7.641-17.067-17.067V85.337c0-9.426,7.641-17.067,17.067-17.067H256c9.426,0,17.067-7.641,17.067-17.067
                    S265.426,34.137,256,34.137H51.2C22.923,34.137,0,57.06,0,85.337V426.67c0,28.277,22.923,51.2,51.2,51.2h307.2
                    c28.277,0,51.2-22.923,51.2-51.2V256.003C409.6,246.578,401.959,238.937,392.533,238.937z"/>
                <path d="M458.742,19.142c-12.254-12.256-28.875-19.14-46.206-19.138c-17.341-0.05-33.979,6.846-46.199,19.149L141.534,243.937
                    c-1.865,1.879-3.272,4.163-4.113,6.673l-34.133,102.4c-2.979,8.943,1.856,18.607,10.799,21.585
                    c1.735,0.578,3.552,0.873,5.38,0.875c1.832-0.003,3.653-0.297,5.393-0.87l102.4-34.133c2.515-0.84,4.8-2.254,6.673-4.13
                    l224.802-224.802C484.25,86.023,484.253,44.657,458.742,19.142z M434.603,87.419L212.736,309.286l-66.287,22.135l22.067-66.202
                    L390.468,43.353c12.202-12.178,31.967-12.158,44.145,0.044c5.817,5.829,9.095,13.72,9.12,21.955
                    C443.754,73.631,440.467,81.575,434.603,87.419z"/>
            </svg>
    
        </div>
        <div class="options-box" id="install-skill" onclick='installSkill(this)'>
            <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 477.867 477.867" style="enable-background:new 0 0 477.867 477.867;" xml:space="preserve">
                <path d="M443.733,307.2c-9.426,0-17.067,7.641-17.067,17.067v102.4c0,9.426-7.641,17.067-17.067,17.067H68.267
                    c-9.426,0-17.067-7.641-17.067-17.067v-102.4c0-9.426-7.641-17.067-17.067-17.067s-17.067,7.641-17.067,17.067v102.4
                    c0,28.277,22.923,51.2,51.2,51.2H409.6c28.277,0,51.2-22.923,51.2-51.2v-102.4C460.8,314.841,453.159,307.2,443.733,307.2z"/>
                <path d="M335.947,295.134c-6.614-6.387-17.099-6.387-23.712,0L256,351.334V17.067C256,7.641,248.359,0,238.933,0
                    s-17.067,7.641-17.067,17.067v334.268l-56.201-56.201c-6.78-6.548-17.584-6.36-24.132,0.419c-6.388,6.614-6.388,17.099,0,23.713
                    l85.333,85.333c6.657,6.673,17.463,6.687,24.136,0.031c0.01-0.01,0.02-0.02,0.031-0.031l85.333-85.333
                    C342.915,312.486,342.727,301.682,335.947,295.134z"/>
            </svg>
        </div>
        <div class="options-box" id="remove-skill">
            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve">
                <path d="M425.298,51.358h-91.455V16.696c0-9.22-7.475-16.696-16.696-16.696H194.855c-9.22,0-16.696,7.475-16.696,16.696v34.662
                    H86.704c-9.22,0-16.696,7.475-16.696,16.696v51.357c0,9.22,7.475,16.696,16.696,16.696h5.072l15.26,359.906
                    c0.378,8.937,7.735,15.988,16.68,15.988h264.568c8.946,0,16.302-7.051,16.68-15.989l15.259-359.906h5.073
                    c9.22,0,16.696-7.475,16.696-16.696V68.054C441.994,58.832,434.519,51.358,425.298,51.358z M211.551,33.391h88.9v17.967h-88.9
                    V33.391z M372.283,478.609H139.719l-14.522-342.502h261.606L372.283,478.609z M408.602,102.715c-15.17,0-296.114,0-305.202,0
                    V84.749h305.202V102.715z"/>
                <path d="M188.835,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.475,16.696,16.696,16.696
                    c9.22,0,16.696-7.475,16.696-16.696V204C205.53,194.779,198.055,187.304,188.835,187.304z"/>
                <path d="M255.998,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.474,16.696,16.696,16.696
                    c9.22,0,16.696-7.475,16.696-16.696V204C272.693,194.779,265.218,187.304,255.998,187.304z"/>
                <path d="M323.161,187.304c-9.22,0-16.696,7.475-16.696,16.696v206.714c0,9.22,7.475,16.696,16.696,16.696
                    s16.696-7.475,16.696-16.696V204C339.857,194.779,332.382,187.304,323.161,187.304z"/>
       
            </svg>
        </div>
    </div>
    </div>`;

    // let t = skillHTML.getElementsByClassName('options-box');
    // console.log(t);
    //     let nextArrow = document.getElementById('arrow-next');

    // prevArrow.addEventListener('click', function(event) {
    //     let currentRoute = getCurrentAnchor();
    //     if (currentRoute == '' || currentRoute == 'market') {
    //         clearSkills();
    //         window.skillShow[0] -= 4;
    //         window.skillShow[1] -= 4;
    //         setSkills();
    //     } else if (currentRoute == 'add-skill-step-1') {} else {
    //         history.back()
    //     }
    // });

    skillsContainer.innerHTML += skillHTML;
}

function installSkill(element) {
    let skillId = getSkillId(element);
    console.log(skillId);
}

function editSkill(element) {
    let skillId = getSkillId(element);
    console.log(skillId);
}

function getSkillId(btnElement) {
    let mainElement = btnElement.parentElement.parentElement;
    let skillElement = mainElement.getElementsByClassName('skill-content')[0];

    let skillId = skillElement.getElementsByClassName('skill-number')[0].innerHTML;
    skillId = parseInt(skillId) - 1;

    return skillId;
}

const getAllSkillsUrl = '/getAllSkills'

function getAllSkills() {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = (e) => {
            if (xhr.readyState !== 4) {
                return;
            }
            if (xhr.status === 200) {
                let res = JSON.parse(xhr.responseText);
                resolve(res);
            } else {
                console.warn('request_error');
            }
        };
        let url = getAllSkillsUrl;
        xhr.open('GET', url);
        xhr.send();
    });
}

function createEmptySkill() {
    let skillsContainer = document.getElementById('app');
    skillsContainer.innerHTML += '<div class="skill-box"></div>'
}

function setSkills() {
    let skillColors = ['skill-green', 'skill-purple', 'skill-red', 'skill-gray'];
    getAllSkills().then(res => {
        let start = window.skillShow[0];
        let stop = window.skillShow[1];
        let skillsProps = res['skills'].slice(start, stop);
        for (let i = 0; i < skillsProps.length; i++) {
            let skillId = (start + i + 1).toString();
            if (i < 9) {
                skillId = '0' + skillId;
            }

            let skillName = skillsProps[i]['skillName'];
            let skillDescription = skillsProps[i]['skillDescription'];
            let skillDate = skillsProps[i]['skillDate'];

            addSkillView(skillId, skillDate, skillName, skillDescription, skillColors[i]);
        }

        for (let i = 0; i < 4 - skillsProps.length; i++) {
            createEmptySkill();
        }

        console.log(res);
    })
}

function loadMarket() {
    clearSkills();
    setSkills();
}