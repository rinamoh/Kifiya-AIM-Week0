import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px

def stats(dataframe):
    st.header('Data Statistics')
    st.markdown('#These are some details about your data')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header('Data Header')
    st.markdown('#These are some examples of your data')
    st.write(dataframe.head())

def interactive_plot(dataframe):
    x_axis_val=st.selectbox('Select X-Axis Value', options=dataframe.columns)
    y_axis_val=st.selectbox('Select Y-Axis Value', options=dataframe.columns)
#this plots the options that the user chose 
    plot=px.scatter(dataframe,x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)

# df=pd.DataFrame()
st.title("Dashboard Page")
st.markdown('#This is a page created to design and develop a dashboard using streamlit')

#to add an uploaded file 
st.sidebar.title('Navigation')
uploaded_file=st.sidebar.file_uploader("Please Upload Your File Here")

#create a radio button on the navigation
options = st.sidebar.radio('Pages', options=[
    'Home','Data Statistics','Data Header','Plot','Interactive Plot'])

#this will take the uploaded file and then find the mean,median and other charachteristcs
if uploaded_file:
    
    df = pd.read_csv(uploaded_file)
    

    if options =='Data Statistics':
        stats(df)
    elif options =='Data Header':
        data_header(df)
    elif options =='Interactive Plot':
        interactive_plot(df)



    
    
    