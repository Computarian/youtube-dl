# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class TireRackIE(InfoExtractor):
    #_VALID_URL = r'https?://(?:www\.)?tirerack\.com/watch/(?P<id>[0-9]+)'
    #_VALID_URL = r'https?://(?:www\.)?tirerack\.com/videos/(?P<id>[0-9]+)'
    _VALID_URL = r'https?://(?:www\.)?videos\.?tirerack\.com/.*'


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

    def _real_extract(self, url):
        video_id = self._generic_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)

        # example mp4 link
        # https://videos.tirerack.com/pdl/aa/73/aa732da5-5774-4abf-9d73-554121d0df29/03_Tire_Decision_Guide_30_800k.mp4
        video_url = self._html_search_meta(r'https://videos.tirerack.com/pdl/.*')

        return {
            'id': video_id,
            'url': video_url,
            'title': title,
            'description': description,
            #'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }