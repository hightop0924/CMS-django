'use strict';

// #############################################################################
// Handles JavaScript page errors

module.exports = {
    bind: function() {
        casper.on('page.error', function(msg, trace) {
            casper.echo('Error on page: ' + JSON.stringify(msg), 'ERROR');
            casper.echo('Traceback:', 'ERROR');
