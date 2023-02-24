from django import forms
from .models import Customers, Accounts, Reservation, Transaction, Rooms, RoomType, Payment, Crew

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'


class AccountForm(forms.ModelForm, forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type": 'password'}))
    class Meta:
        model = Accounts
        fields = ['type', 'username', 'password']
    

class ReservationForm(forms.ModelForm, forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    date_in = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    date_out = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    class Meta:
        model = Reservation
        fields = ['crew', 'customer', 'room', 'total_payment', 'date', 'date_in', 'date_out']


class TransactionForm(forms.ModelForm, forms.Form):
    trans_date = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    class Meta:
        model = Transaction
        fields = ['customer', 'crew', 'payment', 'reservation', 'trans_date']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'


class PaymentForm(forms.ModelForm, forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    class Meta:
        model = Payment
        fields = ['customer', 'method', 'amount', 'date']


class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = '__all__'


