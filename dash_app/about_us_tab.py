from dash import dcc, html
from PIL import Image

hugh_summary = 'Hugh is a Data Scientist with a BS in Civil Engineering from the The College of New Jersey and an MS in Engineering Management from Duke University. After 5 years as an engineer, he pivoted to pursue Data Science and Analytics. He has a passion for extracting business value from data.'
charles_summary = 'fkldsjfkldsjf'
jung_summary = 'dkfjdsklfjdlskf'
robert_summary = 'dslfdskfjdsfkljd'

hugh_photo = Image.open('./data/image/hugh.jpg')
#charles_photo = Image.open('./data/image/charles.jpg')
#jung_photo = Image.open('./data/image/jung.jpg')
#robert_photo = Image.open('./data/image/robert.jpg')

about_us_tab = dcc.Tab(label = 'About Us',
                    value='about_us',
                    children = [
                    html.H2("Team Information"),
                    html.H3("Hugh"),
                    html.Img(id = 'photo',
                        src = hugh_photo,
                        style = {'width': 300, 'height': 400}),
                    html.Div(hugh_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/hugh-goode-2a243946/'),
                    html.H3("Charles"),
                    html.Div(charles_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/charles-v-phillips/'),
                    html.H3("Jung"),
                    html.Div(jung_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/jung-lim-a9a348135/'),
                    html.H3("Robert"),
                    html.Div(robert_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/robertsandberg1/'),
                        ])
