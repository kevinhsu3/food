from . import views
from django.urls import path 

app_name = 'food' # namespace (to distinguish between different apps)
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(), name='index'),
    #/food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # /food/add # add items
    path('add', views.CreateItem.as_view(), name='create_item'),
    # /food/update/1 # edit
    path('update/<int:item_id>/', views.update_item, name='update_item'),  
    # /food/delete/1 # delete
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]