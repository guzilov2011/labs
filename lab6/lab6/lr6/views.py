from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.

from lr6.models import BookModel


class BookListView(ListView):

    model = BookModel

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

