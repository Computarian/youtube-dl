# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class TireRackIE(InfoExtractor):
    #_VALID_URL = r'https?://(?:www\.)?tirerack\.com/watch/(?P<id>[0-9]+)'
    #_VALID_URL = r'https?://(?:www\.)?tirerack\.com/videos/(?P<id>[0-9]+)'
    _VALID_URL = r'https?://(?:www\.)?videos\.?tirerack\.com/videos/'
    
    

    _TEST = {
        'url': 'https://www.tirerack.com/videos/index.jsp?video=545',
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

    def _extract_video(self, source):
        return {
            'id': source.get('videoId'),
            'title': source.get('title'),
            'description': source.get('description'),
            'thumbnail': source.get('highResImage') or source.get('medResImage'),
            'uploader': source.get('username'),
            'duration': int_or_none(source.get('length')),
            'view_count': int_or_none(source.get('views')),
            'age_limit': 18 if source.get('isMature') == 'true' or source.get('isSexy') == 'true' else 0,
            'formats': self._extract_formats(source),
        }
            
    def _real_extract(self, url):
        #header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')

        site_id = self._match_id(url)
        webpage = self._download_webpage(url, site_id)


     
        # TODO more code goes here, for example ...
        #title = self._og_search_title(webpage)
        #description = self._og_search_description(webpage)

        # example mp4 link
        # https://videos.tirerack.com/pdl/aa/73/aa732da5-5774-4abf-9d73-554121d0df29/03_Tire_Decision_Guide_30_800k.mp4
        #video_url = self._html_search_meta(r'https://videos.tirerack.com/pdl/.*')

        return {
            'id': video_id,
            'url': site_id,
            #'url': 'https://videos.tirerack.com/pdl/aa/73/aa732da5-5774-4abf-9d73-554121d0df29/03_Tire_Decision_Guide_30_800k.mp4',
            'title': 'title',
            'description': 'description',
            'header': {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            #'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }