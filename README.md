# NLP_final_project
https://github.com/DigiUGA/Gutenberg_Text
Helpful Resources:Coding Systems for Themes of Agency and Communion
https://www.sesp.northwestern.edu/foley/instruments/agency/

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
