#!/usr/bin/env python3
import novel

down_param = {
    'done_down_text': 'changpian-done.text',
    'down_url': "http://www.ve2s.com/AAbook/AAAtb/changpian/index-%i.html",
    'start_page': 1,
    'end_page': 3,
    'select_str': "body div[class='main'] div[class='classList'] ul li a"
}
novel.write_to_text(down_param)
