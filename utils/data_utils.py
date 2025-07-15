import numpy as np
import plotly.graph_objs as go

def fetch_cricket_player_data(player_name):
    # MOCKED: Replace with real API later
    # Just returns fake recent match scores
    return {
        'recent_runs': [45, 50, 30, 60, 40]
    }

def preprocess_data(data):
    runs = data['recent_runs']
    avg = np.mean(runs)
    std = np.std(runs)
    features = [avg, std]
    chart = generate_chart(runs)
    return features, chart

def generate_chart(runs):
    trace = go.Bar(y=runs, name='Runs')
    layout = go.Layout(title="Recent Run Scores")
    fig = go.Figure(data=[trace], layout=layout)
    return fig.to_html(full_html=False)
