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
           
            Airbnb is a market leader in rentals that's why for this project I used [Inside Airbnb]
            (http://insideairbnb.com/get-the-data.html) where I found **file** 
            wich contains information about rents in Paris. 
            
            ### Cleaning the data
           
            Dataset `listings.csv` has 16 columns and 65493 rows. I decided to use latest listings for better accuracy, 
            so I created subset where only data for 2019 was kept. I dropped most extreme outliers and irrelevant columns and 
            columns with sagnificant amount of Missing value, which left me with 7 columns 37349 rows. 
            
            ### Modeling the data
            After I did train/val/test split I choose my target. I decided to predict rent prices.
            I use seaborn to plot 'price' column to see the destribution of values, which showed that I have right 
            skewed graph. I used log transform to produce smaller values to make it easier for my model.
            
              """
        ),
#         dcc.Markdown('Original distribution'),
#         html.Div(html.Img(src='assets/price.png', style={'display': 'inline-block'})),
        
#         dcc.Markdown('Transformed distribution'),
#         html.Div(html.Img(src='assets/log_price.png', style={'display': 'inline-block'})),
        
         dcc.Markdown(
             """
             As my baseline I used mean of my dependend variable which was ~ 118.7 $.  After I transformed my target values 
             I used linear regression model and beat my baseline :  mae ~ 46 $ , score ~ 0.25.  Next using RandomForestRegressor
             I beat my baseline and my linear model, I decresed my mae to ~ 44.6 $ and r2_score 0.28. 
         
         """
         ),

    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown('Original distribution'),
        html.Div(html.Img(src='assets/price.png', style={'display': 'inline-block'})),
        
        dcc.Markdown('Transformed distribution'),
        html.Div(html.Img(src='assets/log_price.png', style={'display': 'inline-block'})
                ),
    ],
)
       
        
        

layout = dbc.Row([column1, column2])