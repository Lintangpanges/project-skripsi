from django.shortcuts import render,get_object_or_404
from multiprocessing import context
from django.shortcuts import render, redirect

# from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import  CreateUserForm

from .forms import *


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def index(request):
    # form_Siswa = Siswa.objects.all()
    # form_Pegawai = Pegawai.objects.all()
    # form_Walisiswa = WaliSiswa.objects.all()
    guru = Guru.objects.all()
    kelas = Kelas.objects.all()
    mapel = MataPelajaran.objects.all()
    hari = Hari.objects.all()
    
    total_guru = guru.count()
    total_kelas = kelas.count()
    total_mapel = mapel.count()
    total_hari = hari.count()
    # total_Siswa = form_Siswa.count()
    # total_Pegawai = form_Pegawai.count()
    # total_Walisiswa = form_Walisiswa.count()

    context = {'total_guru':total_guru, 'total_kelas': total_kelas, 'total_mapel':total_mapel, 'total_hari':total_hari}
    return render(request, 'index.html', context)

def error_404(request,excepiton):
    return render(request, '404.htm')

def register(request):
    context = {}
    return render(request, 'registration/tampilan_regis.html', context)

@unauthenticated_user
def registerPage_Pegawai(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='pegawai')
            user.groups.add(group)
            Pegawai.objects.create(
                user=user,
            )
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@unauthenticated_user
def registerPage_Walisiswa(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='walisiswa')
            group2 = Group.objects.get(name='siswa')
            user.groups.add(group)
            user.groups.add(group2)
            
            WaliSiswa.objects.create(
                user=user,
            )
            Siswa.objects.create(
                user=user,
            )
            
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/singnup_walisiswa.html', context)

# fungsi crud pegawai //////////////////////////////////////////////////////////////////////////////////////////////////////////
@login_required(login_url='login')
def form_Pegawai(request):
    form_Pegawai = Pegawai.objects.all()
    
    context = {'form_Pegawai':form_Pegawai}
    return render(request,'back/pegawai/pegawai_form.html', context )

@login_required(login_url='login')
def create_Pegawai(request):
    form2 = CreateUserForm()
    form = PegawaiForm()
    if request.method == 'POST' :
        form2 = CreateUserForm(request.POST)
        form = PegawaiForm(request.POST, request.FILES)
        if form2.is_valid() and form.is_valid() :
            user = form2.save()
            f1=form.save(commit=False)
            f1.user=user
            f1.save()
            group = Group.objects.get_or_create(name='pegawai')
            group[0].user_set.add(user)
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('pegawai')
    context = {'form':form, 'form2':form2}
    return render(request,'back/pegawai/pegawai_create.html', context)

@login_required(login_url='login')
def update_Pegawai(request, pk):
    p = Pegawai.objects.get(id=pk)
    u = User.objects.get(id=p.user_id)
    
    form2 = UserForm(instance=u)
    form = PegawaiForm(instance=p)
    
    if request.method == 'POST' :
        form2 = CreateUserForm(request.POST, instance=u)     
        # buattt halaman baru untuk tidak mengubah sandi
        form = PegawaiForm(request.POST, request.FILES, instance=p)
        if form2.is_valid() and form.is_valid():
            user=form2.save()
            user.save()
            f1=form.save(commit=False)
            f1.save()            
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('pegawai')
    context = {'form_Pegawai':form_Pegawai, 'form':form,'form2':form2}
    return render(request,'back/pegawai/pegawai_create.html', context)

@login_required(login_url='login')
def delete_Pegawai(request, pk):
        p = get_object_or_404(Pegawai, id=pk)
    
        p.delete()
        p.user.delete()
        messages.success(request, "Data Berhasil Dihapus")
        return redirect('pegawai')
      #  context = {'item':p }
       # return render(request,'back/pegawai/pegawai_delete.html',context)

