from django import forms


class CreateEvent(forms.Form):
    name_event = forms.CharField(label='мероприятие')
    date_event = forms.DateField(label='дата проведения', widget=forms.SelectDateWidget)
    deadline = forms.DateField(label='запись до', widget=forms.SelectDateWidget)
    name = forms.CharField(label='имя отвественнго')
    surname = forms.CharField(label='фамилия отвественнго')
    email = forms.EmailField(label='электронный адрес')
    folder = forms.CharField(label='папка для хранения')

