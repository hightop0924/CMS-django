var cache = {};

/**
 * tmpl
 *
 * @public
 * @param {String} str template
 * @param {Object} data for the template
 * @returns {String|Function}
 */
export default function tmpl(str, data) {
    // Figure out if we're getting a template, or if we need to
    // load the template - and be sure to cache the result.
    // eslint-disable-next-line no-negated-condition
    var fn = !/\W/.test(str)
        ? (cache[str] = cache[str] || tmpl(document.getElementById(str).innerHTML))
        : // Generate a reusable function that will serve as a template
          // generator (and which will be cached).
          // eslint-disable-next-line
          new Function(
              'obj',
              'var p=[],print=function (){p.push.apply(p,arguments);};' +
                  // Introduce the data as local variables using with(){}
                  "with(obj){p.push('" +
                  // Convert the template into pure JavaScript
