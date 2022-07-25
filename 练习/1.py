#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
from pygal.style import *
people=data['人员'].unique()
label=data['月份'].unique()
radar_chart = pygal.Radar(style=LightStyle)
radar_chart.title = '520寝室2020年生活费花销情况'
radar_chart.x_labels = label
for i in people:
    radar_chart.add(i, data[data.人员==i]['花销'].values.tolist())
HTML(base_html.format(rendered_chart=radar_chart.render(is_unicode=True)))#图片渲染