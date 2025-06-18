import os
import pathlib
from typing import Any, Dict


from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.core.paginator import Paginator


from govuk_frontend_django.components.accordion import GovUKAccordion
from govuk_frontend_django.components.back_link import GovUKBackLink
from govuk_frontend_django.components.breadcrumbs import (
   BreadcrumbsItems,
   GovUKBreadcrumbs,
)
from govuk_frontend_django.components.button import GovUKButton
from govuk_frontend_django.components.character_count import GovUKCharacterCount
from govuk_frontend_django.components.checkboxes import GovUKCheckboxes
from govuk_frontend_django.components.cookie_banner import GovUKCookieBanner
from govuk_frontend_django.components.date_input import GovUKDateInput
from govuk_frontend_django.components.error_message import GovUKErrorMessage
from govuk_frontend_django.components.pagination import GovUKPagination

User = get_user_model()


class UserListingView(ListView):
   template_name = "example/user_listing.html"
   model = User
   paginate_by = 1


   def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
       context = super().get_context_data(**kwargs)


       context.update(
           user_columns=[
               ("first_name", "First name"),
               ("last_name", "Last name"),
           ],


       )
       return context


from example_project.example.data_gen import generate_data


def bucket_list_view(request):
   sort_by = request.GET.get("sort_by")
   order = request.GET.get("order", "asc")
   count = int(request.GET.get("count", 0))


   # Only apply sorting if sort_by is specified

   try:
       if sort_by:
           bucket_list = generate_data(count=count, sort_by=sort_by, order=order)
       else:
           bucket_list = generate_data(count=count)
   except (KeyError, ValueError, TypeError):
       # If the sort field doesn't exist or something goes wrong, fallback
       bucket_list = generate_data(count=count)



   # Pagination setup :
   paginator = Paginator(bucket_list, 2) # 2 items per  page
   page_number = request.GET.get('page')


   page_obj = paginator.get_page(page_number)


   context = {
       "adventure_columns": [
           ("location", "Location"),
           ("mountain", "Mountain"),
       ],
       "object_list": page_obj.object_list,  # ONLY current page items here - INVESTIGATE
       "page_obj": page_obj,
       "sort_by": sort_by,
       "order": order,
   }
   return render(request, "example/bucket_list.html", context)


class CustomForm(forms.Form):
   # Checkboxes
   contact = forms.ChoiceField(
       label="How would you like to be contacted?",
       choices=(
           ("email", "Email"),
           ("phone", "Phone"),
           ("text", "Text"),
       ),
       widget=forms.CheckboxSelectMultiple,
   )


def components_view(request):
   context = {}
   context.update(
       form=CustomForm(),
       page_obj=UserListingView.as_view()(request).context_data["page_obj"],
       breadcrumb_items=[
           BreadcrumbsItems(
               text="Item 1",
               href="#",
           ),
           BreadcrumbsItems(
               text="Item 2",
               href="#",
           ),
           BreadcrumbsItems(
               text="Item 3",
               href="#",
           ),
       ],
       table_columns=[
           ("column_1", "Column 1"),
           ("column_2", "Column 2"),
           ("column_3", "Column 3"),
       ],
       table_rows=[
           {
               "column_1": "Row 1 Column 1",
               "column_2": "Row 1 Column 2",
               "column_3": "Row 1 Column 3",
           },
           {
               "column_1": "Row 2 Column 1",
               "column_2": "Row 2 Column 2",
               "column_3": "Row 2 Column 3",
           },
           {
               "column_1": "Row 3 Column 1",
               "column_2": "Row 3 Column 2",
               "column_3": "Row 3 Column 3",
           },
       ],
       model_table_columns=[
           ("first_name", "First Name"),
           ("last_name", "Last Name"),
           ("email", "Email"),
       ],
       model_table_rows=User.objects.all(),
       users=User.objects.all(),
       nav_links=[
           (
               "Link 1",
               reverse("templatetags"),
           ),
           (
               "Link 2",
               reverse("templatetags"),
           ),
           (
               "Link 3",
               reverse("templatetags"),
           ),
           (
               "Link 4",
               reverse("templatetags"),
           ),
       ],
       service_nav_links=[
           {
               "text": "Link 1",
               "href": reverse("templatetags"),
           },
           {
               "text": "Link 2",
               "href": reverse("templatetags"),
               "active": True,
           },
           {
               "text": "Link 3",
               "href": reverse("templatetags"),
           },
           {
               "text": "Link 4",
               "href": reverse("templatetags"),
           },
       ],
   )


   return render(request, "example/templatetags.html", context)


