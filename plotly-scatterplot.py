import plotly
import plotly.graph_objs as go


import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)


trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)
data = [trace]


plotly.offline.plot(data, filename='basic-scatter')
