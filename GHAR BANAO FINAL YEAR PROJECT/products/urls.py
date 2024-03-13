from . import views
from django.urls import path
urlpatterns = [
    path('gsporduct/', views.productviewMainpage.as_view() , name = 'gsproduct'),
    path('gsporductpage/', views.productview.as_view() , name = 'gsproductpage'),
    path('prod_det/<int:pk>', views.prod_detView.as_view() , name = 'prod_det'),
    path('add-to-cart/', views.addtocart , name = 'add-to-cart'),
    path('cart/', views.showcart , name = 'showcart'),
    # path('delete/<str:id>', views.remove_cart , name = 'delete'),
    path('checkout/', views.checkout , name = 'checkout'),
    path('procedtopay/', views.procedtopay , name = 'procedtopay'),
    path('removecart/', views.removecart , name = 'removecart'),
    path('dispcustodr/', views.disp_customerorder , name = 'dispcustodr'),
    

]