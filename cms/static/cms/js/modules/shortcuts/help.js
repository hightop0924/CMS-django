import Modal from '../cms.modal';
import $ from 'jquery';

import keyboard from '../keyboard';
import tmpl from '../tmpl';
var template = require('./help.html');

/**
 * Binds [?] to open modal with shortcuts listing.
 *
    });

    /**
     * openModal
     *
     * @private
     * @param {Event} e
     */
    function openModal(e) {
        e.preventDefault();

        modal.open({
            title: CMS.config.lang.shortcuts,
            width: 600,
            height: 660,
            html: tmpl(template, { shortcutAreas: shortcutAreas })
        });
    }

    keyboard.setContext('cms');
    keyboard.bind('?', openModal);
    $(document).on('pointerup.cms', '.cms-show-shortcuts', openModal);
}
