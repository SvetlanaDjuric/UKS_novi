from django.urls import path

from . import views

app_name = 'github'
urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('saveUser', views.saveUser, name='saveUser'),
    path('activate_user/<username>', views.activate_user, name='activate_user'),
    path('login', views.login, name='login'),
    path('organization', views.organization, name='organization'),
    path('saveOrganization', views.saveOrganization, name='saveOrganization'),
    path('saveOrganizationDetails', views.saveOrganizationDetails, name='saveOrganizationDetails'),
    path('saveOrganizationMembers/<str:name>', views.saveOrganizationMembers, name='saveOrganizationMembers'),
    path('repository/<str:name>', views.repository, name='repository'),
    path('saveRepository/<str:organization>', views.saveRepository, name='saveRepository'),
    path('saveRepositoryMembers', views.saveRepositoryMembers, name='saveRepositoryMembers'),
    path('repositoriesShow', views.repositoriesShow, name='repositoriesShow'),
    path('organizationsShow', views.organizationsShow, name='organizationsShow'),
    path('organizationInfo/<str:name>', views.organizationInfo, name='organizationInfo'),
    path('addNewMemberOrganization/<str:name>', views.addNewMemberOrganization, name='addNewMemberOrganization'),

]