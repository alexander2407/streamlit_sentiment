This Streamlit App uses a Deeplearning Model from huggingface.com (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english). 

It predicts the sentiment of an english sentence. Requests work over an html page (standard for run below is localhost:5000) where the input sentence can be put into a text field and the output is printed below.
On first opening of the website it might take a few seconds for the model to download.

Docker run command: docker run -d -p 5000:8501 aruckner/sdc_uebung4

Extended by providing workflow that deploys to docker hub and azure.
 
Link to Azure: https://ds20m002-sentiment-streamlit.azurewebsites.net/
