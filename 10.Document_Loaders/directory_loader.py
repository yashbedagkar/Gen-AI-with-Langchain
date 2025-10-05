from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='10.Document_Loaders/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
# lazy_load is used if working with too many large files
# it returns a generator instead of a list

for document in docs:
    print(document.metadata)

# returns 1 document object per page if pdfs, depends on the file type