import pickle
import streamlit as st

#loading the model

pickle_in = open('classifier.pickle', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

#defining the function which will make tehe prediction using the data which the user input

def prediction(area, month):
    #preproocessing user iimput
    # area
   
    if area == "춘천":
        area = 0
    elif area == "평택":
        area = 1
    else: 
        area = 2
    
    # prediction 

    prediction = classifier.predict([[area, month]])
  
# Making prediction

    if prediction == 0:
        pred = 'cannot produce'
    elif prediction == 1:
        pred = 'can produce'
    return pred

# define the page in main

def main():
    #front end
    html_temp = """
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">RS-Team ML</h1> 
    </div> 
    """
    
    #display front end aspect 
    st.markdown(html_temp, unsafe_allow_html = True)


    area = st.selectbox('Area', ('춘천', '평택', '제주'))
    #area = st.number_input('area', value=1)
    month = st.number_input('Enter a number corresponding to the Month', value = 1)

    result = ""

    #Make the predicttion after a click 

    if st.button('Predict'):
        result = prediction(area, month)
        st.success('Radish {}'.format(result))
        print(radsish)

if __name__ =='__main__':
    main()