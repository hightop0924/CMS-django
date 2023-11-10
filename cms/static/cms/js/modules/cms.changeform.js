/* global CMS, gettext */
import $ from 'jquery';
import addSlugHandlers from './slug';

$(function() {
    // set local variables
    var title = $('#id_title');
    var slug = $('#id_slug');

    addSlugHandlers(title, slug);

    // all permissions and page states loader
    $('div.loading').each(function() {
        $(this).load($(this).attr('rel'));
    });

    // hide rows when hidden input fields are added
    $('input[type="hidden"]').each(function() {
        $(this).parent('.form-row').hide();
    });

    // public api for changing the language tabs
    // used in admin/cms/page/change_form.html
    window.CMS.API.changeLanguage = function(url) {
        // also make sure that we will display the confirm dialog
