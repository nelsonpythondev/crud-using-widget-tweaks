from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('listsiswa', views.siswa_view, name="list-siswa"),
    path('addsiswa', views.add_siswa, name="add-siswa"),
    path('editsiswa/<int:id>', views.edit_siswa, name="edit-siswa"),
    path('deletesiswa/<int:id>', views.delete_siswa, name="delete-siswa"),
]
