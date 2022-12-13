from django.urls import path
from .views import index, indexPageView, generatePageView, viewListPageView, editStudPageView, editSingleStudentPageView, saveRestsPageView, deleteStudPageView, changeRestrictionsPageView

urlpatterns = [
    path('', index, name='index'),
    path('index/', indexPageView, name='indexNav'),
    path('generate/', generatePageView, name='generate'),
    path('viewList/', viewListPageView, name='viewList'),
    path('edit/<int:stud_id>/', editStudPageView, name='editStud'),
    path('editSS/<int:stud_id>', editSingleStudentPageView, name='editSingleStud'),
    path('delete/<int:stud_id>/', deleteStudPageView, name='deleteStud'),
    path('restrictions/<int:stud_id>/', changeRestrictionsPageView, name='changeRestrictions'),
    path('saveRests/<int:stud_id>/', saveRestsPageView, name='updateRestrictions'),
]


