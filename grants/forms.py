from django import forms

from .models import Housing, Household, FamilyMember, Gender, MaritalStatus, \
    OccupationType


class HouseholdModelForm(forms.ModelForm):
    housing_type_id = forms.ModelChoiceField(queryset=Housing.objects.all(),
                                             to_field_name='housing_type',
                                             empty_label="Select Housing Type",
                                             label='Housing Type')
    household_name = forms.CharField(label='Household Name',
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder": "Enter household "
                                                            "name"
                                         }
                                     ))

    class Meta:
        model = Household
        fields = [
            'housing_type_id',
            'household_name',
        ]


class FamilyMemberModelForm(forms.ModelForm):
    household_type_id = forms.ModelChoiceField(queryset=
                                               Household.objects.all(),
                                               to_field_name='household_name',
                                               empty_label="Select Household "
                                                           "Type",
                                               label='Household Type')
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Enter family member name"
                               }
                           ))
    gender_id = forms.ModelChoiceField(queryset=Gender.objects.all(),
                                       to_field_name='gender',
                                       empty_label="Select Gender",
                                       label='Gender')
    marital_status_id = forms.ModelChoiceField(queryset=
                                               MaritalStatus.objects.all(),
                                               to_field_name='marital_status',
                                               empty_label="Select Marital "
                                                           "Status",
                                               label='Marital Status')
    spouse = forms.CharField(required=False,
                             label='Spouse',
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "Enter spouse's name "
                                                    "(if any)"
                                 }
                             ))
    occupation_type_id = forms.ModelChoiceField(queryset=
                                                OccupationType.objects.all(),
                                                to_field_name=
                                                'occupation_type',
                                                empty_label="Select Occupation"
                                                            " Type",
                                                label='Occupation Type')
    annual_income = forms.DecimalField(label='Annual Income (SGD)')
    date_of_birth = forms.DateField(widget=forms.DateInput(
                                        attrs={
                                            "placeholder": "MM/DD/YYYY"
                                        }
                                    ))

    class Meta:
        model = FamilyMember
        fields = [
            'household_type_id',
            'name',
            'gender_id',
            'marital_status_id',
            'spouse',
            'occupation_type_id',
            'annual_income',
            'date_of_birth',
        ]
