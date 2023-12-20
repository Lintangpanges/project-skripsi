from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from .models import *
from core.algoritma import AG
from django.views.generic import View
from django.conf import settings
# from .render import Render

# # FORMMM

#  KELAS
@login_required(login_url='login')
def form_Kelas(request):
    form_Kelas = Kelas.objects.all()
    
    context = {'form_Kelas':form_Kelas}
    return render(request,'penjadwalan/kelas/kelas_form.html', context )

@login_required(login_url='login')
def create_Kelas(request):
    form = KelasForm()
    if request.method == 'POST' :
        form = KelasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('kelas')
    context = {'form':form}
    return render(request,'penjadwalan/kelas/kelas_create.html', context)

@login_required(login_url='login')
def update_Kelas(request, pk):
    k = Kelas.objects.get(id=pk)
    form = KelasForm(instance=k)
    if request.method == 'POST' :
        form = KelasForm(request.POST, instance=k)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('kelas')
    context = {'form_Kelas':form_Kelas, 'form':form}
    return render(request,'penjadwalan/kelas/kelas_create.html', context)

@login_required(login_url='login')
def delete_Kelas(request, pk):
    k = get_object_or_404(Kelas, id=pk)
    k.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('kelas')

# # RUANGAN
@login_required(login_url='login')
def form_Ruangan(request):
    context = {'ruang_form': Ruangan.objects.all()}
    return render(request, 'penjadwalan/ruangan/ruangan_form.html',context)

@login_required(login_url='login')
def create_Ruangan(request):
    form = RuanganForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('ruangan')
        else:
            print('Invalid')
    context = {'form':form}
    return render(request, 'penjadwalan/ruangan/ruangan_create.html',context)

@login_required(login_url='login')
def update_Ruangan(request, pk):
    rg = Ruangan.objects.get(id=pk)
    form = RuanganForm(instance=rg)
    if request.method == 'POST':
        form = RuanganForm(request.POST, instance=rg)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('ruangan')
        else:
            print('Invalid')
    context = {'form':form}
    return render(request, 'penjadwalan/ruangan/ruangan_create.html', context)

@login_required(login_url='login')
def delete_Ruangan(request, pk):
    rg = Ruangan.objects.get(pk=pk)
    if request.method == 'POST':
        rg.delete()
        messages.success(request, "Data Berhasil Dihapus")
        return redirect('ruangan')
    context = {'item':rg}
    return render(request, 'penjadwalan/ruangan/ruangan_delete.html', context)

# JAM
@login_required(login_url='login')
def form_jam(request):
  context = {'jam': Jam.objects.all()}
  return render(request, 'penjadwalan/jam/form.html', context)

@login_required(login_url='login')
def create_jam(request):
    form = JamForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('jam')
        else:
            print('Invalid')
    context = {'form':form}
    return render(request, 'penjadwalan/jam/create.html',context)

@login_required(login_url='login')
def update_jam(request, pk):
  jam = Jam.objects.get(id=pk)
  form = JamForm(instance=jam)
  if request.method == 'POST':
    form = JamForm(request.POST, instance=jam)
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Diperbaharui")
      return redirect('jam')
    else:
      print('Invalid')
  context = {'form':form}
  return render(request, 'penjadwalan/jam/create.html', context)

@login_required(login_url='login')
def delete_jam(request, pk):
  rg = Jam.objects.get(pk=pk)
  if request.method == 'POST':
    rg.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('jam')

# HARI
@login_required(login_url='login')
def form_hari(request):
  context = {'hari': Hari.objects.all()}
  return render(request, 'penjadwalan/hari/form.html', context)

@login_required(login_url='login')
def create_hari(request):
  form = HariForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Ditambahkan")
      return redirect('hari')
    else:
      print('Invalid')
  context = {'form':form}
  return render(request, 'penjadwalan/hari/create.html',context)

@login_required(login_url='login')
def update_hari(request, pk):
  hari = Hari.objects.get(id=pk)
  form = HariForm(instance=hari)
  if request.method == 'POST':
    form = HariForm(request.POST, instance=hari)
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Diperbaharui")
      return redirect('hari')
    else:
      print('Invalid')
  context = {'form':form}
  return render(request, 'penjadwalan/hari/create.html', context)

@login_required(login_url='login')
def delete_hari(request, pk):
  rg = Hari.objects.get(pk=pk)
  if request.method == 'POST':
    rg.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('hari')

# MATAPELAJARAN
@login_required(login_url='login')
def form_Mapel(request):
    context = {'mapel_form' : MataPelajaran.objects.all()}
    return render(request, 'penjadwalan/mapel/mapel_form.html', context)

@login_required(login_url='login')
def create_Mapel(request):
    form = MapelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('mapel')
        else:
            print('Invalid')
    context = {'form':form}
    return render(request, 'penjadwalan/mapel/mapel_create.html', context)

@login_required(login_url='login')
def update_Mapel(request, pk):
    mapel = MataPelajaran.objects.get(id=pk)
    form = MapelForm(instance=mapel)
    if request.method =='POST':
        form =MapelForm(request.POST, instance=mapel)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('mapel')
        else:
            print('Invalid')
    context ={'form':form}
    return render(request, 'penjadwalan/mapel/mapel_create.html', context)

