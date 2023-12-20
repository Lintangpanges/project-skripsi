import datetime
from django.shortcuts import render, redirect
import pandas as pd
from .models import *

from django.contrib.auth.models import Group, User

from django.http import HttpResponse
import xlwt




# Create your views here.

# PEGAWAI IMPORT
def create_Pegawai(file_path):
    df = pd.read_excel(file_path)
    print(df.values)
    list_file = [list(row) for  row in df.values]
    for l in list_file:
        username= l[1]
        password = l[2]
        user = User(username=username)
        user.set_password(password)        
        user.save()
        group = Group.objects.get(name='pegawai')
        user.groups.add(group)
        Pegawai.objects.create(
            user=user,
            no_hp = l[3],
            pendidikan_terakhir = l[4],
            tempat_lahir= l[5],
            tanggal_lahir = l[6],
            provinsi = l[7],
            kota = l[8],
            kecamatan = l[9],
            kelurahan = l[10],
            alamat = l[11],
            nbm = l[12],
            status = l[13],
            jabatan = l[14],
            gol = l[15],
            pangkat = l[16],
            tmt = l[17] 
        )
       
        
def upload_file_Pegawai(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = Excelfile.objects.create(file = file)   
        create_Pegawai(obj.file) 
        return redirect('pegawai')  
        
    return render(request,'back/pegawai/baru.html')

# PEGAWAI EXPORT
def export_filepegawai(request):
    respone = HttpResponse(content_type='application/ms-excel')
    respone['Content-Disposition'] = 'attachment; filename=Pegawai' +\
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pegawai')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['Username', 'Password','Nama', 'No HP']
    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        
    font_style = xlwt.XFStyle()
    
    rows = Pegawai.objects.all().values_list(
        'user__username', 'user__password', 'user__first_name', 'no_hp')    
    for row in rows :
        row_num+=1
        
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(respone)
    
    return respone
# PEGAWAI SISWA/WALISISWA


# KELAS IMPORT
def create_Kelas(file_path):
    df = pd.read_excel(file_path)
    print(df.values)
    list_file = [list(row) for  row in df.values]
    for l in list_file:
        Kelas.objects.create(
            tingkat = l[1],
            nama_kelas = l[2],
            nama_ruangan= l[3],
            kapasitas_ruangan = l[4],    
        )
        
def upload_file_Kelas(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = Excelfile.objects.create(file = file)    
        create_Kelas(obj.file) 
        return redirect('kelas')
        
    return render(request,'back/kelas/baru.html')

#  RUANGAN IMPORT
def create_Ruangan(file_path):
    df = pd.read_excel(file_path)
    print(df.values)
    list_file = [list(row) for  row in df.values]
    for l in list_file:
        Ruangan.objects.create(
            r_number = l[1],
            r_kapasistas = l[2],  
        )
        
def upload_file_Ruangan(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = Excelfile.objects.create(file = file)    
        create_Ruangan(obj.file) 
        return redirect('ruangan')
        
    return render(request,'penjadwalan/ruangan/baru.html')

# GURU IMPORT
def create_Guru(file_path):
    df = pd.read_excel(file_path)
    print(df.values)
    list_file = [list(row) for  row in df.values]
    for l in list_file:
        Guru.objects.create(
            gid = l[1],
            nama = l[2],  
        )
        
def upload_file_Guru(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = Excelfile.objects.create(file = file)    
        create_Guru(obj.file) 
        return redirect('guru')
        
    return render(request,'penjadwalan/guru/baru.html')

# KELAS EXPORT
def export_filekelas(request):
    respone = HttpResponse(content_type='application/ms-excel')
    respone['Content-Disposition'] = 'attachment; filename=Guru' +\
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Guru')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['id','gid', 'nama']
    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        
    font_style = xlwt.XFStyle()
    
    rows = Guru.objects.all().values_list(
         'id','gid', 'nama')    
    for row in rows :
        row_num+=1
        
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(respone)
    
    return respone
#Waktu 
def export_filepegawai(request):
    respone = HttpResponse(content_type='application/ms-excel')
    respone['Content-Disposition'] = 'attachment; filename=Pegawai' +\
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pegawai')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['Username', 'Password','Nama', 'No HP']
    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        
    font_style = xlwt.XFStyle()
    
    rows = Pegawai.objects.all().values_list(
        'user__username', 'user__password', 'user__first_name', 'no_hp')    
    for row in rows :
        row_num+=1
        
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(respone)
    
    return respone



# IMPORT BARU

def create_Kelas(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Kelas.objects.create(nama_kelas = l[1],)

def upload_file_Kelas(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_Kelas(obj.file) 
    return redirect('kelas')
      
  return render(request,'penjadwalan/kelas/baru.html')

def export_filekelas(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Kelas' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Kelas')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id','nama_kelas']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Kelas.objects.all().values_list('id','nama_kelas')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

# RUANGAN
def create_Ruangan(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Ruangan.objects.create(
      nama_ruangan = l[1],
      kelas = Kelas.objects.get(pk=l[2]),
    )
        
def upload_file_Ruangan(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_Ruangan(obj.file)
    return redirect('ruangan')
      
  return render(request,'penjadwalan/ruangan/baru.html')

def export_Ruangan(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Ruangan' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Kelas')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'nama_ruangan', 'kelas']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Ruangan.objects.all().values_list('id', 'nama_ruangan', 'kelas')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

# JAM
def create_jam(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Jam.objects.create(waktu_mulai = l[1], waktu_selesai = l[2])
        
def upload_file_jam(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_jam(obj.file)
    return redirect('jam')
      
  return render(request,'penjadwalan/jam/baru.html')

def export_jam(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Jam' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Jam')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'waktu_mulai', 'waktu_selesai']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Jam.objects.all().values_list('id', 'waktu_mulai', 'waktu_selesai')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

# HARI
def create_hari(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Hari.objects.create(nama_hari=l[1], jam=Jam.objects.get(pk=l[2]))
        
def upload_file_hari(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_hari(obj.file)
    return redirect('hari')
      
  return render(request,'penjadwalan/hari/baru.html')

def export_hari(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Hari' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Hari')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'nama_hari', 'jam']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Hari.objects.all().values_list('id', 'nama_hari', 'jam')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

# MAPEL
def create_mapel(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    MataPelajaran.objects.create(
      nama_mapel = l[1], 
      kelas = Kelas.objects.get(pk=l[2]),
      waktu = l[3],
    )
        
def upload_file_mapel(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_mapel(obj.file)
    return redirect('mapel')
      
  return render(request,'penjadwalan/mapel/baru.html')

def export_mapel(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Mapel ' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Mapel')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'nama_mapel', 'kelas', 'waktu']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = MataPelajaran.objects.all().values_list('id', 'nama_mapel', 'kelas', 'waktu')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

# GURU
def create_Guru(file_path):
  df = pd.read_excel(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Guru.objects.create(
      nama = l[1],
      alamat = l[2],  
      jenis_kelamin = l[3],  
      status = l[4],  
      
    )
        
def upload_file_Guru(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_Guru(obj.file) 
    return redirect('guru')
      
  return render(request,'penjadwalan/guru/baru.html')

# TUGAS
def create_tugas(file_path):
  df = pd.read_csv(file_path)
  list_file = [list(row) for  row in df.values]
  for l in list_file:
    Tugas.objects.create(
      guru=Guru.objects.get(pk=l[1]),
      mapel=MataPelajaran.objects.get(pk=l[2]),
    )
        
def upload_file_tugas(request):
  if request.method == 'POST':
    file = request.FILES['file']
    obj = Excelfile.objects.create(file = file)    
    create_tugas(obj.file)
    return redirect('tugas')
      
  return render(request,'penjadwalan/tugas/baru.html')

def export_tugas(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Tugas ' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Tugas')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'guru', 'mapel']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Tugas.objects.all().values_list('id', 'guru', 'mapel')    
  for row in rows :
    row_num+=1        
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone

def export_jadwal(request):
  respone = HttpResponse(content_type='application/ms-excel')
  respone['Content-Disposition'] = 'attachment; filename=Jadwal ' +\
      str(datetime.datetime.now())+'.xls'
  wb = xlwt.Workbook(encoding='utf-8')
  ws = wb.add_sheet('Tugas')
  row_num = 0
  font_style = xlwt.XFStyle()
  font_style.font.bold = True
  columns = ['id', 'guru', 'telepon', 'mapel', 'kelas', 'hari', 'waktu']
  
  for col_num in range(len(columns)):
    ws.write(row_num, col_num, columns[col_num], font_style)
      
  font_style = xlwt.XFStyle()
  
  rows = Jadwal.objects.all().values_list('id', 'tugas__guru__nama', 'tugas__guru__telepon', 'tugas__mapel__nama_mapel', 'tugas__mapel__kelas__nama_kelas', 'waktu__nama_hari', 'waktu__jam')
  for row in rows:
    row = list(row)
    waktu = Hari.objects.get(pk=row[-1])
    row[-1] = f'{waktu.jam.waktu_mulai} - {waktu.jam.waktu_selesai}'
    row_num+=1
    for col_num in range(len(row)):
      ws.write(row_num, col_num, str(row[col_num]), font_style)
  wb.save(respone)
  
  return respone


