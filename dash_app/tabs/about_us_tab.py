from dash import dcc, html
from PIL import Image

hugh_summary = 'Hugh is a Data Scientist with a BS in Civil Engineering from the The College of New Jersey and an MS in Engineering Management from Duke University. After 5 years as an engineer, he pivoted to pursue Data Science and Analytics. He has a passion for extracting business value from data.'
charles_summary = 'Charles has a BS in Mathematics with a minor in Computer Science from Stony Brook University. He is an aspiring Data Scientist'
jung_summary = 'Jung is an apiring data scientist with a BE in Mechanical Engineering from The Cooper Union. In his free time he likes to play basketball.'
robert_summary = 'Robert is an aspiring Data Scientist with a BS in Chemistry and Mathematics from Binghamton University and a PhD in Computational Chemistry from Stanford University. He pivoted from academia to Data Science with a focus on problem-solving, analytics, and machine learning for technology companies.'

hugh_photo = Image.open('./data/image/hugh.jpg')
charles_photo = Image.open('./data/image/charles.jpg')
jung_photo = Image.open('./data/image/jung.jpg')
robert_photo = Image.open('./data/image/robert.jpg')

about_us_tab = dcc.Tab(label = 'About Us',
                    value='about_us',
                    children = [
                    html.H2("Team Information"),

                    html.Div(children = [
                        html.Div(children = [
                        html.H3("Hugh"),
                        html.Img(id = 'hg_photo',
                            src = hugh_photo,
                            style = {'width': 300, 'height': 450}),
                        html.Div(hugh_summary, style = {'font-size': '1vw'}),
                        html.A("LinkedIn",
                            href = 'https://www.linkedin.com/in/hugh-goode-2a243946/')],
                            style={'width': '50%', 'display': 'inline-block','vertical-align': 'top'}),

                        html.Div(children = [
                        html.H3("Charles"),
                        html.Img(id = 'cp_photo',
                            src = charles_photo,
                            style = {'width': 300, 'height': 450}),
                        html.Div(charles_summary, style = {'font-size': '1vw'}),
                        html.A("LinkedIn",
                            href = 'https://www.linkedin.com/in/charles-v-phillips/')],
                            style={'width': '50%', 'display': 'inline-block','vertical-align': 'top'})]),

                    html.Div(children = [
                        html.Div(children = [
                        html.H3("Jung"),
                        html.Img(id = 'jl_photo',
                            src = jung_photo,
                            style = {'width': 'auto', 'height': 450}),
                        html.Div(jung_summary, style = {'font-size': '1vw'}),
                        html.A("LinkedIn",
                            href = 'https://www.linkedin.com/in/jung-lim-a9a348135/')],
                            style={'width': '50%', 'display': 'inline-block','vertical-align': 'top'}),

                        html.Div(children = [
                        html.H3("Robert"),
                        html.Img(id = 'bob_photo',
                            src = robert_photo,
                            style = {'width': 300, 'height': 450}),
                        html.Div(robert_summary, style = {'font-size': '1vw'}),
                        html.A("LinkedIn",
                            href = 'https://www.linkedin.com/in/robertsandberg1/')],
                            style={'width': '50%', 'display': 'inline-block','vertical-align': 'top'})]),
                            ])
