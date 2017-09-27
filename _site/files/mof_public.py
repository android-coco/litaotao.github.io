# -*- coding: utf-8 -*-

import json
import copy
import time
import requests
import pprint
import datetime as dt

import charts
import IPython

import pandas as pd
import numpy as np
import scipy as sp

options = {
    'xAxis': {
        'type': 'datetime',
    },
    'title': {'text': 'title'},
    'subtitle': {'text': ''},
    'line': {
            'dataLabels': {
                'enabled': True
            },
            'color': 'red',
            'lineWidth': 8
        },
    'column': {
            'dataLabels': {
                'enabled': True
            },
        },
    'series': {
            'dataLabels': {
                'enabled': True,
                },
            "color": 'red',
            },
    'tooltip': {'crosshairs': [True], 'shared': True, 'valueDecimals': 4},
    'chart': {'zoomType': 'xy'},
    "height": 400, 
    "width": "auto",
}


template_2_div = """
<div>
 <div style="width:50%; height:400px; float:left; text-align:-webkit-center; overflow: scroll">{}</div>
 <div style="width:50%; height:400px; float:left; text-align:-webkit-center; overflow: scroll">{}</div>
 <div style="clear:both;"></div>
</div>
"""

def print_progressbar(progress, initial_bar=False, barid='myBar'):
    """打印进度条
    progress 代表进度，值为 0 ～ 100
    """
    if initial_bar:
        print_html("""
         <div id="myProgress">
           <div id="%s" class='barbar'></div>
         </div>
        """ % barid)
    else:
        print_html("""
                <script id="fuck">

                var elem = document.getElementById("{}"); 
                elem.style.width = {} + '%'; 
                elem.innerHTML = {};

                document.getElementById('fuck').parentElement.parentElement.remove();
                
                </script>
                """.format(barid, progress, progress))


def print_html(html_text):
    """将 charts 图表的 html 数据手动展现，一般适用于循环作图的场景
    """
    IPython.core.display.publish_display_data({'text/html': html_text})


def print_text(text, color='gray'):
    print_html(u"""<h1 style='color: {};text-align: center'>{}</h1>""".format(color, text))


def print_table(df):
    """将 dataframe 输出为 html 的表格形式，在 notebook 中适用
    """
    IPython.core.display.publish_display_data({'text/html': df.to_html()})    


def draw_figure(figure1, figure2):
    html = template_2_div.format(figure1.data, figure2.data)
    print_html(html)
    

def draw(df, x, y, title=None, **kwargs):
    my_options = copy.deepcopy(options)

    title = title if title else str(y)
    my_options['title']['text'] = title
    tmp = df[[x] + y]

    x_type = kwargs.pop('x_type') if 'x_type' in kwargs else 'datetime'
    x_labels = kwargs.pop('x_labels') if 'x_labels' in kwargs else None
    subtitle = kwargs.pop('subtitle') if 'subtitle' in kwargs else ''
     
    if x_type == 'datetime':
        tmp.set_index(x, inplace=True)
        tmp.index = tmp.index.to_datetime()
    else:
        my_options['xAxis']['type'] = x_type
        my_options['xAxis']['categories'] = df[x].tolist()

    if x_labels:
        my_options['xAxis']['categories'] = x_labels

    if 'options' in kwargs:
        my_options.update(kwargs.get('options'))
        kwargs.pop('options')

    if 'width' in kwargs:
        my_options['width'] = kwargs.get('width')

    if 'height' in kwargs:
        my_options['height'] = kwargs.get('height')

    if subtitle:
        my_options['subtitle']['text'] = subtitle

    if 'just_draw' not in kwargs:
        return charts.plot(tmp, options=my_options, show='inline', display=y, **kwargs)
    else:
        kwargs.pop('just_draw')
        figure = charts.plot(tmp, options=my_options, show='inline', display=y, **kwargs)
        print_html(figure.data)
