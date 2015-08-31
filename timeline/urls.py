from django.conf.urls import include, url
from MyTraveler.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^timeline/$', 'timeline.views.show_timeline', name='timeline'),
    url(r'^logout/$', 'timeline.views.log_out', name='logout'),
    url(r'^profile$', 'timeline.views.show_profile', name='profile'),
    url(r'^board/(\d+)$', 'timeline.views.show_board', name='board'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, }),
]
