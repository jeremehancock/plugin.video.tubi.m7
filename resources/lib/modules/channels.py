"""
    Tubi Add-on Add-on
    Developed by mhancoc7

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    # Python 3
    from resources.lib.modules.common import *
except ImportError:
    # Python 2
    from common import *

import m7lib

class Channels:

    @staticmethod
    def section_list():
        icon = ""
        try:
            section_list = m7lib.Stream.get_tubi_tv_categories()
            for category in section_list:
                if category["icon"] == "none":
                    icon = icon
                else:
                    icon = category["icon"]
                m7lib.Common.add_section(category["id"] + "tubitv-content", icon, fanart, category["title"])
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def content_list(mode):
        try:
            category = mode.split('tubitv-content')[0]
            content_list = m7lib.Stream.get_tubi_tv_content(category)
            for entry in content_list:
                if entry["type"] == "v":
                    m7lib.Common.add_channel(entry["id"] + "play-tubitv", entry["icon"], fanart, entry["title"],
                                             live=False)

                elif entry["type"] == "s":
                    m7lib.Common.add_section(entry["id"] + "tubitv-episodes", entry["icon"], fanart, entry["title"])
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def episode_list(mode):
        try:
            show = mode.split('tubitv-episodes')[0]
            episode_list = m7lib.Stream.get_tubi_tv_episodes(show)
            for entry in episode_list:
                m7lib.Common.add_channel(entry["id"] + "play-tubitv", entry["icon"], fanart, entry["title"], live=False)
        except StandardError:
            dlg_oops(addon_name)

    @staticmethod
    def play_tubi(mode):
        try:
            stream_id = mode.split('play-tubitv')[0]
            stream = m7lib.Stream.get_tubi_tv_stream(stream_id)
            m7lib.Common.play(stream)
        except StandardError:
            dlg_oops(addon_name)