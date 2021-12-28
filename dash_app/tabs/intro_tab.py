from dash import dcc, html
from blurbs.project_info_blurbs import project_blurb, data_blurb
from PIL import Image

cb_photo = Image.open('./data/image/pic1.jpg')

intro_tab = dcc.Tab(label = 'Project Introduction',
                    value='intro',
                    children = [
                    html.H1('Project Description'),
                    html.Div(children = [
                                html.Div(project_blurb, style = {'width': '48vw'}),
                                html.Div('dummy', style = {'width' : '48vw'})
                        ],
                            style = {}),
                    html.H1(),
                    html.H1('Data Description'),
                     html.Div(children = [
                                html.Div(data_blurb, style = {'width': '48vw'}),
                                html.Div('dummy', style = {'width' : '48vw'})
                        ],
                            style = {}),
                    html.Img(id = 'pic1',
                            src = cb_photo,
                            style = {'width': 500, 'height': 'auto'})
                    ])

