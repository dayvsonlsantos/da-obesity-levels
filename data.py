# pip install matplotlib seaborn scikit-learn dash pandas numpy

# Imports
import pandas as pd
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# Read dataset
obesityDataSet = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv', sep=',')

# Filter dataset for specific obesity types
obesityTypeDataSet = obesityDataSet.loc[
    (obesityDataSet['NObeyesdad'] != 'Normal_Weight') &
    (obesityDataSet['NObeyesdad'] != 'Overweight_Level_I') &
    (obesityDataSet['NObeyesdad'] != 'Overweight_Level_II') &
    (obesityDataSet['NObeyesdad'] != 'Overweight_Level_III') &
    (obesityDataSet['NObeyesdad'] != 'Insufficient_Weight')
]

# Calculate BMI
obesityTypeDataSet['imc'] = obesityTypeDataSet['Weight'] / (obesityTypeDataSet['Height'] ** 2)

# Convert Age to integer
obesityTypeDataSet['Age'] = obesityTypeDataSet['Age'].astype(int)

# Filter for Obesity_Type_I
obesityLevel_I = obesityTypeDataSet.loc[obesityTypeDataSet['NObeyesdad'] == 'Obesity_Type_I']

# Calculate mean age for Obesity_Type_I by gender
mean_age_male_Obesity_I = obesityLevel_I.loc[obesityLevel_I['Gender'] == 'Male', 'Age'].mean().astype(int)
mean_age_female_Obesity_I = obesityLevel_I.loc[obesityLevel_I['Gender'] == 'Female', 'Age'].mean().astype(int)

print("Média de idade entre homens em Obesity_Type_I:", mean_age_male_Obesity_I)
print("Média de idade entre mulheres em Obesity_Type_I:", mean_age_female_Obesity_I)

# Filter for Obesity_Type_II
obesityLevel_II = obesityTypeDataSet.loc[obesityTypeDataSet['NObeyesdad'] == 'Obesity_Type_II']

# Calculate mean age for Obesity_Type_II by gender
mean_age_male_Obesity_II = obesityLevel_II.loc[obesityLevel_II['Gender'] == 'Male', 'Age'].mean().astype(int)
mean_age_female_Obesity_II = obesityLevel_II.loc[obesityLevel_II['Gender'] == 'Female', 'Age'].mean().astype(int)

print("Média de idade entre homens em Obesity_Type_II:", mean_age_male_Obesity_II)
print("Média de idade entre mulheres em Obesity_Type_II:", mean_age_female_Obesity_II)

# Filter for Obesity_Type_III
obesityLevel_III = obesityTypeDataSet.loc[obesityTypeDataSet['NObeyesdad'] == 'Obesity_Type_III']

# Calculate mean age for Obesity_Type_III by gender
mean_age_male_Obesity_III = obesityLevel_III.loc[obesityLevel_III['Gender'] == 'Male', 'Age'].mean().astype(int)
mean_age_female_Obesity_III = obesityLevel_III.loc[obesityLevel_III['Gender'] == 'Female', 'Age'].mean().astype(int)

print("Média de idade entre homens em Obesity_Type_III:", mean_age_male_Obesity_III)
print("Média de idade entre mulheres em Obesity_Type_III:", mean_age_female_Obesity_III)

# Calculate mean and median age by gender for entire dataset
mean_obesityData_Man = obesityTypeDataSet.loc[obesityTypeDataSet['Gender'] == 'Male', 'Age'].mean()
mean_obesityData_Woman = obesityTypeDataSet.loc[obesityTypeDataSet['Gender'] == 'Female', 'Age'].mean()

print("Média de idade entre homens no dataset completo:", mean_obesityData_Man)
print("Média de idade entre mulheres no dataset completo:", mean_obesityData_Woman)

median_man = np.median(obesityTypeDataSet.loc[obesityTypeDataSet['Gender'] == 'Male', 'Age'])
median_woman = np.median(obesityTypeDataSet.loc[obesityTypeDataSet['Gender'] == 'Female', 'Age'])

print("Mediana de idade entre homens no dataset completo:", median_man)
print("Mediana de idade entre mulheres no dataset completo:", median_woman)

