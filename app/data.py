from app.db import collection

def get_documents():
    docs = list(collection.find({}))

    if len(docs) == 0:
        print("⚠️ No data in DB, using fallback")

        return [
            "AI crop disease detection using CNN",
            "Deep learning for plant disease classification",
            "IoT based smart irrigation system"
        ]

    documents = []

    for d in docs:
        text = f"""
        {d.get('title', '')}
        {d.get('description', '')}
        {d.get('objectives', '')}
        {d.get('methodology', '')}
        """

        documents.append(text.strip())

    return documents