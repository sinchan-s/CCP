# CCP
Color Consum Prediction(CCP) is a very helpful tool to be used in the Textile Printing Production. The main focus of this tool is to predict the actual color paste quantity(in Kg) that will be required to print a particular color.  
This repository is divided into 4 components:  
1. **Client**: it contains files to generate a static website viz. [app.html](https://github.com/sinchan-s/CCP/blob/main/client/app.html), [app.css](https://github.com/sinchan-s/CCP/blob/main/client/app.css) & [app.js](https://github.com/sinchan-s/CCP/blob/main/client/app.js) to integrate with python server files.
2. **Model**: it contains the main python [notebook](https://github.com/sinchan-s/CCP/blob/main/model/Color-Consum-Prediction.ipynb), pickle file generated from the trained machine learning model and a [json](https://github.com/sinchan-s/CCP/blob/main/model/columns.json) file containing headers of dataset features.
3. **Server**: it contains python [utiliy](https://github.com/sinchan-s/CCP/blob/main/server/util.py) file for the flask [server](https://github.com/sinchan-s/CCP/blob/main/server/server.py) to operate.
4. **Streamlit-model**: it contains the streamlit framework based python [predictor](https://github.com/sinchan-s/CCP/blob/main/streamlit-model/st-color_pred.py) web-app, which is deployed on the streamit cloud platform and can be accessed with this [link](https://sinchan-s-ccp-streamlit-modelst-color-pred-9yqvu3.streamlitapp.com/)🙂.  
   
### Streamlit web-app:
![image](https://user-images.githubusercontent.com/63915540/177386368-553915cb-4aff-474f-ae69-6582bdc14b98.png)
