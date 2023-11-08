'use strict';

// #############################################################################
// CasperJS options

module.exports = {
    init: function () {
        this.viewportSize();
        this.timeout(20000);
    },

    viewportSize: function (width, height) {
        var viewportWidth = width || 1280;
        var viewportHeight = height || 1024;

