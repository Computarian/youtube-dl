# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

import re


class tveastIE(InfoExtractor):

    _VALID_URL = r'https?://(?:www\.)?\.?tveast\.dk/'
    
    

    _TEST = {
        'url': 'https://www.tveast.dk/tv-ost-reportagen/tv-ost-reportagen-samleren-fra-norreballe',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'Video title goes here',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }


  
    def _real_extract(self, url):
        #header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
       
        video_id = self._match_id(url)

        
        #webpage = self._download_webpage(url, video_id)


        return {
            'id': video_id,
            'url': 'site_id',
            #'url': 'https://videos.tirerack.com/pdl/aa/73/aa732da5-5774-4abf-9d73-554121d0df29/03_Tire_Decision_Guide_30_800k.mp4',
            'title': 'title',
            'description': 'description',
            'header': {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            #'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }