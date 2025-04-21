from dash import Dash, dcc, html, Input, Output
import pandas as pd
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'linearregression.pkl')
model = joblib.load(model_path)

app = Dash(__name__)
server = app.server

# Define layout
app.layout = html.Div([
    html.H1(
        "BrightPath Academy: Student Performance Predictor",
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'fontFamily': 'Arial',
            'padding': '20px',
            'backgroundColor': 'Green'
        }
    ),
    
    html.Div(
        [
            # Study Time Input
            html.Div(
                [
                    html.Label("Weekly Study Time (hours)", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Input(id='study_time', type='number', value=5, style={'width': '100%', 'padding': '8px'})
                ],
                style={'marginBottom': '15px'}
            ),
            
            # Absences Input
            html.Div(
                [
                    html.Label("Number of Absences", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Input(id='absences', type='number', value=2, style={'width': '100%', 'padding': '8px'})
                ],
                style={'marginBottom': '15px'}
            ),
            
            # Tutoring Radio choice
            html.Div(
                [
                    html.Label("Receiving Tutoring", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.RadioItems(
                        id='tutoring',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        value=1,
                        inline=True,
                        style={'marginTop': '5px'}
                    )
                ],
                style={'marginBottom': '15px'}
            ),
            
            # Parental Support Input
            html.Div(
                [
                    html.Label("Parental Support (0-4)", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                    dcc.Input(id='parental_support', type='number', value=3, style={'width': '100%', 'padding': '8px'})
                ],
                style={'marginBottom': '15px'}
            ),
            
            # Predict Button
            html.Div(
                html.Button('Predict', id='predict-button', style={'width': '100%', 'padding': '10px', 'backgroundColor': '#4CAF50', 'color': 'white', 'border': 'none', 'cursor': 'pointer'}),
                style={'marginTop': '20px'}
            )
        ],
        style={
            'width': '50%',
            'margin': 'auto',
            'padding': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '10px',
            'backgroundColor': 'white'
        }
    ),
    
    # Prediction Output
    html.Div(
        id='prediction-output',
        style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '20px'}
    )
], style={'backgroundColor': 'Green', 'minHeight': '100vh'})

# Callback (keep your existing callback logic)
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    [Input('study_time', 'value'),
     Input('absences', 'value'),
     Input('tutoring', 'value'),
     Input('parental_support', 'value')]
)
def predict(n_clicks, study_time, absences, tutoring, parental_support):
    if n_clicks:
        input_data = pd.DataFrame([[study_time, absences, tutoring, parental_support]],
                                  columns=['StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport'])
        prediction = model.predict(input_data)[0]
        grades = ['A', 'B', 'C', 'D', 'F']
        return html.H3(f"Predicted Grade: {grades[prediction]}")
    return ""

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)