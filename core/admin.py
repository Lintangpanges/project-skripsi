from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from core.models import *



# Register your models here.


class ImportExportAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_filter = [field.name for field in model._meta.fields
                            if field.name != 'id' and
                            not isinstance(field, models.ForeignKey) and
                            not isinstance(field, models.ManyToManyField) and
                            not isinstance(field, models.OneToOneField)]
        self.search_fields = [field.name for field in model._meta.fields
                              if field.name != 'id' and
                              not isinstance(field, models.ForeignKey) and
                              not isinstance(field, models.ManyToManyField) and
                              not isinstance(field, models.OneToOneField)
                              ]
        super(ImportExportAdmin, self).__init__(model, admin_site)


admin_class = type('AdminClass', (ImportExportAdmin, admin.ModelAdmin), {})

# admin.site.register(Alamat, admin_class)
# admin.site.register(Pendidikan, admin_class)
admin.site.register(Pegawai, admin_class)
admin.site.register(WaliSiswa, admin_class)
admin.site.register(Kelas, admin_class)
admin.site.register(Siswa, admin_class)
admin.site.register(Excelfile, admin_class)

# model penjadwalan
admin.site.register(Ruangan, admin_class)
admin.site.register(Guru, admin_class)
admin.site.register(Jam, admin_class)
admin.site.register(Hari, admin_class)
admin.site.register(Tugas, admin_class)
admin.site.register(MataPelajaran, admin_class)








