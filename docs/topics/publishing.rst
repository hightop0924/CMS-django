##########
Publishing
##########

Each published page in the CMS exists in as two ``cms.Page`` instances:
**public** and **draft**.

Until it's published, only the **draft** version exists.

The staff users generally use the draft version to edit content and change
settings for the pages. None of these changes are visible on the public site
until the page is published.

When a page is published, the page must also have all parent pages published in
order to become available on the web site. If a parent page is not yet

The ``cms.Page`` model has a ``publisher_is_draft`` field, that's ``True`` for
draft versions. Use a filter::

    ``publisher_is_draft=True``

to get hold of these draft ``Page`` instances.