#\\\ user pegawai ///##########################################################################
@login_required(login_url='login')
def userPage_Pegawai(request):
    form_Pegawai = Pegawai.objects.all()
    # form_Pegawai= request.user.pegawai.p_set.all()
    
    print('tes:',form_Pegawai)    
    context = {'form_Pegawai':form_Pegawai}
    return render(request,'back/pegawai/pegawai_user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['pegawai'])
def userView_Pegawai(request):
    user = request.user
    pegawai = request.user.pegawai
    
    form = UserForm(instance=user)
    form2 = PegawaiForm(instance=pegawai) 
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=user)
        form2 = PegawaiForm(request.POST, request.FILES,instance=pegawai)
 
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('userpage_pegawai')

    context = {'form':form, 'form2':form2}
    return render(request,'back/pegawai/pegawai_view.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['pegawai'])
def view_Pegawai(request):
    context = {
            'pegawai' : request.user.pegawai, 'user': request.user,
        }
    return render(request, 'back/pegawai/pegawai_overview.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['pegawai'])
def userCreate_Pegawai(request):
    user = request.user
    pegawai = request.user.pegawai
    
    form = UserForm(instance=user)
    form2 = PegawaiForm(instance=pegawai) 
     # form3 = AlamatForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=user)
        form2 = PegawaiForm(request.POST, request.FILES,instance=pegawai)
        # form3 = AlamatForm(request.POST)
        
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            # form3.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('userpage_pegawai')

    context = {'form':form, 'form2':form2}
    return render(request,'back/pegawai/pegawai_create_user.html',context)

# fungsi crud walisiswa //////////////////////////////////////////////////////////////////////////////////////////////////////////
def form_Walisiswa(request):
    form_Walisiswa = WaliSiswa.objects.all()
    form_user = User.objects.all()
    
    context = {'form_Walisiswa':form_Walisiswa,'form_user':form_user}
    return render(request,'back/walisiswa/walisiswa_form.html', context )

@login_required(login_url='login')
def create_Walisiswa(request):
    form2 = CreateUserForm()
    form = WalisiswaForm()
    if request.method == 'POST' :
        form2 = CreateUserForm(request.POST)
        form = WalisiswaForm(request.POST, request.FILES)
        if form2.is_valid() and form.is_valid():
            user = form2.save()
            
            f1 = form.save(commit=False)
            f1.user=user
            f1.save()
            group = Group.objects.get_or_create(name='walisiswa')
            group1 = Group.objects.get(name='siswa')
            group[0].user_set.add(user)
            user.groups.add(group1)
            
            Siswa.objects.create(
                user=user,
            )
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('walisiswa')
    context = {'form':form,'form2':form2}
    return render(request,'back/walisiswa/walisiswa_create.html', context)

@login_required(login_url='login')
def update_Walisiswa(request, pk):
    w = WaliSiswa.objects.get(id=pk)
    u = User.objects.get(id=w.user_id)
    
    form2 = CreateUserForm(instance=u)
    form = WalisiswaForm(instance=w)
    if request.method == 'POST' :
        form2 = CreateUserForm(request.POST, instance=u)
        form = WalisiswaForm(request.POST, request.FILES, instance=w)
        if  form2.is_valid and form.is_valid():
            user = form2.save()
            user.save()
            f1 = form.save(commit=False)
            f1.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('walisiswa')
    context = {'form_Walisiswa':form_Walisiswa, 'form':form,'form2':form2}
    return render(request,'back/walisiswa/walisiswa_create.html', context)

@login_required(login_url='login')
def delete_Walisiswa(request, pk):
    w =get_object_or_404(WaliSiswa,id=pk)
  
    w.delete()
    w.user.delete()
    messages.success(request, "Data Berhasil Dihapus")

    return redirect('walisiswa')
    #context = {'item':w}
   # return render(request,'back/walisiswa/walisiswa_delete.html',context)

#\\\ user walisisa ///###########################################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def userPage_Walisiswa(request):
    form_Walisiswa = WaliSiswa.objects.all()
    
    context = {'form_Walisiswa':form_Walisiswa}
    return render(request,'back/walisiswa/walisiswa_user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def view_Walisiswa(request):
    context = {
            'walisiswa' : request.user.walisiswa, 'user': request.user,
        }
    return render(request, 'back/walisiswa/walisiswa_overview.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def userCreate_Walisiswa(request):
    user = request.user
    walisiswa = request.user.walisiswa
    
    form = UserForm(instance=user)
    form2 = WalisiswaForm(instance=walisiswa)  
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=user)
        form2 = WalisiswaForm(request.POST, request.FILES,instance=walisiswa)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('userpage_walisiswa')

    context = {'form':form, 'form2':form2}
    return render(request,'back/walisiswa/walisiswa_create_user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def userView_Walisiswa(request):
    user = request.user
    walisiswa = request.user.walisiswa
    
    form = UserForm(instance=user)
    form2 = WalisiswaForm(instance=walisiswa) 
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=user)
        form2 = WalisiswaForm(request.POST, request.FILES,instance=walisiswa)
 
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('userpage_walisiswa')

    context = {'form':form, 'form2':form2}
    return render(request,'back/walisiswa/walisiswa_view.html',context)

# kelas baru////////////////////////////////////


# Fungsi crud Siswa //////////////////////////////////////////////////////////////////////////////////////////////////////////
@login_required(login_url='login')
def form_Siswa(request):
    form_Siswa = Siswa.objects.all()
    
    context = {'form_Siswa':form_Siswa}
    return render(request,'back/Siswa/Siswa_form.html', context )

@login_required(login_url='login')
def update_Siswa(request, pk):
    s = Siswa.objects.get(id=pk)
    form = SiswaForm(instance=s)
    if request.method == 'POST' :
        form = SiswaForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('Siswa')
    context = {'form_Siswa':form_Siswa, 'form':form}
    return render(request,'back/Siswa/Siswa_create.html', context)

@login_required(login_url='login')
def delete_Siswa(request, pk):
    s =get_object_or_404( Siswa,id=pk)
    s.delete()
    s.user.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('Siswa')

#\\\ user siswa///###########################################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def userCreate_Siswa(request):
    siswa = request.user.siswa
    
    form2 = SiswaForm(instance=siswa)  
    if request.method == 'POST':
        form2 = SiswaForm(request.POST, request.FILES,instance=siswa)
        if form2.is_valid():
            form2.save()
            return redirect('userpage_walisiswa')

    context = {'form2':form2}
    return render(request,'back/Siswa/siswa_create_user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['walisiswa'])
def userView_Siswa(request):
    siswa = request.user.siswa
    
    form2 = SiswaForm(instance=siswa)  
    if request.method == 'POST':
        form2 = SiswaForm(request.POST, request.FILES,instance=siswa)
        if form2.is_valid():
            form2.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('userpage_walisiswa')

    context = {'form2':form2}
    return render(request,'back/Siswa/Siswa_view.html',context)
    
    
#penjadwalan template //////////////////////////////////////////////////////////////////////////////////////////////////////////////////




