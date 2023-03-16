import streamlit as st
def main():
    import pandas as pd
    import pickle
    kmeans_new=pickle.load(open("model.pkl","rb"))
    clusters_new=pd.read_excel("clusters_new.xlsx")
    gm=st.number_input("Graduation Marks")
    em=st.number_input("Entrance Marks")
    input_para=[gm,em]
    input_para[0]=(input_para[0]-77.3172)/9.2327
    input_para[1]=(input_para[1]-127.9162)/27.4483
    if st.button("Result"):

        if (kmeans_new.predict([input_para])==0):
            result="Not Selected this time. Better luck next time."
        elif (kmeans_new.predict([input_para])==1):
            result="Congratulations! Selected for the course."
        elif(kmeans_new.predict([input_para])==2):
            result="Congratulations! Selected for the next second exam."
        else:
            result="Congratulations! Selected for the interview."
        st.text(result)
    
if __name__=='__main__':
    main()
