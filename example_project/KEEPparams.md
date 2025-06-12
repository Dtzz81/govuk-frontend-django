# Keeping Query Parameters in Pagination
## Issue
The pagination component in the app was overwriting the query string, keeping only the page parameter and removing others (e.g., ?another_key=value). This led to loss of important filters or search context when navigating between pages.

Example:
http://localhost:8000/?page=2&q=value

After using the pagination link, the resulting URL becomes:
http://localhost:8000/?page=3

So another_key=value was lost.

## Solution
Pagination logic was updated to preserve all query parameters except page, ensuring filters/search terms remain active across pages.

**Updates to pagination.py**

New imports:

```python
from django.http import HttpRequest
from urllib.parse import urlencode
```

**Updated tag function:**

```python
@register.simple_tag
def gds_pagination(page_obj: Page, request: HttpRequest):
    current_query_params = request.GET.copy()
    if 'page' in current_query_params:
        del current_query_params['page']
    query_string = current_query_params.urlencode()
    preserved_query_string = f"&{query_string}" if query_string else ""
```

**Template link update:**
 Add the preserved query string to the pagination URLs:

```python
href="?page={{ page_obj.previous_page_number }}{{ preserved_query_string }}"
```
## Template Changes

**In userlisting.html**
Update the pagination tag to include request:

```python
{% gds_pagination page_obj request %}
```

**In templatetags**
The request parameter is passed properly on line 127:

```python
{% gds_pagination page_obj request %}
```

**Refactoring**
Removed unused imports,empty lines and redundant comments


