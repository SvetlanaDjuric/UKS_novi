from django.urls import path

from . import views

app_name = 'github'
urlpatterns = [
    path('', views.switch_home, name='home'),
    path('registration', views.switch_registration, name='registration'),
    path('save_user', views.save_user, name='save_user'),
    path('activate_user/<username>', views.activate_user, name='activate_user'),

    path('login', views.switch_login, name='login'),
    path('login_user', views.login_user, name='login_user'),

    path('forgot_password', views.switch_forgot_password, name='forgot_password'),
    path('reset_password/', views.send_email_reset_password, name='reset_password'),
    path('password_reset/<username>', views.switch_forgot_password_reset, name='password_reset'),
    path('insert_reset_password', views.reset_password, name='insert_reset_password'),

    path('logout', views.logout, name='logout'),

    path('about_user',views.about_user, name='about_user'),

    path('switch_change_username',views.switch_change_username, name='switch_change_username'),
    path('change_username',views.change_username, name='change_username'),

    path('switch_change_password',views.switch_change_password, name='switch_change_password'),
    path('change_password',views.change_password, name='change_password'),

    path('switch_delete_account',views.switch_delete_account, name='switch_delete_account'),
    path('delete_account',views.delete_account, name='delete_account'),

    path('organization', views.organization, name='organization'),
    path('saveOrganization', views.saveOrganization, name='saveOrganization'),
    path('saveOrganizationDetails', views.saveOrganizationDetails, name='saveOrganizationDetails'),

    #issue
    path('switch_all_issues', views.switch_issue_show_all, name='switch_all_issues'),
    path('issue_show_all_open', views.issue_show_all_open, name='issue_show_all_open'),
    path('issue_show_all_closed', views.issue_show_all_closed, name='issue_show_all_closed'),

    path('switch_issue_new', views.switch_issue_new, name='switch_issue_new'),
    path('issue_new', views.issue_new, name='issue_new'),
    path('switch_issue_view_one/<id>', views.switch_issue_view_one, name='switch_issue_view_one'),
    path('issue_edit_title/<id>', views.issue_edit_title, name='issue_edit_title'),
    path('issue_close/<id>', views.issue_close, name='issue_close'),
    path('issue_reopen/<id>', views.issue_reopen, name='issue_reopen'),

    #comment
    path('comment_new/<id>', views.comment_new, name='comment_new'),
    path('comment_edit/<idIssue>/<idComment>', views.comment_edit, name='comment_edit'),
    path('comment_delete/<id>', views.comment_delete, name='comment_delete'),
    path('comment_reply/<idIssue>/<idComment>', views.comment_reply, name='comment_reply'),

    #label
    path('switch_label_show_all', views.switch_label_show_all, name='switch_label_show_all'),
    path('switch_label_new', views.switch_label_new, name='switch_label_new'),
    path('label_new', views.label_new, name='label_new'),
    path('label_edit', views.label_edit, name='label_edit'),


    path('saveOrganizationMembers/<str:name>', views.saveOrganizationMembers, name='saveOrganizationMembers'),
    path('repository/<str:p>', views.repository, name='repository'),
    path('saveRepository/<str:p>', views.saveRepository, name='saveRepository'),
    path('saveRepositoryMembers/<str:name>', views.saveRepositoryMembers, name='saveRepositoryMembers'),
    path('repositoriesShow', views.repositoriesShow, name='repositoriesShow'),
    path('organizationsShow', views.organizationsShow, name='organizationsShow'),
    path('organizationInfo/<str:name>', views.organizationInfo, name='organizationInfo'),
    path('addNewMemberOrganization/<str:name>', views.addNewMemberOrganization, name='addNewMemberOrganization'),
    path('repositoryInfo/<str:name>', views.repositoryInfo, name='repositoryInfo'),
    path('addNewMemberRepository/<str:name>', views.addNewMemberRepository, name='addNewMemberRepository'),
    path('organizationsByUser', views.organizationsByUser, name='organizationsByUser'),
    path('switch_delete_organization/<str:name>', views.switch_delete_organization, name='switch_delete_organization'),
    path('delete_organization/<str:name>', views.delete_organization, name='delete_organization'),
    path('switch_delete_repository/<str:name>', views.switch_delete_repository, name='switch_delete_repository'),
    path('delete_repository/<str:name>', views.delete_repository, name='delete_repository'),
    path('switch_edit_repository/<str:name>', views.switch_edit_repository, name='switch_edit_repository'),
    path('edit_repository/<str:name>', views.edit_repository, name='edit_repository'),
    path('switch_edit_organization/<str:name>', views.switch_edit_organization, name='switch_edit_organization'),
    path('edit_organization/<str:name>', views.edit_organization, name='edit_organization'),

]