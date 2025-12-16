import getpass
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 获取当前脚本所在的绝对路径 (相当于 Node.js 的 __dirname)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 拼接出 PDF 的完整路径 (相当于 path.join(__dirname, '...'))
file_path = os.path.join(current_dir, "temp.pdf")

loader = PyPDFLoader(file_path)
docs = loader.load()

print(len(docs))

print(f"{docs[0].page_content[:200]}\n")

# print(docs[0].metadata)

# 3. 分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
all_splits = text_splitter.split_documents(docs)
# print(len(all_splits))

# print(f"{all_splits[0].page_content[:200]}\n")

# print(all_splits[0].metadata)

# if not os.environ.get("GOOGLE_API_KEY"):
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# vector_1 = embeddings.embed_query(all_splits[0].page_content)
# vector_2 = embeddings.embed_query(all_splits[1].page_content)

# assert len(vector_1) == len(vector_2)
# print(f"Generated vectors of length {len(vector_1)}\n")
# print(vector_1[:10])