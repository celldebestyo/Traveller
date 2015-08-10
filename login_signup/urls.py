from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', 'login_signup.views.log_in', name='login'),
    url(r'^signup/', 'login_signup.views.signup', name='signup'),
    url(r'^timeline/', 'login_signup.views.timeline', name='timeline'),
    url(r'^logout/', 'login_signup.views.log_out', name='logout')
]
