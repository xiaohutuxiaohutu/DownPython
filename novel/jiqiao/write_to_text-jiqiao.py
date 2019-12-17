import novel

down_param = {
    'done_down_text': 'jiqiao-done.text',
    'down_url': "https://www.4455sk.com/xiaoshuo/list-性爱技巧-%i.html",
    'start_page': 1,
    'end_page': 3,
    'select_str': "body div[class='maomi-content'] main[id='main-container'] div[class='text-list-html'] div ul li a"
}
novel.write_to_text(down_param)
