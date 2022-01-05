from dash import dcc, html
from blurbs.project_info_blurbs import project_blurb, data_blurb
from PIL import Image

cb_photo = Image.open('./data/image/pic1.jpg')
charles_photo = Image.open('./data/image/charles_bike.jpg')

intro_tab = dcc.Tab(label = 'Project Introduction',
                    value='intro',
                    children = [
                    html.H1('Project Description'),
                    html.Div(children = [
                                html.Div(project_blurb, style = {'width': '48vw','display':'inline-block'}),
                                html.Div(html.Img(id = 'pic1',
                            src = cb_photo,
                            style = {'width': '30vw', 'height': 'auto'}), style = {'vertical-align': 'top','width' : '48vw','display':'inline-block'})
                        ],
                            style = {}),
                    html.H1(),
                    html.H1('Data Description'),
                     html.Div(children = [
                                html.Div(data_blurb, style = {'width': '48vw','display':'inline-block'}),
                                html.Div(html.Img(id = 'pic2',
                            src = charles_photo,
                            style = {'width': '30vw', 'height': 'auto'}), style = {'vertical-align': 'top','width' : '48vw','display':'inline-block'})
                        ],
                            style = {})
                    
                    ])

