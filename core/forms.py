
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django import forms
from django.forms import ModelForm
from .models import *
from django import forms 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        
class RemoveUser(forms.Form):
     username = forms.CharField()
              


class DateInput(forms.DateInput):
    input_type = 'date'
    
class PegawaiForm(forms.ModelForm):
    
    class Meta:
        model = Pegawai
        fields = '__all__'
        exclude =['user']
        widgets = {
            "no_hp" : forms.NumberInput (),  
        }
def __init__(self, *args, **kwargs):
     super(PegawaiForm, self).__init__(*args,**kwargs)
     self.fields['alamat'].queryset = self.alamat.objects.none()
             
          
class WalisiswaForm(forms.ModelForm):
    class Meta:
        model = WaliSiswa
        fields = '__all__'
        exclude = ['user']
        widgets = {
            "no_hp" : forms.NumberInput (),  
        }
        
        
class SiswaForm(forms.ModelForm):
     class Meta:
         model = Siswa
         fields = '__all__'
         exclude = ['user']
         widgets = {
            
            "nis" : forms.NumberInput (),   
            "nisn" : forms.NumberInput (), 
         
        }


# FORM PENJADWALAN

class KelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'
        
class RuanganForm(ModelForm):
    class Meta:
        model = Ruangan
        fields = '__all__'

class JamForm(ModelForm):
  class Meta:
    model = Jam
    fields = '__all__'
    widgets = {
      'waktu_mulai': forms.TimeInput(attrs={'type': 'time'}),
      'waktu_selesai': forms.TimeInput(attrs={'type': 'time'}),
    }

class HariForm(ModelForm):
  class Meta:
    model = Hari
    fields = '__all__'

class MapelForm(ModelForm):
  class Meta:
    model = MataPelajaran
    fields = '__all__'
    
        
class GuruForm(ModelForm):

  class Meta:
    model = Guru
    fields = '__all__'



class TugasForm(ModelForm):
  class Meta:
    model = Tugas
    fields = '__all__'
