from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page,name="home"),
    path("login/",views.login_page,name="login"),
    path("register/",views.register_page,name="register"),
    path("user_page/",views.user_page,name="user_page"),
    path("add_owner/",views.add_owners,name="add_owner"),
    path("search/",views.user_ds,name="search"),
    path("search_service/",views.search_serviceplace,name="search_service"),
    path("bookings/",views.bookings_page,name="bookings"),
    path("search_service_add/",views.add_service,name="search_service_add"),
    path("service_center/",views.service_center_ds,name="service_center"),
    path("add_mechanic/",views.add_mechanic,name="add_mechanic"),
    path("booking_page/<int:service_center_id>/",views.booking_page,name="booking_page"),
    path("delete_machanic/<int:pk>/",views.delete_machanic,name="delete_machanic"),
    path("update_mechanic/<int:pk>/",views.update_mechanic,name="update_mechanic"),
    path("mechanic_dashbord/",views.mechanic_dashbord,name="mechanic_dashbord"),
    path("update_order/<int:pk>/",views.update_staus,name="update_order"),
    path("mybooking/",views.mybooking_page,name="mybooking"),
    path("lagout_page/",views.lagout_page,name="lagout_page"),
    path("contact_page/",views.contact_page,name="contact_page"),
    path("delete_service_center/<int:pk>/",views.delete_service_center,name="delete_service_center"),
    path("edit_branch/<int:pk>/",views.edit_branch,name="edit_branch")
    
]