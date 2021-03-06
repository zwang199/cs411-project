from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^search_for/', views.search_page, name='explore'),
    url(r'^add/', views.enter, name='add something'),
    url(r'^add_i/', views.ai, name='add_i'),
    url(r'^add_j/', views.aj, name='add_j'),
    url(r'^add_m/', views.am, name='add_m'),
    url(r'^pour/', views.pour),
    url(r'^result/', views.get_list),
    url(r'^result_tag/', views.get_list_tag),
    url(r'^result_macro/', views.get_list_macro),
    url(r'^show/', views.show_result),
    url(r'^show_ingredient/', views.show_ingredient),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^success/', views.return_success)
]
