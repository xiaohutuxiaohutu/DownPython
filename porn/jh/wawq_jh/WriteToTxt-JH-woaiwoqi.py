#!/usr/bin/env python3
import porn

down_param = {
    'done_down_text': 'DoneDown-JH-WAWQ.text',
    'down_url': 'forumdisplay.php?fid=21&orderby=dateline&filter=digest&page=%i',
    'start_page': 1,
    'end_page': 2
}
porn.write_to_text_include_jh(down_param)
