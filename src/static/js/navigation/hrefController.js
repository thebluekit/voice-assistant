function goToAnchor(anchor) {
    window.location = document.URL.replace(/#.*$/, "") + '#' + anchor
}

function getCurrentAnchor() {
    let hash = window.location.hash;
    let lastHash = hash.split('#').pop();
    return lastHash
}