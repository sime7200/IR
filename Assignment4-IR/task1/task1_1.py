from collections import defaultdict

# Testo di input
text = "Ocean environment is a deep and complex ecosystem filled with diverse creatures. Yet, much about the ocean lacks exploration."

# Lista di stop-words 
#stop_words = {"is", "a", "with", "the", "and", "yet", "much", "about"}
stop_words = {"a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your"} # from Textifier

# Funzione per creare una lista invertita senza stop-words
def inverted_list(text, stop_words):
    # Tokenizzazione del testo e rimozione delle stop-words
    words = text.lower().replace(".", "").split()
    filtered_words = [(word, i + 1) for i, word in enumerate(words) if word not in stop_words]
    
    # Creazione della lista invertita
    inverted_index = defaultdict(list)
    for word, position in filtered_words:
        inverted_index[word].append(position)
    
    return inverted_index

# Funzione per creare una lista invertita con block addressing
def inverted_list_block_addressing(inverted_index, block_size=4):
    # Creazione di un nuovo dizionario per memorizzare i blocchi
    block_index = defaultdict(set)
    for word, positions in inverted_index.items():
        for pos in positions:
            block = (pos - 1) // block_size + 1  # Calcolo del blocco
            block_index[word].add(block)
    
    # Convertiamo i set in liste ordinate per leggibilità
    return {word: sorted(blocks) for word, blocks in block_index.items()}

# Funzione per costruire un albero dei suffissi parziale
def build_suffix_tree(words):
    suffix_tree = {}
    
    for word in words:
        current_dict = suffix_tree
        for i in range(len(word)):
            suffix = word[i:]  # Otteniamo il suffisso corrente
            if suffix not in current_dict:
                current_dict[suffix] = {}
            current_dict = current_dict[suffix]
    
    return suffix_tree


# Step 1: Costruzione della lista invertita senza stop-words
inverted_index = inverted_list(text, stop_words)
print("Lista Invertita:\n", dict(inverted_index))

# Step 2: Lista invertita con block addressing
block_addressing_index = inverted_list_block_addressing(inverted_index, block_size=4)
print("\nLista Invertita con Block Addressing:\n", block_addressing_index)

# Step 3: Albero dei suffissi parziale
# Selezioniamo alcune parole per costruire il suffix tree
selected_words = ["ocean", "environment", "ecosystem", "creatures", "exploration"]
suffix_tree = build_suffix_tree(selected_words)
print("\nAlbero dei Suffissi Parziale:\n", suffix_tree)
