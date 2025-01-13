a. All’avvio del programma, si crei un grafo semplice, pesato e non orientato i cui vertici siano tutte le localizzazioni 
(tabella classification, colonna localization).
b. Ogni localizzazione contiene un insieme di geni, i quali possono essere collegati tra di loro attraverso la tabella 
interactions. I vertici corrispondenti a due localizzazioni saranno collegati da un arco se e solo se esiste almeno u
na interazione che coinvolge due geni, rispettivamente della prima della seconda localizzazione (o nell’ordine inverso).
c. Il peso di ciascun arco dovrà essere un numero intero, pari al numero di tipi1 diversi di interazioni tra i geni 
associati alle due localizzazioni. Nell’esempio seguente (che riporta solo un sottoinsieme delle righe), vi sono molti 
geni associati a cytoplasm che interagiscono con geni associati a cytoskeleton, ma i tipi di interazione riscontrati 
in questo caso sono 3.
d. Si visualizzi il numero di vertici ed archi del grafo.
e. Permettere all’utente di selezionare una localizzazione, ed alla pressione del tasto “Statistiche”, stampare
tutte le localizzazioni connesse a quelle selezionata, visualizzando per ciascuna di esse il peso dell’arco corrispondente.
PUNTO 2
a. A partire dal grafo calcolato al punto precedente, alla pressione del tasto “Ricerca Cammino”, si avvii una procedura di ricerca ricorsiva per determinare il più lungo cammino semplice di localizzazioni che parta dalla localizzazione selezionata dall’utente. La lunghezza del cammino sarà valutata dalla somma dei pesi degli archi incontrati.
b. Si stampi la sequenza di localizzazioni di lunghezza massima così ottenuta.
