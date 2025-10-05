from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='10.Document_Loaders/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[0].page_content)

# returns 1 document object per row of the csv file