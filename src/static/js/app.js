'use strict';

(function() {
    function init() {
        var router = new Router([
            new Route('market', 'market.html', true),
            new Route('add-skill-step-1', 'add-skill-step-1.html'),
            new Route('add-skill-step-2', 'add-skill-step-2.html'),
            new Route('add-skill-step-3', 'add-skill-step-3.html'),
            new Route('skill-was-uploaded', 'skill-was-uploaded.html')
        ]);
    }
    init();
}());