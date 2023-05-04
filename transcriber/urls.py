from django.urls import path

from transcriber.views import *

urlpatterns = [
    path('', Transcribers.as_view(), name='transcriber_home'),
    path('transcriber/<slug:transcriber_slug>/', TranscriberText.as_view(), name='transcriber'),
    path('transcriber/<slug:transcriber_slug>/transcribe/', transcribe_audio, name='transcribe_audio'),
    path('add_file/', AddFile.as_view(), name='add_file')
]
