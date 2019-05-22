# RA Website
Check and make notes on blobs of text.


Uses django, and an import function to allow for checking and making notes on blobs of text.
Used for RAs checking information rights in debt covenants initially.

For more information on Django, see [the tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

<!--
## Updating projects

Run the following SQL query to change project IDs:

```SQL
update html_checker_textblob SET project_id=2 WHERE id IN (SELECT id FROM html_checker_textblob WHERE project_id=1 LIMIT 2000);
```
-->

## TODO:
* [X] Add admin interface
* [X] Add import functionality
* [ ] Update admin interface to allow minimal or centralized customizing
