from dash import dcc, html
from PIL import Image

hugh_summary = 'Hugh is a Data Scientist with a BS in Civil Engineering from the The College of New Jersey and an MS in Engineering Management from Duke University. After 5 years as an engineer, he pivoted to pursue Data Science and Analytics. He has a passion for extracting business value from data.'
charles_summary = 'Charles has a BS in Mathematics with a minor in Computer Science from Stony Brook University. He is an aspiring Data Scientist'
jung_summary = 'BE in Mechanical Engineering from Cooper Union. He is currently pursuing Data Science.'
robert_summary = 'Robert is an aspiring Data Scientist with a BS in Chemistry and Mathematics from Binghamton University and a PhD in Computational Chemistry from Stanford University. He pivoted from academia to Data Science with a focus on problem-solving, analytics, and machine learning for technology companies.'

hugh_photo = Image.open('./data/image/hugh.jpg')
charles_photo = Image.open('./data/image/charles.jpg')
jung_photo = Image.open('./data/image/jian_yang.jpg')
robert_photo = Image.open('./data/image/bob.jpg')

about_us_tab = dcc.Tab(label = 'About Us',
                    value='about_us',
                    children = [
                    html.H2("Team Information"),
                    html.H3("Hugh U Good?"),
                    html.Img(id = 'hg_photo',
                        src = hugh_photo,
                        style = {'width': 300, 'height': 450}),
                    html.Div(hugh_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/hugh-goode-2a243946/'),
                    html.H3("Charlie"),
                    html.Img(id = 'cp_photo',
                        src = charles_photo,
                        style = {'width': 300, 'height': 450}),
                    html.Div(charles_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/charles-v-phillips/'),
                    html.H3("Real ass *****"),
                    html.Img(id = 'jl_photo',
                        src = jung_photo,
                        style = {'width': 500, 'height': 300}),
                    html.Div(jung_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/jung-lim-a9a348135/'),
                    html.H3("Mr. Bob"),
                    html.Img(id = 'bob_photo',
                        src = robert_photo,
                        style = {'width': 300, 'height': 400}),
                    html.Div(robert_summary),
                    html.A("LinkedIn",
                        href = 'https://www.linkedin.com/in/robertsandberg1/'),
                        ])
