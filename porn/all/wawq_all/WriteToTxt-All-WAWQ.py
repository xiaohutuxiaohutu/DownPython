#!/usr/bin/env python3

import porn

down_param = {
    'done_down_text': 'Down-Done-WAWQ.text',
    'down_url': 'forumdisplay.php?fid=21&orderby=dateline&filter=2592000&page=%i',
    'start_page': 1,
    'end_page': 5
}
porn.write_to_text_exclude_jh(down_param)
