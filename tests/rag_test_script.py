from rag import search_documents

results = search_documents(
    "How can I improve my resume for ATS?"
)

for item in results:
    print("-" * 80)
    print(item)