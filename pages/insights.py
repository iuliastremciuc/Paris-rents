# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            The Permutation Importances, shown below, explains how important every feature is for predicting price.
            The biggest influence on this prediction model is made by the 'longitude', 'latitude', and 'room_type' features.
            """
        ),
         
        dcc.Markdown('Permutation Importances'),
        html.Div(html.Img(src='assets/PermutationImportances.png', style={'display': 'inline-block'})),
            
        dcc.Markdown(
            """
            
            The next Graph is a Partial Dependence Plot, which shows the interaction of the two most important features of the data. 
            Lighter color indicates probability of higher price according to the predictive model.
            
            """
        ),
        
        dcc.Markdown('PDP Interaction'),
        html.Div(html.Img(src='assets/PDPinteraction.png', style={'display': 'inline-block'})),
        
             
        dcc.Markdown(
            """
            
            
            As observed in the graphs below, two of the most important features that affect rental price are location and room/privacy type.
            The better the neighbourhood the higher the price. Similarly, a whole home/apt rental drives the price up compared to single 
            room rental.
           
            
            

            """
        ),
        dcc.Markdown('Shaply Example(a)'),
        html.Div(html.Img(src='assets/Shapley1.png', style={'display': 'inline-block'})),
        
        dcc.Markdown('Shaply Example(b)'),
        html.Div(html.Img(src='assets/Shapley2.png', style={'display': 'inline-block'})),


    ],
)
# column2 = dbc.Col(
#     [
#          dcc.Markdown('Permutation Importances'),
#          html.Div(html.Img(src='assets/PermutationImportances.png', style={'display': 'inline-block'})),
         
        
#          dcc.Markdown('PDP Interaction'),
#          html.Div(html.Img(src='assets/PDPinteraction.png', style={'display': 'inline-block'})),
#     ],
# )


layout = dbc.Row([column1])