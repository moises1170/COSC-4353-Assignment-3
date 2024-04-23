from django import forms


class FuelQuoteForm(forms.Form):
    gallons = forms.IntegerField(label='Gallons Requested', min_value=1, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'placeholder': 0}),  
        error_messages={'required': "Please enter a valid number of gallons."})
    date = forms.DateField(label='Delivery Date', required=True, 
        widget=forms.DateInput(attrs={'class': 'form-control col-2 mx-auto', 'type': 'date'}), 
        error_messages={'required': "Please select a date."})
    price = forms.DecimalField(label='Suggested Price / Gallons',
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'readonly': 'readonly'}))
    total_price = forms.FloatField(label='Total Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control col-2 mx-auto', 'readonly': 'readonly'}))