from django.urls import path
from . import views
from django.conf.urls import url ,include
from django.contrib import admin
from django.conf.urls import url ,include
from . import  views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('signup/', views.SignUp.as_view(), name='signup'),
    #url(r'^login/$', views.login_user),
    url('terms/', views.terms_conditions, name='terms'),
    url('signin/', views.sign_in, name='signin'),
    url(r'^signup/$', views.signs, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url('register/', views.register, name='register'),
    url('agency/add/', views.create_agency, name='create_agency'),
    url('prop/add/', views.create_prop, name='add_property'),
    url('prop/editor/?page=(?P<page>.*)$', views.edit_prop, name='edit_property'),
    url(r'^prop/edit/?page=(?P<page>.*)$', views.edit_props, name='edit_prop'),
    url('prop/fav/', views.add_bookmark, name='fav_property'),
    url(r'^$', views.home, name='home'),
    url('slider/', views.slider, name='slider'),
    url('contact/', views.contact, name='contact'),
    url('comments/?page=(?P<page>.*)$', views.comments, name='comments'),
    url('shortcodes/', views.shortcodes, name='shortcodes'),
    url('about/us/', views.about_us, name='about_us'),
    url('about/us/', views.about_us, name='about_us'),
    url('agency/agents/', views.my_agents, name='my_agents'),
    url('agency/create/prop/', views.agency_create_prop, name='agency_create_prop'),
    url('agency/assign/', views.assign_agents, name='assign'),
    url('agency/deactivate/', views.deactivate_agents, name='deactivate_agents'),
    url('agency/accept/', views.accept_agents, name='agency_accept'),
    url('agency/assignprop/', views.assign_prop, name='prop_assign'),
    url('agency/transfare/', views.prop_transfare, name='prop_transfare'),
    url('agency/trans/', views.prop_trans, name='prop_trans'),
    url('agency/profile/', views.agency_profile, name='agency_profile'),
    url('agent/detail/', views.agent_detail, name='agent_detail'),
    url('email/activate/', views.emailactivate , name='email_activate'),
    url('invoice/', views.invoice, name='invoice'),
    url('profile/', views.profile, name='profile'),
    #url('user/profile/', views.userprofile, name='user_profile'),
    #url('home/profile/', views.homeprofile, name='home_profile'),
    url('prop/details', views.property_detail, name='property_detail'),
    url('prop/detail/?page=(?P<page>.*)$', views.property_details, name='property_det'),
    url('prop/listing/tile', views.property_listing, name='property_listing'),
    url('agent/listing', views.agents_listing, name='agent_listing'),
    url(r'^agency/detail/$', views.agency_detail, name='agency_detail'),
    url(r'^agency/listing/$', views.agency_listing, name='agency_listing'),
    url('prop/listing/grid', views.property_grid_listing, name='property_grid_listing'),
    url('prop/listing/line', views.property_line_listing, name='property_line_listing'),
    url('prop/', views.my_properties, name='my_properties'),
    url('bookmarked/', views.bookmarked, name='bookmarked'),
    url('fourzerothree/', views.fourzerothree, name='403'),
    url('fourzerofour/', views.fourzerofour, name='404'),
    url('fivehundred/', views.fivehundred, name='500'),
    url('faq/', views.faq, name='faq'),
    url(r'^password/$', views.change_password, name='change_password'),
    url('right/side/', views.right_side, name='right_side'),
    url('left/side/', views.left_side, name='left_side'),
    url('submit/', views.submit, name='submit'),
    url('timeline/', views.timeline, name='timeline'),
    url('rtl/', views.rtl, name='rtl'),
    url('terms/conditions/', views.terms_conditions, name='terms_conditions'),
    url('upload/', views.simple_upload, name='upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)