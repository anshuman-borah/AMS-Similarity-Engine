from app.db import collection

def get_documents():
    docs = list(collection.find({}))

    # Fallback if DB is empty
    if len(docs) == 0:
        print("⚠️ No data in DB, using fallback")

        return [
            "AI crop disease detection using CNN",
            "Deep learning for plant disease classification",
            "Smart irrigation using IoT"
        ]

    documents = []

    for d in docs:
        title = d.get("title", "")
        description = d.get("description", "")
        objectives = d.get("objectives", "")
        methodology = d.get("methodology", "")

        text = f"""
        {title} {title}

        {description}

        {objectives}

        {methodology}
        """

        documents.append(text.strip())

    return documents