# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np




# Imports from this application
from app import app


import pickle

pipeline = pickle.load(open('assets/last_model.sav', 'rb'))

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
     [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Latitude'), 
        dcc.Slider(
            id = 'latitude',
            min=48.816990,
            max=48.900790,
            step=0.001,
            value=48.816990,
            marks = {48.816990: '48.816990', 48.900790: '48.900790'},
            className = 'mb-1' 
), 
         
        dcc.Markdown('', id = 'out1'),
         
        dcc.Markdown('#### Longitude'),
        dcc.Slider(
            id = 'longitude',
            min=2.247990,
            max=2.427590,
            step=0.001,
            value=2.247990,
            marks = {2.247990: '2.247990', 2.427590: '2.427590'}, 
            className = 'mb-1'
),
        dcc.Markdown('', id = 'out2'),
         
        dcc.Markdown('#### Nights'), 
        dcc.Dropdown(
            id='minimum_nights', 
            options = [
                {'label': '1', 'value' : '1'}, {'label': '2', 'value' : '2'}, {'label': '3', 'value' : '3'},                    
                {'label': '4', 'value' : '4'}, {'label': '5', 'value' : '5'}, {'label': '6', 'value' : '6'},                      
                {'label': '7', 'value' : '7'}, {'label': '8', 'value' : '8'}, {'label': '9', 'value' : '9'},
                {'label': '10', 'value' : '10'}, {'label': '11', 'value' : '11'}, {'label': '12', 'value' : '12'},
                {'label': '13', 'value' : '13'}, {'label': '14', 'value' : '14'}, {'label': '15', 'value' : '15'},
                {'label': '16', 'value' : '16'}, {'label': '17', 'value' : '17'}, {'label': '18', 'value' : '18'},
                {'label': '19', 'value' : '19'}, {'label': '20', 'value' : '20'}, {'label': '21', 'value' : '21'},
                {'label': '22', 'value' : '22'}, {'label': '23', 'value' : '23'}, {'label': '24', 'value' : '24'},
                {'label': '25', 'value' : '25'}, {'label': '26', 'value' : '26'}, {'label': '27', 'value' : '27'},
                {'label': '28', 'value' : '28'}, {'label': '29', 'value' : '29'}, {'label': '30', 'value' : '30'},
            ], 
            value = '1', 
            className='mb-5', 
     
        ), 
         dcc.Markdown('#### Rent Type'), 
        dcc.Dropdown(
            id='room_type', 
            options = [
                {'label': 'Entire home/apt', 'value' : 'Entire home/apt'},
                {'label': 'Private room', 'value' : 'Private room'}, 
                {'label': 'Hotel room', 'value' : 'Hotel room'},                    
                {'label': 'Shared room', 'value' : 'Shared room'},
            ], 
            value = 'Private room', 
            className='mb-5', 
     
        ), 
         
        dcc.Markdown('#### Neighbourhood'), 
        dcc.Dropdown(
            id='neighbourhood', 
            options = [
                {'label': 'Buttes-Montmartre', 'value': 'Buttes-Montmartre'}, {'label': 'Popincourt', 'value': 'Popincourt'}, 
                {'label': 'Entrepôt', 'value': 'Entrepôt'},{'label': 'Vaugirard', 'value': 'Vaugirard'}, 
                {'label': 'Batignolles-Monceau', 'value': 'Batignolles-Monceau'}, {'label': 'Ménilmontant', 'value': 'Ménilmontant'}, 
                {'label': 'Temple', 'value': 'Temple'}, {'label': 'Buttes-Chaumont', 'value': 'Buttes-Chaumont'}, 
                {'label': 'Opéra', 'value': 'Opéra'}, {'label': 'Passy', 'value': 'Passy'},
                {'label': 'Bourse', 'value': 'Bourse'}, {'label': 'Reuilly', 'value': 'Reuilly'},
                {'label': 'Observatoire', 'value': 'Observatoire'}, {'label': 'Panthéon', 'value': 'Panthéon'},
                {'label': 'OHôtel-de-Ville', 'value': 'Hôtel-de-Ville'}, {'label': 'Luxembourg', 'value': 'Luxembourg'},
                {'label': 'Gobelins', 'value': 'Gobelins'}, {'label': 'Palais-Bourbon', 'value': 'Palais-Bourbon'},
                {'label': 'Élysée', 'value': 'Élysée'}, {'label': 'Louvre', 'value': 'Louvre'},
            ], 
            value = 'Louvre', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [      
        html.H2('Estimated rent in Paris: ', className='mb-5'), 
        html.Div(id='prediction-content', className='lead', style={'fontSize': 40}), 
        
    ]
)


layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('neighbourhood', 'value'),
     Input('latitude', 'value'),
     Input('longitude', 'value'),
     Input('room_type', 'value'),
     Input('minimum_nights', 'value')],
)
def predict( neighbourhood, latitude, longitude, room_type, minimum_nights):
    df = pd.DataFrame(
        data=[[neighbourhood, latitude, longitude, room_type, minimum_nights]], 
        columns=['neighbourhood', 'latitude', 'longitude','room_type', 'minimum_nights']
    )
    y_pred = pipeline.predict(df)[0]
    price_pred = np.expm1(y_pred)
    return f'{price_pred:.0f} $'
