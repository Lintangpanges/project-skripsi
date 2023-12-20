from django.contrib.auth.models import User
from django.db import models
import random as rnd

STATUS_PEGAWAI = (
    (1, 'aktif'),
    (2, 'cuti'),
    (3, 'studi lanjut'),
    (4, 'resign'),
    (5, 'pensiun'),
    (6, 'meninggal'),
    (7, 'dikeluarkan')
)

JENJANG_PENDIDIKAN = (
    (0, 'Tidak Menempuh Pendidikan'),
    (1, 'SD'),
    (2, 'SMP'),
    (3, 'SMA, D1, D2'),
    (4, 'D3'),
    (5, 'S1/D4'),
    (6, 'S2'),
    (7, 'S3')
)

JENIS_KELAMIN = (
    ('L', 'Laki-Laki'),
    ('P', 'Perempuan')
)

STATUS_SISWA = (
    (1, 'aktif'),
    (2, 'keluar/pindah'),
    (3, 'lulus'),
    (4, 'meninggal')
)


# Create your models here.
class Pegawai(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    # alamat = models.ForeignKey(Alamat, related_name='alamat_pegawai', on_delete=models.SET_NULL, null=True)
    no_hp = models.CharField(max_length=30)
    # pendidikan_terakhir = models.ForeignKey(Pendidikan, related_name='pendidikan_terakhir_pegawai',
                                            # on_delete=models.SET_NULL, null=True)
    pendidikan_terakhir = models.IntegerField(default=3, choices=JENJANG_PENDIDIKAN)
    tempat_lahir = models.CharField(max_length=50, null=True, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    provinsi = models.CharField(default='', max_length=30)
    kota = models.CharField(default='', max_length=30)
    kecamatan = models.CharField(default='', max_length=30)
    kelurahan = models.CharField(default='', max_length=30)
    alamat = models.TextField(default='')
    nbm = models.CharField(max_length=30, null=True)
    status = models.IntegerField(default= 1, choices=STATUS_PEGAWAI)
    jabatan = models.CharField(max_length=30)
    gol = models.CharField(max_length=10)
    pangkat = models.CharField(max_length=20)
    tmt = models.DateField(null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank= True)

    @property
    def nama_lengkap(self):
         return self.user.get_username()
    
    @property
    def set_nama(self, first_name, last_name):
        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.save()
        return self
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    def __str__(self):
        return self.nama_lengkap



KELOMPOK_PENGHASILAN = (
    (1, '0-500.000 rupiah/bulan'),
    (2, '500.001-1.000.000 rupiah/bulan'),
    (3, '1.000.001-2.000.000 rupiah/bulan'),
    (4, '2.000.001-4.500.000 rupiah/bulan'),
    (5, '4.500.001-6.000.000 rupiah/bulan'),
    (5, 'lebih dari 6.000.000 rupiah/bulan'),
)


class WaliSiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    no_hp = models.CharField(max_length=30)   
    pendidikan_terakhir = models.IntegerField(default=3, choices=JENJANG_PENDIDIKAN)
    pekerjaan = models.CharField(max_length=100, default='-')
    penghasilan = models.IntegerField(choices=KELOMPOK_PENGHASILAN, default=3)
    provinsi = models.CharField(default='', max_length=30)
    kota = models.CharField(default='', max_length=30)
    kecamatan = models.CharField(default='', max_length=30)
    kelurahan = models.CharField(default='', max_length=30)
    alamat = models.TextField(default='')
    profile_pic = models.ImageField(default="profile.png", null=True, blank= True)
    

    @property
    def nama_lengkap(self):
        return self.user.get_username()
    
    @property
    def set_nama(self, first_name, last_name):
        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.save()
        return self
    
    def __str__(self):
        return self.nama_lengkap
    
class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    nis = models.CharField(max_length=20, editable=True,blank=True, )
    nisn = models.CharField(max_length=20, editable=True,blank=True, )
    tahun_angkatan = models.IntegerField(default=2022)
    nama_siswa = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(null=True)
    # alamat = models.ForeignKey(Alamat, on_delete=models.SET_NULL, related_name='alamat_siswa', null=True)
    wali_siswa = models.ForeignKey(WaliSiswa, on_delete=models.SET_NULL, related_name='siswa', null=True, blank=True)
    is_abk = models.BooleanField(default=False)
    # shadow_teacher = models.ForeignKey(Pegawai, related_name='siswa_abk', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS_SISWA, default=1)

    def __str__(self):
        return self.nama_siswa
    
# MODEL AG

class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_kelas

class Ruangan(models.Model):
    nama_ruangan = models.CharField(max_length=50)
    kelas = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nama_ruangan
    
class Jam(models.Model):
  waktu_mulai = models.TimeField()
  waktu_selesai = models.TimeField()
  
  def __str__(self):
    return '{} - {}'.format(self.waktu_mulai, self.waktu_selesai)

class Hari(models.Model):
  nama_hari = models.CharField(max_length=50)
  jam = models.ForeignKey(Jam, on_delete=models.SET_NULL, null=True)
  
  def __str__(self):
    return self.nama_hari

class MataPelajaran(models.Model):
    nama_mapel = models.CharField(max_length=50)
    kelas = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True)
    waktu = models.IntegerField()
    
    def __str__(self):
        return '{} - {}'.format(self.nama_mapel, self.kelas)
        

class Guru(models.Model):
    nama = models.CharField(max_length=30)
    alamat = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    status = models.IntegerField(choices=STATUS_PEGAWAI, default=1)
   
    
    def __str__(self):
        return f'{self.nama}'
    
class Tugas(models.Model):
    mapel = models.ForeignKey(MataPelajaran, on_delete=models.SET_NULL, null=True)
    guru = models.ForeignKey(Guru, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.guru} {self.mapel}'

    
class Jadwal(models.Model):
  tugas = models.ForeignKey(Tugas, on_delete=models.SET_NULL, null=True)  
  waktu = models.ForeignKey(Hari, on_delete=models.SET_NULL, null=True)  

  def __str__(self):
    return f'{self.tugas} {self.waktu}'
    

class Excelfile(models.Model):
    file = models.FileField(upload_to='files')
   


