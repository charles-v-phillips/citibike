from dash import dcc, html
from project_info_blurbs import project_blurb, data_blurb
from PIL import Image

cb_photo = Image.open('./data/image/bob.jpg')

intro_tab = dcc.Tab(label = 'Project Introduction',
                    value='intro',
                    children = [
                    html.H1('Project Description'),
                    html.Div(project_blurb),
                    html.H1('Data Description'),
                    html.Div(data_blurb),
                    html.Img(id = 'pic1',
                            src = cb_photo,
                            style = {'width': 300, 'height': 'auto'})
                    ])
