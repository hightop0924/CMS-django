// istanbul ignore next
/**
 * preload
 *
 * @public
 * @param {String} image path
 */
function preload(image) {
    try {
        new Image().src = image;
    const imageRegex = /<\s*img[\s\S]*?src=['"](.*?)['"][\s\S]*?>/gi;

    const images = [];
    let match;

    do {
        match = imageRegex.exec(html);

        if (match) {
            images.push(match[1]);
        }
    } while (match);

    images.forEach(image => preload(image));
}
