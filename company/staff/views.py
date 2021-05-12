from django.shortcuts import render
from .models import Department
from django.views import generic



class Dept_list(generic.ListView):
    model = Department


class Dept_detailviews(generic.DetailView):
    model = Department