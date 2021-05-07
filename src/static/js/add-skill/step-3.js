function addSkillConst() {
    let constName = document.getElementById('const-name');
    let constDescription = document.getElementById('const-description');
    window.skillObj["skillConstants"].push([constName.value, constDescription.value]);
    updateSkillConsts(window.skillObj["skillConstants"]);
    constName.value = '';
    constDescription.value = '';
}

function editSkillConst() {
    let constName = document.getElementById('const-name');
    let constDescription = document.getElementById('const-description');
    window.skillObj["skillConstants"][window.editConstIndex] = [constName.value, constDescription.value];
    constName.value = '';
    constDescription.value = '';


    let addBtn = document.getElementById('add-constant');
    let addScriptBtn = document.getElementById('add-script-btn');
    let editBtn = document.getElementById('edit-constant-btn');
    let removeBtn = document.getElementById('remove-constant-btn');
    addBtn.classList.remove('none-visability');
    addScriptBtn.classList.remove('none-visability');
    editBtn.classList.add('none-visability');
    removeBtn.classList.add('none-visability');

    updateSkillConsts(window.skillObj["skillConstants"]);

    window.editConstIndex = -1;

}

function removeSkillConst() {
    if (window.editPhraseIndex != -1) {
        window.skillObj["skillConstants"].splice(window.editConstIndex, 1);

        let constName = document.getElementById('const-name');
        let constDescription = document.getElementById('const-description');
        constName.value = '';
        constDescription.value = '';

        let addBtn = document.getElementById('add-constant');
        let addScriptBtn = document.getElementById('add-script-btn');
        let editBtn = document.getElementById('edit-constant-btn');
        let removeBtn = document.getElementById('remove-constant-btn');
        addBtn.classList.remove('none-visability');
        addScriptBtn.classList.remove('none-visability');
        editBtn.classList.add('none-visability');
        removeBtn.classList.add('none-visability');

        updateSkillConsts(window.skillObj["skillConstants"]);
    }
    window.editConstIndex = -1;
}

function updateSkillConsts(skillConstants) {
    let constantsElem = document.getElementById('constants-container');
    constantsElem.innerHTML = ''
    for (let skillConst of skillConstants) {
        constantsElem.innerHTML += `<p class="phrase" onclick="modifyConst(this)">${skillConst[0]}</p>`;
    }
}

function modifyConst(elem) {
    let addBtn = document.getElementById('add-constant');
    let addScriptBtn = document.getElementById('add-script-btn');
    let editBtn = document.getElementById('edit-constant-btn');
    let removeBtn = document.getElementById('remove-constant-btn');

    addBtn.classList.add('none-visability');
    addScriptBtn.classList.add('none-visability');
    editBtn.classList.remove('none-visability');
    removeBtn.classList.remove('none-visability');

    for (let i = 0; i < window.skillObj["skillConstants"].length; i++) {
        if (window.skillObj["skillConstants"][i][0] == elem.innerHTML) {
            window.editConstIndex = i;
            break;
        }
    }

    let constNameElem = document.getElementById('const-name');
    let constDescriptionElem = document.getElementById('const-description');

    constNameElem.value = window.skillObj["skillConstants"][window.editConstIndex][0]
    constDescriptionElem.value = window.skillObj["skillConstants"][window.editConstIndex][1]
}

function setFileSize(fileSize) {
    const fileBytes = fileSize;
    const fileKbytes = Math.floor(fileBytes / 1000);
    const fileMbytes = Math.floor(fileKbytes / 1000);

    if (fileMbytes != 0) {
        return `${fileMbytes} Mb`;
    } else if (fileKbytes != 0) {
        return `${fileKbytes} Kb`;
    } else {
        return `${fileBytes} bytes`;
    }
}


function getFileBytes() {
    const fileList = this.files;
    const firstFile = fileList[0];


    var reader = new FileReader();
    reader.onload = function() {

        var arrayBuffer = this.result,
            array = new Uint8Array(arrayBuffer),
            binaryString = String.fromCharCode.apply(null, array);
        window.skillObj["skillScript"] = binaryString;

    }
    reader.readAsArrayBuffer(this.files[0]);
}

function loadStep3() {
    window.skillObj["skillStep"] = 3;

    window.editConstIndex = -1;
    let checkExistBtn = setInterval(function() {
        let addBtn = document.getElementById('add-constant');
        if (addBtn != undefined) {
            addBtn.addEventListener('click', function() {
                addSkillConst();
            });
            clearInterval(checkExistBtn);
        }
    }, 100);

    let checkExistConstantsElem = setInterval(function() {
        let constantsElem = document.getElementById('constants-container');
        if (constantsElem != undefined) {
            constantsElem.style.maxHeight = constantsElem.offsetHeight.toString() + "px";
            clearInterval(checkExistConstantsElem);
        }
    }, 100);

    let checkExistEditBtn = setInterval(function() {
        let addBtn = document.getElementById('edit-constant-btn');
        if (addBtn != undefined) {
            addBtn.addEventListener('click', function() {
                editSkillConst();
            });
            clearInterval(checkExistEditBtn);
        }
    }, 100);

    let checkExistRemoveBtn = setInterval(function() {
        let addBtn = document.getElementById('remove-constant-btn');
        if (addBtn != undefined) {
            addBtn.addEventListener('click', function() {
                removeSkillConst();
            });
            clearInterval(checkExistRemoveBtn);
        }
    }, 100);

    let checkExistFileElem = setInterval(function() {
        const fileElement = document.getElementById("file-picker");
        if (fileElement != undefined) {

            fileElement.addEventListener("change", getFileBytes, false);

            clearInterval(checkExistFileElem);
        }
    }, 100);

    let checkExistContainer = setInterval(function() {
        let container = document.getElementById('constants-container');
        if (container != undefined) {
            updateSkillConsts(window.skillObj["skillConstants"]);
            clearInterval(checkExistContainer);
        }
    }, 100);


}