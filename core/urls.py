
from django.urls import path,include

from core import views
from .import excelviews, jadwalviews


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register-pegawai/', views.registerPage_Pegawai, name='registerpegawai'),
    path('register_walisiswa/', views.registerPage_Walisiswa, name='registerwalisiswa'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('pegawai/', views.form_Pegawai, name='pegawai'),
    path('pegawai/create_pegawai/', views.create_Pegawai, name='create_pegawai'),
    path('pegawai/update_pegawai/<str:pk>/', views.update_Pegawai, name='update_pegawai'),
    path('pegawai/delete_pegawai/<str:pk>/', views.delete_Pegawai, name='delete_pegawai'),
    path('pegawai/pegawai-import/', excelviews.upload_file_Pegawai, name='importpegawai'),
    path('pegawai/pegawai-export', excelviews.export_filepegawai, name='exportpegawai'), 
    #User Pegawai
    path('pegawai-user/', views.userPage_Pegawai, name='userpage_pegawai'),
    path('pegawai-user/pegawai-create/', views.userCreate_Pegawai, name='usercreate_pegawai'),
    path('pegawai-user/pegawai-view/', views.userView_Pegawai, name='userview_pegawai'),
    path('pegawai-user/pegawai-overview/', views.view_Pegawai, name='overview_pegawai'),
    
    
    
    
    path('walisiswa/', views.form_Walisiswa, name='walisiswa'),
    path('walisiswa/create_walisiswa/', views.create_Walisiswa, name='create_walisiswa'),
    path('walisiswa/update_walisiswa/<str:pk>/', views.update_Walisiswa, name='update_walisiswa'),
    path('walisiswa/delete_walisiswa/<str:pk>/', views.delete_Walisiswa, name='delete_walisiswa'),
    # User Walisiswa
    path('walisiswa-user/', views.userPage_Walisiswa, name='userpage_walisiswa'),
    path('walisiswa-user/walisiswa-create/', views.userCreate_Walisiswa, name='usercreate_walisiswa'),
    path('walisiswa-user/walisiswa-view/', views.userView_Walisiswa, name='userview_walisiswa'),
    path('walisiswa-user/walisiswa-overview/', views.view_Walisiswa, name='overview_walisiswa'),
    
    # path('kelas/baru/', views.kelasbaru, name='kelasbaru'),
    
    
    
    path('Siswa/', views.form_Siswa, name='Siswa'),
    # path('Siswa/create_Siswa/', views.create_Siswa, name='create_Siswa'),
    path('Siswa/update_Siswa/<str:pk>/', views.update_Siswa, name='update_Siswa'),
    path('Siswa/delete_Siswa/<str:pk>/', views.delete_Siswa, name='delete_Siswa'),
    
    path('siswa-user/siswa-create/', views.userCreate_Siswa, name='usercreate_siswa'),
    path('siswa-user/siswa-view/', views.userView_Siswa, name='userview_siswa'),
    
    
    # URL PENJADWALAN
    
    path('kelas/', jadwalviews.form_Kelas, name='kelas'),
    path('kelas/create_kelas/', jadwalviews.create_Kelas, name='create_kelas'),
    path('kelas/update_kelas/<str:pk>/', jadwalviews.update_Kelas, name='update_kelas'),
    path('kelas/delete_kelas/<str:pk>/', jadwalviews.delete_Kelas, name='delete_kelas'),
    path('kelas/kelas-import/', excelviews.upload_file_Kelas, name='importkelas'),
    path('kelas/kelas-export', excelviews.export_filekelas, name='exportkelas'),
    
    # # # RUANGAN
    path('ruangan/', jadwalviews.form_Ruangan, name='ruangan'),
    path('ruangan/create', jadwalviews.create_Ruangan, name='create_ruangan'),
    path('ruangan/update/<str:pk>/', jadwalviews.update_Ruangan, name='update_ruangan'),
    path('delete_ruangan/<str:pk>/', jadwalviews.delete_Ruangan, name='delete_ruangan'),
    path('ruangan/ruangan-import/', excelviews.upload_file_Ruangan, name='importruangan'),
    
    path('jam/', jadwalviews.form_jam, name='jam'),
    path('jam/create', jadwalviews.create_jam, name='create_jam'),
    path('jam/update/<str:pk>/', jadwalviews.update_jam, name='update_jam'),
    path('delete_jam/<str:pk>/', jadwalviews.delete_jam, name='delete_jam'),
    path('jam/jam-import/', excelviews.upload_file_jam, name='importjam'),
    path('jam/jam-export/', excelviews.export_jam, name='exportjam'),
    
    path('hari/', jadwalviews.form_hari, name='hari'),
    path('hari/create', jadwalviews.create_hari, name='create_hari'),
    path('hari/update/<str:pk>/', jadwalviews.update_hari, name='update_hari'),
    path('delete_hari/<str:pk>/', jadwalviews.delete_hari, name='delete_hari'),
    path('hari/hari-import/', excelviews.upload_file_hari, name='importhari'),
    path('hari/hari-export/', excelviews.export_hari, name='exporthari'),
    
    # # # GURU
    path('guru/', jadwalviews.form_Guru, name='guru'),
    path('guru/create', jadwalviews.create_Guru, name='create_guru'),
    path('guru/update/<str:pk>/', jadwalviews.update_Guru, name='update_guru'),
    path('delete_guru/<str:pk>/', jadwalviews.delete_Guru, name='delete_guru'),
    path('guru/guru-import/', excelviews.upload_file_Guru, name='importguru'),
     path('guru/guru-export/', excelviews.upload_file_Guru, name='exportguru'),
    

    
    # # # # MATAPELJARAN
    path('mapel/', jadwalviews.form_Mapel, name='mapel'),
    path('mapel/create', jadwalviews.create_Mapel, name='create_mapel'),
    path('mapel/update/<str:pk>/', jadwalviews.update_Mapel, name='update_mapel'),
    path('delete_mapel/<str:pk>/', jadwalviews.delete_Mapel, name='delete_mapel'),
    path('mapel/mapel-import/', excelviews.upload_file_mapel, name='importmapel'),
    path('mapel/mapel-export/', excelviews.export_mapel, name='exportmapel'),
    
    
    path('tugas/', jadwalviews.form_tugas, name='tugas'),
    path('tugas/create', jadwalviews.create_tugas, name='create_tugas'),
    path('tugas/update/<str:pk>/', jadwalviews.update_tugas, name='update_tugas'),
    path('delete_tugas/<str:pk>/', jadwalviews.delete_tugas, name='delete_tugas'),
    path('tugas/tugas-import/', excelviews.upload_file_tugas, name='importtugas'),
    path('tugas/tugas-export/', excelviews.export_tugas, name='exporttugas'),

    path('generate/', jadwalviews.generate, name='generate'),
    path('jadwal/', jadwalviews.jadwal_views, name='jadwal'),
    path('jadwal/export/', excelviews.export_jadwal, name='exportjadwal'),
    
    

    path('dashboard/', views.index, name='index'),
    # path('baru/', views.upload_file_view, name='upload-view'),
    
    
    # template baruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
   
   
   
    
]
handler404 = 'core.views.error_404'



