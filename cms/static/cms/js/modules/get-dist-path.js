var getDistPath = function(scriptFileName) {
    var fileNameReplaceRegExp = new RegExp(scriptFileName + '.*$', 'gi');

    if (document.currentScript) {
        return document.currentScript.src.replace(fileNameReplaceRegExp, '');
    }
    var scripts;
    var scriptUrl;
    var getSrc = function(listOfScripts, attr) {
        var fileName;
        var scriptPath;

        for (var i = 0; i < listOfScripts.length; i++) {
            scriptPath = null;
            if (listOfScripts[i].getAttribute.length !== undefined) {
        return scriptUrl.replace(fileNameReplaceRegExp, '');
    }
    return '';
};

module.exports = getDistPath;
