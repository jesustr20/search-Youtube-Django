import json
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
import requests
from urllib import parse, request
from os import close
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from .forms import SearchYoutubeForm
from community.models import EnlacesAPI, Community_info

from urllib import parse, request


class SearchPrivate(View):
    template_name = 'searchchannel.html'
    api_key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

    def get(self, request, *args, **kwargs):
        context = {}
        q = context['search'] = request.GET.get("q", "")
        if q:
            # context['data_api'] = self.getDataYoutube(q)
            context['data_api'] = self._get_channels_from_json_file(q, 3)
        return render(request, 'searchchannel.html', {'context': context})

    def _get_channels_from_json_file(self, search, quantity_channels):
        with open('C:/Proyectos/proyecto_librosFree/Proyecto_uno_libros/community/channels2.json', 'r', encoding='utf-8') as f:
            items = json.load(f)
        items['title'] = search
        list_data = [items for i in range(quantity_channels)]
        return list_data

    def getDataYoutube(self, q):
        url_search_channel = 'https://youtube.googleapis.com/youtube/v3/search'
        channels = []

        params_search_channel = {
            'part': 'snippet',
            'maxResults': 2,
            'q': q,
            'type': 'channel',
            'key': self.api_key
        }

        channel_items = self._get_api_items(
            url_search_channel, params_search_channel)

        for channel_item in channel_items:
            channel_id = channel_item['snippet']['channelId']
            channel = {
                'id': channel_item['snippet']['channelId'],
                'title': channel_item['snippet']['title'],
                'description': channel_item['snippet']['description'],
                'image': channel_item['snippet']['thumbnails']['default']['url'],
                'playlists': []
            }
            playlist_data = self.playlistData(channel_id)
            channel['playlists'] = playlist_data
            channels.append(channel)
        return channels

    def playlistData(self, channel_id):
        url_linkPlayList = 'https://youtube.googleapis.com/youtube/v3/playlists'

        playlists = []

        params_playlist = {
            'key': self.api_key,
            'part': 'snippet',
            'channelId': channel_id,
            'maxResults': 5,
        }

        playlists_items = self._get_api_items(
            url_linkPlayList, params_playlist)

        for playlists_item in playlists_items:
            playlist = {
                'id': playlists_item['id'],
                'title': playlists_item['snippet']['title'],
                'publishedAt': playlists_item['snippet']['publishedAt'],
                'image': playlists_item['snippet']['thumbnails']['default']['url']
            }
            playlists.append(playlist)

        return playlists

    def _get_api_items(self, url, params):
        url_params = parse.urlencode(params)
        with request.urlopen(url + '?' + url_params) as response:
            json_response = json.loads(response.read())
        return json_response['items']


class YoutubeView(TemplateView):
    template_name = 'youtube.html'
    api_key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        url_link = 'https://youtube.googleapis.com/youtube/v3/search'
        url_linkPlayList = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
        part = 'snippet'
        maxResults = 2
        q = 'Programación ATS'
        channelId = 'UC7QoKU6bj1QbXQuNIjan82Q'
        # playlistId = 'PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj'
        type = 'playlist'
        key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

        # urlPLaylist = f'{url_linkPlayList}?part={part}&playlistId={playlistId}&key={key}'

        url = requests.get(
            f'{url_link}?part={part}&channelId={channelId}&maxResults={maxResults}&q={q}&type={type}&key={key}')
        api = url.json()
        items = api['items']
        context['data'] = api
        context['items'] = items

        for i in items:
            ides = i['id']
            playlistId = ides['playlistId']
            title = i['snippet']
            channelTitle = title['channelTitle']
            print(playlistId)

        context['snippet'] = title
        context['channelTitle'] = channelTitle
        context['id'] = ides
        context['playlistId'] = playlistId

        # context = self.channelData()
        context = self._get_channels_from_json_file(3)
        return {'context': context}

    def _get_channels_from_json_file(self, quantity_channels):
        with open('C:/Proyectos/proyecto_librosFree/Proyecto_uno_libros/community/channels2.json', 'r', encoding='utf-8') as f:
            items = json.load(f)
        list_data = [items for i in range(quantity_channels)]
        return list_data

    def channelData(self):
        url_link = 'https://youtube.googleapis.com/youtube/v3/search'

        CHANNEL_NAME = 'Programación ATS'

        params_channel = {
            'key': self.api_key,
            'part': 'snippet',
            'q': CHANNEL_NAME,
            'type': 'channel',
            'maxResults': 2
        }
        url_values = parse.urlencode(params_channel)
        with request.urlopen(url_link + '?' + url_values) as response:
            json_response = json.loads(response.read())
        channel_items = json_response['items']

        channels = []
        channel_ids = []

        for channel_item in channel_items:
            channel_id = channel_item['snippet']['channelId']
            channel = {
                'id': channel_item['snippet']['channelId'],
                'title': channel_item['snippet']['title'],
                'description': channel_item['snippet']['description'],
                'image': channel_item['snippet']['thumbnails']['default']['url'],
                'playlists': []
            }
            print(channel_id)
            playlist_data = self.playlistData(channel_id)
            channel['playlists'] = playlist_data
            channels.append(channel)

        return channels

    def playlistData(self, channel_id):
        url_linkPlayList = 'https://youtube.googleapis.com/youtube/v3/playlists'
        api_key = 'AIzaSyAz9mAAmXf7eVzsabaSK5C1Q0VAS6VyZkw'

        params_playlist = {
            'key': api_key,
            'part': 'snippet',
            'channelId': channel_id,
            'maxResults': 3
        }
        url_values = parse.urlencode(params_playlist)
        with request.urlopen(url_linkPlayList + '?' + url_values) as response:
            json_response = json.loads(response.read())
        playlists_items = json_response['items']

        playlists = []

        for playlists_item in playlists_items:
            playlist = {
                'id': playlists_item['id'],
                'title': playlists_item['snippet']['title'],
                'publishedAt': playlists_item['snippet']['publishedAt'],
                'image': playlists_item['snippet']['thumbnails']['default']['url']
            }
            playlists.append(playlist)

        return playlists


class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context


class ChannelYTView(TemplateView):
    template_name = 'channelYoutube.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        with open('community/channels.json', 'r') as f:
            context['channel'] = json.load(f)
            print(context)
            return context
