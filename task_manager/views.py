from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404


class IndexView(TemplateView):
    template_name = 'index.html'
