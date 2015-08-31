from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'login_signup.views.log_in', name='login'),
    url(r'^signup/$', 'login_signup.views.signup', name='signup'),
    url(r'^verification/(.*)$', 'login_signup.views.verify', name='verification'),
    url(r'^forgot_step_1$', 'login_signup.views.forgot_password_1', name='fpw1'),
    url(r'^forgot_step_2/(.*)/(\d+)$', 'login_signup.views.forgot_password_2', name='fpw2'),
]
