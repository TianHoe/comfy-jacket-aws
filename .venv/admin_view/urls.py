from django.urls import path
from admin_view import views

urlpatterns = [
    path('', views.ShowAllBouquet, name='showBouquets'),
    path('bouquet/<int:pk>/', views.BouquetDetails, name='bouquet'),
    path('addbouquet/', views.addBouquet, name='addbouquet'),
    path('addcategory/', views.addCategory, name='addcategory'),
    path('updatebouquet/<int:pk>/', views.updateBouquet, name='updatebouquet'),
    path('deletebouquet/<int:pk>/', views.deleteBouquet, name='deletebouquet'),
    path('deletecatgory/<int:pk>/', views.deleteCategory, name='deletecategory'),
    path('search/', views.searchEngine, name='search'),
    path('orders/', views.vieworder, name='orders'),
]