import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing


scatter_column, setting_column = st.beta_column((4, 1))

scatter_column.title("Multi-Dimensional Analysis")

setting_column.title("Settings")