@login_required(login_url='login')
def delete_Mapel(request, pk):
    mp = MataPelajaran.objects.get(pk=pk)
    if request.method == 'POST':
        mp.delete()
        messages.success(request, "Data Berhasil Dihapus")
        return redirect('mapel')
    
# GURU
@login_required(login_url='login')
def form_Guru(request):
    context = {'guru_form': Guru.objects.all()}
    return render(request, 'penjadwalan/guru/guru_form.html', context)

@login_required(login_url='login')
def create_Guru(request):
    form = GuruForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('guru')
        else:
            print('Invalid')
    context = {'form':form}
    return render(request, 'penjadwalan/guru/guru_create.html', context)

@login_required(login_url='login')
def update_Guru(request, pk):
    gr = Guru.objects.get(id=pk)
    form = GuruForm(instance=gr)
    if request.method =='POST':
        form =GuruForm(request.POST, instance=gr)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('guru')
        else:
            print('Invalid')
    context ={'form':form}
    return render(request, 'penjadwalan/guru/guru_create.html', context)

@login_required(login_url='login')
def delete_Guru(request, pk):
    gr = Guru.objects.get(pk=pk)
    if request.method == 'POST':
        gr.delete()
        messages.success(request, "Data Berhasil Dihapus")
        return redirect('guru')
    context = {'item':gr}
    return render(request, 'penjadwalan/guru/guru_delete.html', context)

# TUGAS
@login_required(login_url='login')
def form_tugas(request):
  context = {'tugas': Tugas.objects.all()}
  return render(request, 'penjadwalan/tugas/form.html', context)

@login_required(login_url='login')
def create_tugas(request):
  form = TugasForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Ditambahkan")
      return redirect('create_tugas')
    else:
      print('Invalid')
  context = {'form':form}
  return render(request, 'penjadwalan/tugas/create.html',context)

@login_required(login_url='login')
def update_tugas(request, pk):
  tugas = Tugas.objects.get(id=pk)
  form = TugasForm(instance=tugas)
  if request.method == 'POST':
    form = TugasForm(request.POST, instance=tugas)
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Diperbaharui")
      return redirect('tugas')
    else:
      print('Invalid')
  context = {'form':form}
  return render(request, 'penjadwalan/tugas/create.html', context)

@login_required(login_url='login')
def delete_tugas(request, pk):
  rg = Tugas.objects.get(pk=pk)
  if request.method == 'POST':
    rg.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('tugas')

@login_required
def generate(request):
  context = {}
  context['total_tugas'] =  Tugas.objects.all().count()
  context['total_waktu'] = Hari.objects.all().count()

  if request.method == 'POST':
    num_kromosom = int(request.POST['num_kromosom'])
    max_generation = int(request.POST['max_generation'])
    crossover_rate = int(request.POST['crossover_rate'])
    mutation_rate = int(request.POST['mutation_rate'])
    
    if num_kromosom < 10 or num_kromosom > 500:
      messages.success(request, "Masukkan jumlah kromosom dari 10 sampai 500")
      return render(request, 'penjadwalan/penjadwalan/form.html', context)
    
    if max_generation < 10 or max_generation > 500:
      messages.success(request, "Masukkan maksimal generasi dari 25 sampai 500")
      return render(request, 'penjadwalan/penjadwalan/form.html', context)
    
    if crossover_rate < 1 or crossover_rate > 100 or mutation_rate < 1 or mutation_rate > 100:
      messages.success(request, "Masukkan dari 1 sampai 100")
      return render(request, 'penjadwalan/penjadwalan/form.html', context)

    tugas_queryset = Tugas.objects.all()
    tugas_dict = {}
    for tugas in tugas_queryset:
      tugas_dict[tugas.id-1] = {
        'id_tugas': tugas.id,
        'id_guru': tugas.guru.id,
        'id_mapel': tugas.mapel.id,
        'nama_mapel': tugas.mapel.nama_mapel,
        'waktu': tugas.mapel.waktu,
        'id_kelas': tugas.mapel.kelas.id
      }

    hari_queryset = Hari.objects.all()
    hari_dict = {}
    for hari in hari_queryset:
      hari_dict[hari.id-1] = {
        'id_hari': hari.id,
        'nama_hari': hari.nama_hari,
        'id_jam': hari.jam.id,
        'waktu_mulai': hari.jam.waktu_mulai,
        'waktu_selesai': hari.jam.waktu_selesai,
      }

    ag = AG(hari_dict, tugas_dict)
    ag.num_crommosom = num_kromosom
    ag.max_generation = max_generation
    ag.debug = True if request.POST.get('debug') else False
    ag.crossover_rate = crossover_rate
    ag.mutation_rate = mutation_rate
    data = ag.generate()
    context.update(data)

  return render(request, 'penjadwalan/penjadwalan/form.html', context)

@login_required
def jadwal_views(request):
  context = {'jadwal': Jadwal.objects.order_by('tugas__guru__nama', 'waktu__nama_hari').all()}
  return render(request, 'penjadwalan/jadwal/index.html', context)

def error_404(request, exception):
  return render(request, '404.htm')


