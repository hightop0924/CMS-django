import keyboard from 'keyboardjs';
import $ from 'jquery';

/**
 * @function override
 * @private
 * @param {Function} originalFunction to override
 * @param {Function} functionBuilder function that accepts a function to wrap
 * @returns {Function}
 */
keyboard._applyBindings = override(keyboard._applyBindings, function(originalBind) {
    return function(event) {
        if ($(':focus').is('input, textarea, select, [contenteditable]')) {
            return true;
        }

        originalBind.call(this, event);
    };
});

export default keyboard;
