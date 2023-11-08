/**
 * Select2 Portuguese (Portugal) translation
 */
(function ($) {
    "use strict";

    $.fn.select2.locales['pt-PT'] = {
        formatNoMatches: function () { return "Nenhum resultado encontrado"; },
        formatInputTooShort: function (input, min) { var n = min - input.length; return "Introduza " + n + " car" + (n == 1 ? "ácter" : "acteres"); },
        formatInputTooLong: function (input, max) { var n = input.length - max; return "Apague " + n + " car" + (n == 1 ? "ácter" : "acteres"); },
