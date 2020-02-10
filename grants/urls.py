from django.urls import path

from .views import HouseholdCreateView, HouseholdDetailView, \
    FamilyMemberCreateView, HouseholdListView, HouseholdDeleteView, search


app_name = 'grants'
urlpatterns = [
    path('household/create/', HouseholdCreateView.as_view(),
         name='household-create'),
    path('household/<int:id>/', HouseholdDetailView.as_view(),
         name='household-detail'),
    path('household/add/', FamilyMemberCreateView.as_view(),
         name='household-add'),
    path('household/', HouseholdListView.as_view(), name='household-list'),
    path('household/<int:id>/delete/', HouseholdDeleteView.as_view(),
         name='household-delete'),
    path('household/search/', search, name='search'),
]
