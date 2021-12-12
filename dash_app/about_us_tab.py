from dash import dcc, html
from PIL import Image

hugh_summary = 'sdklfjaslkfjadslkfjasdl;kjflakdsj'
hugh_photo = Image.open('./data/image/hugh.jpg')

about_us_tab = dcc.Tab(label = 'About Us',
                    value='about_us',
                    children = [
                    html.H2("Team Information"),
                    html.H3("Hugh"),
                    html.Img(id = 'photo',
                        src = hugh_photo,
                        style = {'width': 300, 'height': 300}),
                    dcc.Textarea(id = 'bio',
                        value = hugh_summary,
                        style={'width': '100%'}),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com'),
                    html.H3("Charles"),
                    html.H3("Jung"),
                    html.H3("Robert"),
                        ])
