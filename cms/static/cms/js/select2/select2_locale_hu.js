/**
 * Select2 Hungarian translation
 */
(function ($) {
    "use strict";

    $.fn.select2.locales['hu'] = {
        formatNoMatches: function () { return "Nincs találat."; },
        formatInputTooShort: function (input, min) { var n = min - input.length; return "Túl rövid. Még " + n + " karakter hiányzik."; },
        formatInputTooLong: function (input, max) { var n = input.length - max; return "Túl hosszú. " + n + " karakterrel több, mint kellene."; },
