import keyboard from 'keyboardjs';
import $ from 'jquery';

/**
 * @function override
 * @private
 * @param {Function} originalFunction to override
 * @param {Function} functionBuilder function that accepts a function to wrap
 * @returns {Function}
 */
function override(originalFunction, functionBuilder) {
    var newFn = functionBuilder(originalFunction);

    newFn.prototype = originalFunction.prototype;
    return newFn;
export default keyboard;
