import pandas as pd
import os
import plotly.offline as pyof               #使用的离线绘图模式，速度比较快
import plotly.graph_objs as go

import numpy as np
import matplotlib.pyplot as plt

class Plotly_PyQt5():

    def __init__(self):
        '''初始化时设置存储HTML文件的文件夹名称，默认为plotly_html'''
        plotly_dir='plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)

        self.path_dir_plotly_html=os.getcwd()+os.sep+plotly_dir

    def get_plotly_path(self,file_name='map.html'):
        path_plotly=self.path_dir_plotly_html+os.sep+file_name

        '''绘制散点图'''
        data = [
            go.Scattermapbox(
                #纬度
                lat=['30.57267', '29.56753', '26.65066',
                     '24.88271', '30.59517', '28.23129',
                     '28.68535', '22.81941', '23.13175',],
                #经度
                lon=['104.06227', '106.54698', '106.62664',
                     '102.83178', '114.29980', '112.93342',
                     '115.85304', '108.36282', '113.25902'],
                mode='markers+text',            #marker是点加上text表示不悬停的情况下也出现text
                marker=go.scattermapbox.Marker(
                    size=10,
                    symbol="circle",            #没太看懂，只会用circle
                    color='#ff5500'
                ),
                text=["成都", "重庆", "贵阳",
                      "昆明", "武汉", "长沙",
                      "南昌", "南宁", "广州"],
                textfont=dict(
                    family='Microsoft YaHei',
                    size=13,
                ),

            )
        ]

        layout = go.Layout(
            autosize=True,
            hovermode='closest',
            mapbox=go.layout.Mapbox(
                accesstoken='pk.eyJ1IjoiaGVubmVzc3ktemhhbyIsImEiOiJjanVjMjVrODUwN3Q3NDNxcDZpcGgzNHY4In0.lXpVP9PXHWo7LYoq4xBbuQ',
                bearing=0,          #以北为单位逆时针设置地图的方位角
                center=go.layout.mapbox.Center(
                    lat=26.65066,
                    lon=106.62664
                ),
                pitch=0,            #设置地图的俯仰角度（以度为单位，其中“0”表示垂直于地图表面）
                zoom=3.5           #设置地图的缩放级别
            ),
            hoverlabel=dict(
                bgcolor='#ffffff',
                bordercolor='#dcdcdc',
                font=dict(
                    family='Microsoft YaHei',
                    size=13,
                    color='#777'
                )
            ),
            title=dict(
                text='地图',
                font=dict(
                    family='Microsoft YaHei',
                    size=13,
                    color='#777'
                )
            )
        )

        fig=go.Figure(data=data,layout=layout)

        pyof.plot(fig,filename=path_plotly,auto_open=False)     #禁止浏览器自动打开

        # 绘图完成后绘图结果就保存在本地，通过函数返回保存的路径，然后QWebEngineView调用路径实现PyQt和Plotly的交互
        return path_plotly