#!/usr/bin/env python3
import novel

down_param = {
    'down_url': novel.down_url_luanlun,
    'start_page': 1,
    'end_page': 3,
    'select_str': "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a"
}
novel.write_to_text(down_param)
