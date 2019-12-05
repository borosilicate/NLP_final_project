# NLP_final_project     Texts
https://github.com/DigiUGA/Gutenberg_Text

#Helpful Resources:Coding Systems for Themes of Agency and Communion
https://www.sesp.northwestern.edu/foley/instruments/agency/

#Article about word2vec digital humanities:
https://www.reddit.com/r/MachineLearning/comments/4m7h4f/word_vectors_word2vec_in_eighteenthcentury/
http://bookworm.benschmidt.org/posts/2015-10-25-Word-Embeddings.html
http://ryanheuser.org/word-vectors-1/
http://ryanheuser.org/word-vectors-2/

Word2Vec:
https://colab.research.google.com/drive/1rJJifX_aL63JNqAnTOXPnXm078ejC-1n

List of autobiographies/letters in Project Gutenburg:
Anderson, Hans Christian - The True Story of my Life (1847)
Austin, Jane - The Letters of Jane Austen (1884)
Balzac, Honore - Letters to Madam Hanska (1833)
Conrad, Joseph - Notes on My Life & Letters (1898-1919)
Dumas, Alexandre - My Memoirs Vol 2 - Vol 6 (1844-1846)
Franklin, Benjamin - Autobiography and Memoirs (1791)
Gibbon, Edward - Private Letters of Edward Gibbon (1753-1794)
Goethe, Johann Wolgang von - The Autobiography of Goethe (1774) Letters from Switzerland and Travels in Italy
Hugo, Victor - The Memoirs of Victor Hugo (1899)
James, Henry - The Letters of Henry James (1892-1911)
Morley, Henry - Letters to Sir William Windham and Mr. Pope (1717)
Stevenson, Robert Louis - Memories and Portraits (1887)
Thorough, Henry David -- journal entries (1837-1854)
Trollope, Anthony - An Autobiography of Anthony Trollope (1876)
Twain, Mark — autobiography and letters (1835-1910)
Voltaire — autobiography and letters (1745)

#numbers
 cat -n voltaire_letters.txt | grep LETTER 

#gets text
cat voltaire_letters.txt | awk  "129 <= NR && NR <= 3738" > voltaire_letters_headings.txt

1.) Setup 			 Tool/ENV/Setup

Python 3.7.3
MacOS High Sierra
conda install numpy 
conda install spacy
conda install requests
#This will be a siginificant amount of memory 0.6 gb
conda install -c conda -forge spacy-model-en_core_web_lg

3.)     #gathering synonyms 
	python agency_synonyms.py
	python communion_synonyms.py



4.)
	Michael Joseph Hearn
	

5.) The project was done with a combination of scripts working in an ordered fashion.
    Collect documents
    Recieved Words thematicly related to agency and communion
    web scraped synonyms
    Load spacy word embeddings
    Collect words from docs
    Compare similarity between synonyms and words common to docs
    Use matplotlib to plot scores

https://colab.research.google.com/drive/1rJJifX_aL63JNqAnTOXPnXm078ejC-1n



