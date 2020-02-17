#!/usr/bin/env python3
import novel

down_param = {
    # 'done_down_text': 'changpian-done.text',
    'down_url': novel.down_url_changpian,
    'start_page': 1,
    'end_page': 3,
    'select_str': "body div[class='main'] div[class='classList'] ul li a"
}
novel.write_to_text(down_param)
