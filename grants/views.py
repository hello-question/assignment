from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView, ListView, DeleteView)

from .models import Household, FamilyMember
from .forms import HouseholdModelForm, FamilyMemberModelForm


class HouseholdCreateView(CreateView):
    """
    Create households
    """
    template_name = 'grants/household_create.html'
    form_class = HouseholdModelForm
    queryset = Household.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class FamilyMemberCreateView(CreateView):
    """
    Add a family member into the household
    """
    template_name = 'grants/household_add.html'
    form_class = FamilyMemberModelForm
    queryset = FamilyMember.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class HouseholdDetailView(ListView):
    """
    Show the family member(s) in a household
    """
    template_name = 'grants/household_detail.html'

    def get_queryset(self):
        id_ = self.kwargs.get("id") # parse through the URL
        queryset = FamilyMember.objects.filter(household_type_id=id_)
        return queryset


class HouseholdListView(ListView):
    """
    Show the list of households
    """
    template_name = 'grants/household_list.html'
    queryset = Household.objects.all()


class HouseholdDeleteView(DeleteView):
    """
    Delete the household & family members
    """
    template_name = 'grants/household_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id") # parse through the URL
        return get_object_or_404(Household, id=id_)

    def get_success_url(self):
        return reverse('grants:household-list')


def search(request):
    """
    Search (not completed)
    """
    if request.method == 'GET':
        query = request.GET.get('q')

        submit_btn = request.GET.get('submit')

        if query is not None:
            # lookups = FamilyMember(household_type_id__icontains=query)

            results = FamilyMember.objects.filter(query)

            context = {'results': results,
                       'submit_btn': submit_btn}

            return render(request, 'grants/household_search.html', context)

        else:
            return render(request, 'grants/household_search.html')

    else:
        return render(request, 'grants/household_search.html')
