from django import forms
from dpo.models import PostDPO , DetailDPO

class PostFormDPO(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter Your Full Name '}))
    umur = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Age','min':1 ,'max':200}))
    tinggi = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Height in cm','min':1 ,'max':300}))
    berat = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Weight in kg','min':1 ,'max':500}))
    reward = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Your Reward in Rupiah','min':0 , 'max':10000000000}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Example: +6281395231145'}))
    pasal = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Pasal yang di langgar'}))
    pekerjaan = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Pekerjaan'}))
    gambar = forms.ImageField(required=True)

    class Meta:
        model = PostDPO
        fields = ['name','umur','tinggi','berat','phone_number','kelamin','pekerjaan','pasal','alamat','gambar','ciri']


class DetailFormDPO(forms.ModelForm):
    class meta:
        model = DetailDPO
        fields = ['message',]
