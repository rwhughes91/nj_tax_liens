from django import forms

from . import models


class LienForm(forms.ModelForm):
    block = forms.CharField(widget=forms.TextInput, label='', required=False)
    lot = forms.CharField(widget=forms.TextInput, label='', required=False)
    qualifier = forms.CharField(widget=forms.TextInput, label='', required=False)
    certificate_number = forms.CharField(widget=forms.TextInput, label='', required=False)
    sale_date = forms.DateField(widget=forms.TextInput, label='', required=False)
    address = forms.CharField(widget=forms.TextInput, label='', required=False)
    lien_id = forms.IntegerField(widget=forms.TextInput, label='', required=False)

    def __init__(self, *args, **kwargs):
        super(LienForm, self).__init__(*args, **kwargs)
        self.fields['block'].widget.attrs['placeholder'] = 'Block'
        self.fields['lot'].widget.attrs['placeholder'] = 'Lot'
        self.fields['qualifier'].widget.attrs['placeholder'] = 'Qualifier'
        self.fields['certificate_number'].widget.attrs['placeholder'] = 'Certificate Number'
        self.fields['sale_date'].widget.attrs['placeholder'] = 'Sale Year'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['lien_id'].widget.attrs['placeholder'] = 'Lien ID'
        self.fields['county'].widget.choices = [("", "Township"),] + list(self.fields['county'].choices)[1:]
        self.fields['county'].label = ''
        self.fields['block'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['lot'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['qualifier'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['certificate_number'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['sale_date'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['county'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['lien_id'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-md'
        self.fields['county'].required = False

        self.fields['block'].widget.attrs['autocomplete'] = "off"
        self.fields['lot'].widget.attrs['autocomplete'] = "off"
        self.fields['qualifier'].widget.attrs['autocomplete'] = "off"
        self.fields['certificate_number'].widget.attrs['autocomplete'] = "off"
        self.fields['sale_date'].widget.attrs['autocomplete'] = "off"
        self.fields['address'].widget.attrs['autocomplete'] = "off"
        self.fields['lien_id'].widget.attrs['autocomplete'] = "off"

    class Meta:
        model = models.Lien
        fields = (
            'block',
            'lot',
            'qualifier',
            'certificate_number',
            'sale_date',
            'county',
            'lien_id',
            'address',
        )


class LienUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LienUpdateForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs['class'] = 'form-control'
        self.fields['redemption_date'].widget.attrs['class'] = 'form-control'
        self.fields['redemption_amount'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['notes'].widget.attrs['rows'] = "3"
        self.fields['status'].widget.choices = [("", "Status"),] + list(self.fields['status'].choices)[1:]
        self.fields['redemption_date'].widget.attrs['placeholder'] = 'Redemption Date'

    class Meta:
        model = models.Lien
        fields = (
            'redemption_date',
            'redemption_amount',
            'status',
            'notes',
        )


class SubForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubForm, self).__init__(*args, **kwargs)
        self.fields['sub_date'].widget.attrs['placeholder'] = 'Date of Interest'
        self.fields['sub_type'].widget.attrs['placeholder'] = 'Type'
        self.fields['total'].widget.attrs['placeholder'] = 'Amount'
        self.fields['sub_date'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['sub_type'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['total'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['sub_date'].widget.attrs['autocomplete'] = "off"
        self.fields['sub_type'].widget.attrs['autocomplete'] = "off"
        self.fields['total'].widget.attrs['autocomplete'] = "off"
        self.fields['sub_type'].widget.choices = [("", "Type"),] + list(self.fields['sub_type'].choices)[1:]

    class Meta:
        model = models.Sub
        fields = (
            'sub_type',
            'sub_date',
            'total',
        )
