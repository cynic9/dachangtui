import requests
from urllib.parse import urlencode


def get_url(offset):
    parmaters = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '大长腿',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1568963540959',
        'has_video': 'False'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
        'cookie': 'csrftoken=0bfbe4650322a3253c0543825cd01759; tt_webid=6737963992306615812; tt_webid=6737963992306615812; WEATHER_CITY=%E5%8C%97%E4%BA%AC; s_v_web_id=b823f94daa3d40eed1c7c6e1d3f4a8eb; __tasessionId=l4fpipgeg1568975444082',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E5%A4%A7%E9%95%BF%E8%85%BF'
    }
    # 输入大长腿，可以看到头条的请求地址 以及请求后缀，再通过url解码拼接地址
    url = 'https://www.toutiao.com/api/search/content/?'+urlencode(parmaters)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print('下载失败')
    except Exception as e:
        print(e)
