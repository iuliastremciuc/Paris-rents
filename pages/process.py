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
        
            ## Process
            
            ### Sourcing the data
           
            Airbnb is a market leader in rentals which is why for this project I used [Inside Airbnb]
            (http://insideairbnb.com/get-the-data.html) where I found rental data 
            wich contains information about rents in Paris. 
            
            ### Cleaning the data
           
            Dataset listings.csv had 16 columns and 65493 rows. In order to avoid using outdated rental price information I reduced the
            dataset to exclude rents prior to 2019. I dropped the most extreme outliers and irrelevant columns, such as 'id' and 
            'host_name', as well as columns with no values. This narrowed the dataset to 7 columns  and 37349 rows. 
            
            ### Modeling the data
            After I did train/val/test split I chose my target. I decided to predict rent prices.
            I used seaborn to plot 'price' column to see the distribution of values, which showed that I have a right 
            skewed graph. I used log transform to produce smaller values to make it easier for my model.
            
              """
        ),
        dbc.Row([
            dbc.Col([
                dcc.Markdown('Original distribution'),
                html.Div(html.Img(src='assets/price.png', style={'display': 'inline-block'})),
                    ], md = 3
                   ),
            dbc.Col(md = 3), 
            dbc.Col([
                dcc.Markdown('Transformed distribution'),
                html.Div(html.Img(src='assets/log_price.png', style={'display': 'inline-block'})),
                    ], md = 3
                 )]),
        
         dcc.Markdown(
             """
             As my baseline I used Mean Absolute Error (MAE) of my dependent variable which was ~$62.  After I transformed my target values 
             I used linear regression model and beat my baseline: MAE ~$46, score ~0.25. 
             Next using RandomForestRegressor I beat my baseline and my linear model, I decresed my MAE to ~$44.6 and r2_score 0.28. 
             Before I settled on RandomForestRegressor I tried the DecisionTreeRegressor and XGBRegressor but MAE was worst
             then my final model.
         
         """
         ),
    ],
)

# # column2 = dbc.Col(
# #     [
# #         dcc.Markdown('Original distribution'),
# #         html.Div(html.Img(src='assets/price.png', style={'display': 'inline-block'})),
        
# #         dcc.Markdown('Transformed distribution'),
# #         html.Div(html.Img(src='assets/log_price.png', style={'display': 'inline-block'})
# #                 ),
#     ],
# )
       
        
        

layout = dbc.Row([column1])