import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
html.H1("Fruit Quantities", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='fruit-dropdown',
        options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit']],
        value='Apples',  # Default selection
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='fruit-bar-chart')
])

# Define the callback to update the graph
@app.callback(
    Output('fruit-bar-chart', 'figure'),
    [Input('fruit-dropdown', 'value')]
)
def update_graph(selected_fruit):
    # Filter the data to only include the selected fruit
    filtered_df = df[df['Fruit'] == selected_fruit]
    
    # Create the bar chart
    fig = px.bar(
        filtered_df,
        x='Fruit',
        y='Amount',
        title=f"Quantity of {selected_fruit}",
        labels={'Amount': 'Quantity'},
        color='Fruit',
        height=400
    )
    fig.update_layout(
        xaxis_title="Fruit",
        yaxis_title="Quantity",
        title_x=0.5
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)