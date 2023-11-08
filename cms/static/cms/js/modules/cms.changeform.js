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
            if (slug.data('changed') || title.data('changed')) {
                changed = true;
            }
        }

        if (changed) {
            var question = gettext('Are you sure you want to change tabs without saving the page first?');

            // eslint-disable-next-line no-alert
            answer = confirm(question);
        }
        if (answer) {
            window.location.href = url;
        }
    };
});
