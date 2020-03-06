# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Going to visit Paris?
            
            #### Congratulations!!
            
            This price estimator will help you find the place to stay in Paris.
            Depending on your preferences of location, type of rent, and how long you stay there,
            this app may help you determine the budget for the trip.  

           

            """
        ),
         dcc.Link(dbc.Button('Predict the price', color='primary'), href='/predictions')
     ],
     md=4,
 )

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
#)

column2 = dbc.Col(
    [
        html.Div(html.Img(src='assets/paris.jpg'))
    ]
)
    
layout = dbc.Row([column1, column2])