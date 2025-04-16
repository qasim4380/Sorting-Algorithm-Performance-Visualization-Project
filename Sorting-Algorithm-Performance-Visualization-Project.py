

# **Bubble Sort**


import plotly.graph_objects as go
import pandas as pd

df_usgsn03 = pd.read_csv('BubbleFork.csv',sep=',')
df_usgsn04 = pd.read_csv('BubbleThread.csv',sep=',')


df_usgsn03_sorted = df_usgsn03.sort_values(by='trial')
df_usgsn04_sorted = df_usgsn04.sort_values(by='trial')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_usgsn03_sorted['trial'],
        y=df_usgsn03_sorted['time'],
        name = 'Fork'     
    ))

fig.add_trace(
    go.Scatter(
        x=df_usgsn04_sorted['trial'],
        y=df_usgsn04_sorted['time'],
        name = 'Thread'
    ))

fig.update_layout(title = 'Bubble sort', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()



"""

# **Comb Sort**

"""

import plotly.graph_objects as go
import pandas as pd

df_usgsn03 = pd.read_csv('CombFork.csv',sep=',')
df_usgsn04 = pd.read_csv('CombThread.csv',sep=',')


df_usgsn03_sorted = df_usgsn03.sort_values(by='trial')
df_usgsn04_sorted = df_usgsn04.sort_values(by='trial')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_usgsn03_sorted['trial'],
        y=df_usgsn03_sorted['time'],
        name = 'Fork'     
    ))

fig.add_trace(
    go.Scatter(
        x=df_usgsn04_sorted['trial'],
        y=df_usgsn04_sorted['time'],
        name = 'Thread'
    ))

fig.update_layout(title = 'Comb Sort', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()



"""#**Insertion Sort**"""

import plotly.graph_objects as go
import pandas as pd

df_usgsn03 = pd.read_csv('InsertionFork.csv',sep=',')
df_usgsn04 = pd.read_csv('InsertionThread.csv',sep=',')


df_usgsn03_sorted = df_usgsn03.sort_values(by='trial')
df_usgsn04_sorted = df_usgsn04.sort_values(by='trial')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_usgsn03_sorted['trial'],
        y=df_usgsn03_sorted['time'],
        name = 'Fork'     
    ))

fig.add_trace(
    go.Scatter(
        x=df_usgsn04_sorted['trial'],
        y=df_usgsn04_sorted['time'],
        name = 'Thread'
    ))

fig.update_layout(title = 'Insertion sort', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()



"""#**Selection Sort**"""

import plotly.graph_objects as go
import pandas as pd

df_usgsn03 = pd.read_csv('SelectionFork.csv',sep=',')
df_usgsn04 = pd.read_csv('SelectionThread.csv',sep=',')


df_usgsn03_sorted = df_usgsn03.sort_values(by='trial')
df_usgsn04_sorted = df_usgsn04.sort_values(by='trial')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_usgsn03_sorted['trial'],
        y=df_usgsn03_sorted['time'],
        name = 'Fork'     
    ))

fig.add_trace(
    go.Scatter(
        x=df_usgsn04_sorted['trial'],
        y=df_usgsn04_sorted['time'],
        name = 'Thread'
    ))

fig.update_layout(title = 'Selection sort', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()



"""#**Shell Sort**"""

import plotly.graph_objects as go
import pandas as pd

df_usgsn03 = pd.read_csv('ShellFork.csv',sep=',')
df_usgsn04 = pd.read_csv('ShellThread.csv',sep=',')


df_usgsn03_sorted = df_usgsn03.sort_values(by='trial')
df_usgsn04_sorted = df_usgsn04.sort_values(by='trial')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_usgsn03_sorted['trial'],
        y=df_usgsn03_sorted['time'],
        name = 'Fork'     
    ))

fig.add_trace(
    go.Scatter(
        x=df_usgsn04_sorted['trial'],
        y=df_usgsn04_sorted['time'],
        name = 'Thread'
        
    ))

fig.update_layout(title = 'Shell sort', xaxis_title='Trial',yaxis_title='Time(seconds)')

fig.show()
