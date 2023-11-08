'use strict';

// #############################################################################
// Toolbar behaviour

var helpers = require('djangocms-casper-helpers');
var globals = helpers.settings;
var cms = helpers();

casper.test.setUp(function(done) {
            test.assertVisible('.cms-toolbar');
        })
        .waitForSelector('.cms-toolbar-expanded', function() {
            test.assertEquals(
                this.getElementAttribute('.cms-toolbar-item-logo a', 'href'),
                '/',
                'The django CMS logo redirects to homepage'
            );
        })
        .run(function() {
            test.done();
        });
});
