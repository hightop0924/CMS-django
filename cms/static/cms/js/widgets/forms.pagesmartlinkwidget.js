/*
 * Copyright https://github.com/divio/django-cms
 */

// this essentially makes sure that dynamically required bundles are loaded
// from the same place
// eslint-disable-next-line
__webpack_public_path__ = require('../modules/get-dist-path')('bundle.forms.pagesmartlinkwidget');

// #############################################################################
// PAGE SMART LINK WIDGET
// cms/forms/widgets.py used for redirects in admin/cms/page/advanced-settings
require.ensure([], function (require) {
    var $ = require('jquery');
    var Class = require('classjs');

    require('../select2/select2');

    /**
     * Creates a select field using jquery.select2 to filter through
     * available pages or set a custom url.
     *
     * @class PageSmartLinkWidget
     * @namespace CMS
     */
                        return {
                            q: term,
                            language_code: options.lang
                        };
                    },
                    // default search output, will be overridden if no results map
                    results: function (data) {
                        return {
                            more: false,
                            results: $.map(data, function (item) {
                                return {
                                    id: item.redirect_url,
                                    text: item.title + ' (/' + item.path + ')'
                                };
                            })
                        };
                    }
                },
                // create fallback entry if no choices are found
                createSearchChoice: function (term, data) {
                    if ($(data).filter(
                        function () {
                            return this.text.localeCompare(term) === 0;
                        }).length === 0
                    ) {
                        return {
                            id: term,
                            text: term
                        };
                    }
                },
                // ensures initial selection is loaded
                initSelection: function (element, callback) {
                    callback({
                        id: element.val(),
                        text: element.val()
                    });
                }
            });
        }
    });

    window.CMS = window.CMS || {};
    window.CMS.PageSmartLinkWidget = PageSmartLinkWidget;

    $(function () {
        window.CMS.Widgets._pageSmartLinkWidgets.forEach(function (widget) {
            new PageSmartLinkWidget(widget);
        });
    });
}, 'admin.widget');
