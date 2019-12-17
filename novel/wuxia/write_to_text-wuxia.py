#!/usr/bin/env python3
import novel

down_param = {
    'done_down_text': 'wuxia-done.text',
    'down_url': "https://www.4455sk.com/xiaoshuo/list-武侠古典-%i.html",
    'start_page': 1,
    'end_page': 3,
    'select_str': "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a"
}
novel.write_to_text(down_param)
