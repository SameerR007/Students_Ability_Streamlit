import streamlit as st
def main():
   import pandas as pd
   import sklearn
   from sklearn import preprocessing
   from matplotlib import pyplot as plt
   data=pd.read_excel("DUET Data - Copy.xlsx")
   data=data.dropna()
   data=data[data['Graduation Marks']>=50]
   x=data[['Graduation Marks','Entrance Marks']]
   x_scaled=preprocessing.scale(x)
   kmeans_new=KMeans(4,random_state=1)
   kmeans_new.fit(x_scaled)
   clusters_new=x.copy()
   clusters_new['clusters']=kmeans_new.fit_predict(x_scaled) 
   clusters_new=pd.read_excel("clusters_new.xlsx")
    
   gm=st.number_input("Graduation Marks")
   em=st.number_input("Entrance Marks")
   input_para=[gm,em]
   input_para[0]=(input_para[0]-data['Graduation Marks'].mean())/data['Graduation Marks'].std()
   input_para[1]=(input_para[1]-data['Entrance Marks'].mean())/data['Entrance Marks'].std()   
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
