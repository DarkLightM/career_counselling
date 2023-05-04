import time

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from speechkit.auth import generate_jwt

from .forms import *
from .models import *
from profiles.models import Profile
from speechkit import RecognitionLongAudio, Session

from pydub import AudioSegment


class Transcribers(ListView):
    model = Transcriber
    template_name = 'transcriber/index.html'
    context_object_name = 'transcribers'

    def get_queryset(self):
        return Transcriber.objects.filter(profile__slug=self.kwargs['profile_slug'])


class AddFile(CreateView):
    form_class = AddFileForm
    template_name = 'transcriber/add_transcribe_file.html'


class TranscriberText(DetailView):
    model = Transcriber
    template_name = 'transcriber/transcriber_text.html'
    context_object_name = 'transcriber'

    def get_object(self, queryset=None):
        return Transcriber.objects.get(slug=self.kwargs['transcriber_slug'])


def transcribe_audio(request, profile_slug, transcriber_slug):
    from career_counseling.settings import SERVICE_ACCOUNT_ID, YANDEX_PRIVATE_KEY, YANDEX_KEY_ID, \
        BUCKET_NAME

    jwt = generate_jwt(SERVICE_ACCOUNT_ID, YANDEX_KEY_ID, YANDEX_PRIVATE_KEY.replace('\\n', '\n').encode('utf-8'))
    session = Session.from_jwt(jwt)

    recognize_long_audio = RecognitionLongAudio(session, SERVICE_ACCOUNT_ID, BUCKET_NAME,
                                                aws_access_key_id="AWS_KEY",
                                                aws_secret="AWS_SECRET")

    transcriber = Transcriber.objects.get(slug=transcriber_slug)

    recognize_long_audio.send_for_recognition(
        transcriber.audio_source.path, audioEncoding='LINEAR16_PCM', sampleRateHertz='48000',
        audioChannelCount=1, rawResults=False
    )

    recognize_long_audio.get_recognition_results()

    text = recognize_long_audio.get_raw_text()
    transcriber.transcribe_text = text
    transcriber.save()
    #print("TEXT: ", text)
    return redirect('transcriber_home', profile_slug)
