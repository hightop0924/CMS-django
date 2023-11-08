'use strict';

// #############################################################################
// CasperJS options

module.exports = {
    init: function () {
        this.viewportSize();
        this.timeout(20000);
    },
    },

    timeout: function (timeout) {
        casper.options.waitTimeout = timeout || 10000;
    }
};
