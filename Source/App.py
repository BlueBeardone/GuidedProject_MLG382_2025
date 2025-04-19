import dash
from dash import dcc, html, Input, Output
import pandas as pd
import joblib

#Import model when complete
model = joblib.load()

app = dash.Dash(__name__)

# Define Website layout in html
app.layout = html.Div([
    html.H1("BrightPath Academy: Student Performance Predictor"),
    html.Div([
        html.Label("Weekly Study Time (hours)"),
        dcc.Input(id='study_time', type='number', value=5),
        
        html.Label("Number of Absences"),
        dcc.Input(id='absences', type='number', value=2),
        
        html.Label("Parental Support (0-4)"),
        dcc.Input(id='parental_support', type='number', value=3),
        
        html.Button('Predict', id='predict-button'),
    ]),
    html.Div(id='prediction-output')
])



