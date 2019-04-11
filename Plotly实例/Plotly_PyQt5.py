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

    def get_plotly_path_if_hs300_bais(self,file_name='if_hs300_bais.html'):
        path_plotly=self.path_dir_plotly_html+os.sep+file_name
        df=pd.read_excel(r'if_index_bais.xlsx')

        '''绘制散点图'''
        line_main_price=go.Scatter(
            x=df.index,
            y=df['main_price'],
            name='main_price',
            connectgaps=True        #这个参数表示允许连接数据之间的缺失值
        )

        line_hs300_close=go.Scatter(
            x=df.index,
            y=df['hs300_close'],
            name='hs300_close',
            connectgaps=True
        )
        data=[line_hs300_close,line_main_price]

        layout=dict(
            title='if_hs300_bais',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Price')
        )

        fig=go.Figure(data=data,layout=layout)

        pyof.plot(fig,filename=path_plotly,auto_open=False)     #禁止浏览器自动打开

        # 绘图完成后绘图结果就保存在本地，通过函数返回保存的路径，然后QWebEngineView调用路径实现PyQt和Plotly的交互
        return path_plotly