# Creating dataset for specific analysis
consumo_de_Alimentos_e_habitos = obesityTypeDataSet[['Age', 'Gender', 'FAVC', 'FCVC', 'NCP', 'family_history_with_overweight', 'imc', 'NObeyesdad']]

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical columns
df_encoded = obesityTypeDataSet.copy()
columns_to_encode = ['Gender', 'CALC', 'FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS', 'NObeyesdad']

for column in columns_to_encode:
    df_encoded[column] = label_encoder.fit_transform(df_encoded[column])

# Dash app initialization
app = Dash(__name__)

# Ensure 'Age', 'MTRANS', 'Weight', and 'imc' are in the correct format
df = obesityTypeDataSet.copy()
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['MTRANS'] = df['MTRANS'].astype(str)
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce').fillna(0).astype(int)
df['imc'] = pd.to_numeric(df['imc'], errors='coerce').fillna(0).astype(int)

# Round 'Height' column to two decimal places
df['Height'] = df['Height'].round(2)

# Count individuals by Age and MTRANS
df_count = df.groupby(['Age', 'MTRANS']).size().reset_index(name='count')

# Count individuals by imc and NObeyesdad
df_count_imc_nob = df.groupby(['imc', 'NObeyesdad']).size().reset_index(name='count')

# Dash app layout
app.layout = html.Div([
    html.H1(children='Dashboard - OBESITY LEVELS', style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id='line-graph-age-mtrans'),
        dcc.Graph(id='scatter-graph-weight-imc')
    ], style={'display': 'flex', 'justify-content': 'space-around'}),
    html.Div([
        dcc.Graph(id='bar-graph-height-weight'),
        dcc.Graph(id='bar-graph-weight-nobeyesdad')
    ], style={'display': 'flex', 'justify-content': 'space-around'}),
    html.Div([
        dcc.Graph(id='line-graph-imc-nobeyesdad'),
    ], style={'display': 'flex', 'justify-content': 'space-around'})
])

# Callback functions for updating graphs

# Line graph for Age and MTRANS
@app.callback(
    Output('line-graph-age-mtrans', 'figure'),
    Input('line-graph-age-mtrans', 'id')  # Placeholder input
)
def update_line_graph_age_mtrans(value):
    fig = px.line(df_count, x='Age', y='count', color='MTRANS', 
                  title='Quantity of Individuals by Age and Transport Mode', 
                  labels={'Age': 'Age', 'count': 'Quantity of Individuals', 'MTRANS': 'Transport Mode'})
    return fig

# Scatter plot for Weight and IMC
@app.callback(
    Output('scatter-graph-weight-imc', 'figure'),
    Input('scatter-graph-weight-imc', 'id')  # Placeholder input
)
def update_scatter_graph_weight_imc(value):
    fig = px.scatter(df, x='Weight', y='imc', title='Relationship between Weight and IMC',
                     labels={'Weight': 'Weight', 'imc': 'IMC'})
    return fig

# Bar graph for Height and Weight
@app.callback(
    Output('bar-graph-height-weight', 'figure'),
    Input('bar-graph-height-weight', 'id')  # Placeholder input
)
def update_bar_graph_height_weight(value):
    fig = px.bar(df, x='Weight', y='Height', title='Relationship between Height and Weight',
                     labels={'Weight': 'Weight', 'Height': 'Height'})
    return fig

# Bar graph for Weight and NObeyesdad
@app.callback(
    Output('bar-graph-weight-nobeyesdad', 'figure'),
    Input('bar-graph-weight-nobeyesdad', 'id')  # Placeholder input
)
def update_bar_graph_weight_nobeyesdad(value):
    fig = px.bar(df, x='NObeyesdad', y='Weight', title='Relationship between Weight and Obesity Level',
                     labels={'Weight': 'Weight', 'NObeyesdad': 'Obesity Level'})
    return fig

# Line graph for IMC and NObeyesdad
@app.callback(
    Output('line-graph-imc-nobeyesdad', 'figure'),
    Input('line-graph-imc-nobeyesdad', 'id')  # Placeholder input
)
def update_line_graph_imc_nobeyesdad(value):
    fig = px.line(df_count_imc_nob, x='imc', y='count', color='NObeyesdad', 
                  title='Quantity of Individuals by IMC and Obesity Level',
                  labels={'count': 'Quantity of Individuals', 'imc': 'IMC', 'NObeyesdad': 'Obesity Level'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

