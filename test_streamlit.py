
import paho.mqtt.client as mqtt
import streamlit as st
from datetime import datetime
import random
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

placeholder = st.empty()

data = {}

def on_message(client, userdata, message):
    global data

    now = datetime.now()
    value = float(message.payload.decode("utf-8"))
    if message.topic not in data:
        data[message.topic] = pd.Series(dtype=float)
    
    data[message.topic][now] = value

    # plotly express    
    # df = pd.DataFrame(data)
    # fig = px.line(df)
    
    fig = go.Figure()
    for k in data:
        fig.add_scatter(x=data[k].index, y=data[k], mode='lines+markers',line_shape='spline',name=k, hovertemplate=k+'<br>time:%{x}<br>value:%{y}') 

    fig.update_layout(title='感測器數據')
    # fig.update_layout(legend=dict(
    #     orientation="h",
    #     yanchor="bottom",
    #     y=1.02,
    #     xanchor="left",
    #     x=0))

    placeholder.write(fig)

broker = "broker.hivemq.com"
client = mqtt.Client(f"client{random.random()}")
client.on_message = on_message
client.connect(broker)
client.subscribe("wetland/sensor/#")
client.loop_forever()
