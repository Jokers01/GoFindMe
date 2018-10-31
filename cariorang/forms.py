from django import forms
from cariorang.models import PostCari ,Detail
from PIL import Image
from django.core.files import File



class PostCariForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Full Name '}))
    umur = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Age','min':1 ,'max':200}))
    tinggi = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Height in cm','min':1 ,'max':300}))
    berat = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Your Weight in kg','min':1 ,'max':500}))
    reward = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Your Reward in Rupiah','min':0 , 'max':10000000000}))
    lokasi_hilang = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Example: +6281395231145'}))
    picture = forms.ImageField(required=True)
    class Meta:
        model = PostCari
        fields = ['name','umur','tinggi','berat','gender','reward','phone_number','lokasi_hilang','picture','ciri','desc']
class DetailForm(forms.ModelForm):

    class meta:
        model = Detail
        fields = ['message',]
