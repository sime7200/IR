from collections import defaultdict

documents = {
    "D1": "The universe is vast and mysterious, filled with countless stars and galaxies.",
    "D2": "Each star may host its own planets, some of which could harbor life.",
    "D3": "Scientists explore these possibilities through advanced telescopes and technology.",
    "D4": "Yet, many questions about our universe remain unanswered, driving curiosity and research.",
    "D5": "The quest for knowledge continues, pushing the boundaries of human understanding."
}

# Lista di stop-words
stop_words = {"a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your"} # from Textifier

# Funzione per creare l'indice invertito
def build_inverted_index(documents, stop_words):
    inverted_index = defaultdict(set) 
    
    for doc_id, text in documents.items():
        # Tokenizza e rimuove stop-words
        words = text.lower().replace(",", "").replace(".", "").split()
        filtered_words = [word for word in words if word not in stop_words]
        
        # Aggiungi ogni parola con l'ID del documento
        for word in filtered_words:
            inverted_index[word].add(doc_id)
    
    return {word: sorted(list(doc_ids)) for word, doc_ids in inverted_index.items()}

inverted_index = build_inverted_index(documents, stop_words)
print("Indice Invertito con Liste di Posting:\n", inverted_index)
