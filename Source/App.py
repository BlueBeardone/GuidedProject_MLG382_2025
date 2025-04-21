import dash 
from dash import dcc, html, Input, Output
import pandas as pd
import joblib

#Import model when complete
model = joblib.load("import model here")

app = dash.Dash(__name__)

# Define Website layout in html
app.layout = html.Div([
    html.H1("BrightPath Academy: Student Performance Predictor",
    style={'textAlign': 'center',
            'color': '#2c3e50',
            'fontFamily': 'Arial',
            'padding': '20px',
            'backgroundColor': 'Green'}),
        
    html.Div([
        html.Label("Weekly Study Time (hours)", style={'margin': '10px', 'fontWeight': 'bold'}),
        dcc.Input(id='study_time', type='number', value=5, style={'margin': '10px', 'padding': '5px'}),
        
        html.Label("Number of Absences"),
        dcc.Input(id='absences', type='number', value=2),

        html.Label("Recieving Tutoring"),
        dcc.Input(id='TutoringYes', type='radio', value="YES"),
        
        html.Label("Parental Support (0-4)"),
        dcc.Input(id='parental_support', type='number', value=3),
        
        html.Button('Predict', id='predict-button'),
    ],
    style={
            'width': '50%',
            'margin': 'auto',
            'padding': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '10px',
            'backgroundColor': 'white'
        }),
    
    html.Div(id='prediction-output', style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '20px'})
], style={'backgroundColor': 'Green', 'minHeight': '100vh'})

#Checks for change on predict btn then grabs inputs and does function and outputs in prediction-outputs as children
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    [Input('study_time', 'value'),
     Input('absences', 'value'),
     Input('TutoringYes', 'value'),
     Input('TutoringNo', 'value'),
     Input('parental_support', 'value')]
)
def predict(n_clicks, study_time, absences, TutoringYes, parental_support):
    if n_clicks:
        tutoring = 0
        if TutoringYes == "yes":
            tutoring = 1
        # Create input DataFrame for model
        input_data = pd.DataFrame([[study_time, absences, tutoring, parental_support]],
                                  columns=['StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport'])
        
        # Predicting GradeClass 
        prediction = model.predict(input_data)[0]
        grades = ['A', 'B', 'C', 'D', 'F']
        
        return html.H3(f"Predicted Grade: {grades[prediction]}")
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)



