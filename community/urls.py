from django.urls import path
from community.views import PortadaView, ChannelYTView, YoutubeView, SearchPrivate

urlpatterns = [
    path('', PortadaView.as_view(), name='inicio'),
    path('channelYoutube/', ChannelYTView.as_view(), name='channelYoutube'),
    path('youtube/', YoutubeView.as_view(), name='youtube'),
    path('searchchannel/', SearchPrivate.as_view(), name='searchchannel'),
]
