import streamlit as st                #pip install streamlit
import pandas as pd                   #pip install pandas
import plotly.express as px           #pip install plotly-express
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from PIL import Image  # Pillow  https://pillow.readthedocs.io/en/stable/reference/Image.html


#https://analyticsindiamag.com/a-beginners-guide-to-streamlit-convert-python-code-into-an-app/
# Deploy
# https://pythonwife.com/deploy-the-streamlit-application/

# This will display the title top left of your screem
st.set_page_config(
            page_title="Data Divers Team ",
            page_icon=":gem:",
            #layout="wide",     # "wide" uses the entire screen.
            layout="centered",  # Defaults to "centered", which constrains the elements into a centered column of fixed width
            initial_sidebar_state="expanded"
            #initial_sidebar_state="collapsed"
        )

# Streamlit cache things which will help to run the application faster
@st.cache()
# NOTE: This must be the first command in your app, and must be set only once
#st.set_page_config(layout="wide")

    
def types(df):
    return pd.DataFrame(df.dtypes, columns=['Type'])

def main():
    st.sidebar.title("What would you like to do?")
    activities = ["Home","Exploring the data", "Plotting and Visualization","Prediction", "Our Team"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    # USING THE SIDE BAR
    st.sidebar.title("Please upload Your CSV File: ")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type={"csv"})   
    #uploaded_file = st.file_uploader("Choose a CSV file")
    
    if uploaded_file is not None and choice == "Home":
        data = pd.read_csv(uploaded_file)
        
        # My title of my project
        st.title("We are Diamond Data Divers :gem:")
    
        IMAGE = "diamond.png"
        st.markdown(
            """
            <style>
            .container {
                display: flex;
            }
            .logo-text {
                font-weight:1000 !impotant;
                font-size:60px !important;
                color: #f9a01b !important;
                padding-top: 75px !important;
            }
            .logo-img {
                float:center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="container">
                <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(IMAGE, "rb").read()).decode()}">
                <p class="logo-text"></p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
       
        st.markdown(
        """
       \n
       
        """,
        unsafe_allow_html=True,
        )
        st.subheader("About this project:")
        st.markdown('''
                  :large_blue_diamond: Data cleaning.\n
                  :large_blue_diamond: Understand better the diamond market.\n
                  :large_blue_diamond: Identify trends.\n
                  :large_blue_diamond: small_blue_diamond: Build a model that can predict prices for 2022.\n
                   ''')  
  
    # How to get rid of "Unnamed: 0" column in a pandas DataFrame read in from CSV file?
    # https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe-    read-in-from-csv-fil
    
    elif uploaded_file is not None and choice == "Exploring the data":
        # My title of my project
        st.title("Exploring the Data :chart_with_upwards_trend:")
        
        #data = pd.read_csv(uploaded_file, index_col=[0])
        data = pd.read_csv(uploaded_file)
        #st.header(choice) 
                     
        # Show dataset
        if st.checkbox("Show Dataset"):
            rows = st.number_input("Number of rows", 5, len(data))
            st.dataframe(data.head(rows))
            
        # Show columns
        if st.checkbox("Columns"):
            st.write(data.columns)   
            
        # Show Shape
        if st.checkbox("Shape of Dataset"):
            data_dim = st.radio("Show by", ("Rows", "Columns", "Shape"))
            if data_dim == "Columns":
                st.text("Number of Columns: ")
                st.write(data.shape[1])
            elif data_dim == "Rows":
                st.text("Number of Rows: ")
                st.write(data.shape[0])
            else:
                st.write(data.shape)
            
        # Show Data summary
        if st.checkbox("Show Data Summary"):
            st.text("Datatypes Summary")
            st.write(data.describe())
      

    elif uploaded_file is not None and choice == "Plotting and Visualization":
        st.title("Plotting and Visualization :bar_chart:")
        #st.subheader(choice)
        data = pd.read_csv(uploaded_file)
        df = data.copy()
        all_columns = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot", ["bar", "pie", "scatter"]) 

        if type_of_plot=="bar":
            select_columns_to_plot = st.multiselect("Select columns to plot", all_columns)
            cust_data = df[select_columns_to_plot]
            st.bar_chart(cust_data)

        elif type_of_plot=="pie":
            select_columns_to_plot = st.selectbox("Select a column", all_columns)
            st.write(df[select_columns_to_plot].value_counts().plot.pie())
            st.pyplot()

        elif type_of_plot=="scatter":
            st.write("Scatter Plot")
            scatter_x = st.selectbox("Select a column for X Axis", all_columns)
            scatter_y = st.selectbox("Select a column for Y Axis", all_columns)
            st.write(sns.scatterplot(x=scatter_x, y=scatter_y, data = df))
            st.pyplot()
            
    elif uploaded_file is not None and choice == "Prediction": 
        #st.subheader(choice)
        st.title("Data Modeling :chart_with_downwards_trend:")
        data = pd.read_csv(uploaded_file)
        df = data.copy()
        all_columns = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot", ["Linear Regression", "SVR Model", "Tree"]) 
        
        
    elif uploaded_file is not None and choice == "Our Team":
        #st.subheader(choice)
        st.title(" Our Team 🏅")
        st.write("We are selected into the 2022 cohort of Hack. Diversity’s career leadership and workforce development program for racial or ethnic minorities in the tech field. Thank you Hack. Diversity for choosing us.")
        st.balloons()
        
        #col1,mid,col2 =st.columns([1,1,20])
        #with col1:
        #    st.image('team_black.png',use_column_width=False)
        #with col2:
        #    st.write("Eduardo")
    
        # Another way
        #image = Image.open('team_black.png')
        #size = (800, 800)
        #image.thumbnail(size)
        #fig = plt.figure()
        #plt.imshow(image)
        #plt.axis("off")
        #st.pyplot(fig)
        
        

        st.subheader("Hey, I am Eduardo :star:")
        
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/eduardo-s%C3%A1-73b76286)
              - [Medium:](https://medium.com/hack-diversity-movement/cohort-stories-meet-eduardo-77e1c2805134)
        
               ''')
   
        
        st.subheader("Hey, I am Cyrus Kirby :star:")
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/cyrus-kirby)
              - [Medium:](https://medium.com/hack-diversity-movement/cohort-stories-meet-cyrus-b1210c0eaa9b)
               ''')
        
        st.subheader("Hey, I am Kevin T :star:")
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/eduardo-s%C3%A1-73b76286)
              - [Medium:](https://medium.com/hack-diversity-movement/cohort-stories-meet-kevin-t-674db5c2dad)
               ''')
        
        st.subheader("Hey, I am Rita Nfamba :star:")
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/rita-nfamba-06136511a)
              - [Medium:](https://medium.com/hack-diversity-movement/cohort-stories-meet-rita-c79a0203cc2f)
               ''')
        
        st.subheader("Hey, I am Justice DelCore :star:")
        st.markdown('''
              I am originally from Brazil. If you are interested in buiding more Computer Apps like this one, please contact us. Please feel free to contact me via email: eduardo.duartesa001@umb.edu.\n
        
              Also check my Social Media:
              - [LinkedIn:](https://www.linkedin.com/in/delcorej)
              - [Medium:](https://medium.com/hack-diversity-movement/cohort-stories-meet-eduardo-77e1c2805134)
               ''')
       
        # one way
        #st.image('team_black.png',use_column_width=False)
       
         # Another way
        image = Image.open('team_black.png')
        size = (800, 800)
        image.thumbnail(size)
        fig = plt.figure()
        plt.imshow(image)
        plt.axis("off")
        st.pyplot(fig)
    
# The Python is executed directly by the python interpreter  


if __name__ == "__main__":
    main() 

# https://github.com/mwitiderrick/Image-Processing/blob/master/streamlit_app.py