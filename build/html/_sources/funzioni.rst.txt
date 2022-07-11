.. figure:: ./_images/logo_3.png
   :align: right
   
Funzioni
===============

La scheda US possiede una serie di funzioni che vanno ad automatizzare alcune delle operazioni che si compiono nel corso della catastazione ed elaborazione dei dati archeologici al fine di aumentare il controllo sull'integrità del dato e la validità dell'output. Al momento per la scheda US sono disponibili le seguenti funzioni:


* apertura delle schede US da selezione su base GIS;
* visualizzazione su GIS della planimetria dell'US del record corrente;
* visualizzazione della pianta all'interno della scheda US;
* creazione in automatico del codice di periodizzazione dell'US;
* controllo automatico dei rapporti stratigrafici;
* esportazione del matrix;
* creazione dell'indice di ordine di successione stratigrafica;
* sistema di generazione di piante composite a partire dalle query della scheda US;
* esportazione schede e indice delle US in formato PDF.

Le funzioni sono molto importanti per poter avere una schedatura corretta delle US/USM oltre che permettere a Qgis di disegnare correttamente le singole geometrie.
Le Unità Stratigrafiche in pianta vengono disegnate dentro al layer informativo pyunitastratigrafiche che contiene solo il limite dell'US e le sue caratterizzazioni (Vedi il paragrafo dedicato al layer informativo pyunitastratigrafiche).
Per generare piante composite, pyArchInit prevede una generazione in automatico a partire da query eseguite sulla scheda US e disegnatte su Qgis. Il disegno avviene tramite pyarchinit_us_view, che collega le geometrie delle US con i dati della scheda US.

Tuttavia Qgis non è in grado di disegnare le US nel loro ordine stratigrafico. Per fare questo esiste un campo apposito "order layer", contenuto nela scheda US che gestisce in Qgis l'ordine di disegno: le più antiche sotto, le più recenti sopra. Per poter assegnare l'indice di ordinamento pyArchInit dispone di uno script che leggendo i rapporti stratigrafici, assegna l'indice. Per poter assegnare l'indice è fondamentale che i rapporti stratigrafici non contengano errori.

Per arrivare ad una schedatura perfetta è bene eseguire il Controllo automatico dei rapporti stratigrafici e generare il Matrix per poter verificare che la schedatura non contenga errori.

Apertura delle schede US da selezione su base GIS
-------------------------------------------------

Sul livello pyarchinit_US_view eseguire una selezione nella porzione di scavo che desiderate.



.. only:: html

.. figure:: ./_images/img_3231f.png
   :align: center

   :descrizione

Oppure, aprite la tabella del livello e utilizzate il query builder di Qgis per realizzare la ricerca che desiderate: in questo caso abbiamo selezionato uno scavo archeologico e tutte le US che per definizione stratigrafica riportano la dicitura: “struttura in muratura”.



.. only:: html

.. figure:: ./_images/img_3231g.png
   :align: center

   :descrizione



.. only:: html

.. figure:: ./_images/img_3231h.png
   :align: center

   :descrizione



.. only:: html

.. figure:: ./_images/img_3231i.png
   :align: center

   :descrizione

Aprite la scheda US di pyArchInit e andate alla sezione Tools. A questo punto cliccate sul pulsante “Show selected Features”. La scheda aprirà i records corrispondenti alla selezione.



.. only:: html

.. figure:: ./_images/img_3231l.png
   :align: center

   :descrizione



.. only:: html

.. figure:: ./_images/img_3231m.png
   :align: center

   :descrizione

Visualizzazione su base GIS dell'US corrente
------------------------------------------------

Quando ci si è posizionati sull'US che si desidera visualizzare, andare nella sezione tools e cliccare sul pulsante "Disegna US”.


.. only:: html

.. figure:: ./_images/img_3231n.png
   :align: center

   :descrizione



.. only:: html

.. figure:: ./_images/img_3231na.png
   :align: center

   :descrizione

In Qgis verrà disegnata l'US corrispondente.



.. only:: html

.. figure:: ./_images/img_3231o.png
   :align: center

   :descrizione


!!! ATTENZIONE !!! AL MOMENTO QUESTO SISTEMA NON FUNZIONA PIU' PER MODIFICA DELLE API DI QGIS!!!

Visualizzazione della pianta all'interno della scheda US
-----------------------------------------------------------------------

È possibile visualizzare la pianta di una US andando nella sezione Tools e cliccando sul pulsante “Preview pianta US” apparirà un messaggio che vi avvertirà che ogni US consultata sarà caricata nell'apposita sezione.

Andando nella sezione “Piante” della scheda US sarà possibile visualizzare la pianta dell'US, con le caratterizzazioni e le quote. Posizionandosi sulla pianta è possibile zoomare con la rotella del mouse e selezionando lo strumento di spostamento (icona con la manina) è possibile navigare in ogni direzione.


Creazione in automatico del codice di periodizzazione dell'US
----------------------------------------------------------------

Dalla scheda US è possibile creare il codice di periodizzazione dell'US.

Come spiegato nel capitolo inerente alla scheda di Periodizzazione e nella parte della scheda US riguardante la periodizzazione,
una volta assegnato un periodo/fase iniziale all'US e un eventuale periodo finale, basta cliccare nella sezione Tools il
pulsante “Crea codice Periodo”.


.. only:: html

.. figure:: ./_images/img_3231p.png
   :align: center

   :descrizione

Sarà assegnato il valore del codice periodo dalla periodizzazione finale all'iniziale, divisi da uno slash per motivi prettamente informatici. Se uno strato vive dal periodo 2.1 fino al 2.3, il codice di periodizzazione sarà: 2/3/4



.. table::

    ======= ===== =======
    Periodo  Fase Codice
    ======= ===== =======
    2		1	  2
    2		2	  3
    2		3	  4
    ======= ===== =======

test::

    Risultato: 2/3/4


.. only:: html

.. figure:: ./_images/img_3231q.png
   :align: center

   :descrizione


La sintassi del valore inserito nel campo, serve a pyArchInit per poter realizzare le query di
richiamo delle piante di fase, attraverso una sintassi specifica:

cont_per = '3' OR cont_per LIKE '3/%' OR cont_per LIKE '%/3' OR cont_per LIKE '%/3/%'



.. only:: html

.. figure:: ./_images/img_3231r.png
   :align: center

   :descrizione

Sul campo cont_per viene cercato il codice di periodizzazione in quattro modalità:

1. cont_per = valore: trova tutte le US che vivono solo nel periodo preso in esame;
cont_per LIKE 'valore/%': trova tutte le US che iniziano in un certo periodo e arrivano fino
ai periodi successivi;
3. cont_per LIKE '%/valore': trova tutte le US che finiscono in un certo periodo e iniziano nei
periodi precedenti;
4. cont_per LIKE '%/valore/%': trova tutte le US che afferiscono ad un periodo intermedio tra un periodo iniziale e uno finale.




.. only:: html

.. figure:: ./_images/img_3231r1.png
   :align: center

   :descrizione

Sistema di generazione di piante composite a partire dalle query della scheda US
--------------------------------------------------------------------------------------------

1. Andate nella sezione Tools della scheda US e cliccare sul pulsante “Visualizzazione GIS”; apparirà un messaggio che vi informa che le vostre ricerche saranno trasformate in piante di scavo.




.. only:: html

.. figure:: ./_images/img_3231a.png
   :align: center

   :descrizione

2. Dopo aver cliccato su “New Search” impostate una ricerca (in questo caso cerchiamo la struttura TB01 – una tomba, di uno scavo di Ravenna).





.. only:: html


.. figure:: ./_images/img_3231b.png
   :align: center

   :descrizione


3. Lanciate la ricerca cliccando su “Search!!!”.




.. only:: html

.. figure:: ./_images/img_3231c.png
   :align: center

   :descrizione


4. Sul GIS vengono caricate le US corrispondenti alla ricerca, caratterizzate in base agli stili pre-impostati di Qgis (vedi capitolo sugli stili); nella scheda US invece sono disponibili i singoli record.




.. only:: html

.. figure:: ./_images/img_3231d.png
   :align: center

   :descrizione

Controllo automatico dei rapporti stratigrafici
--------------------------------------------------

Nella sezione Tools, selezionando uno scavo, è possibile eseguire il controllo sui rapporti stratigrafici.

Gli errori nell'inserimento delle US possono essere di vari tipi. Ecco elencate alcune casistiche:

1. tipo di rapporto fisico errato;
2. numero del rapporto errato;
3. tipo di rapporto e numero errati;

4. tipo di rapporto non inserito;
5. numero del rapporto non inserito;
6. tipo di rapporto fisico e numero non inseriti (equivale a non inserire il rapporto, dato che pyarchinit elimina il record vuoto nel campo rapporti);

7. tipo di rapporto non corrispondente con la definizione stratigrafica (Esempio: uno strato di argilla che taglia un muro);

8. rapporto tra 2 US che non hanno una sovrapposizione o adiacenza topografica che giustifichi il rapporto, sia in verticale che in orizzontale. Per esempio due strati che hanno i propri limiti a metri di distanza; uno strato individuato ad inizio scavo di spessore di pochi centimetri che copre un livello che si trova diversi metri più in basso;

9. reciproco non inserito. Esempio 1 copre 2, ma 2 non è coperto da 1. In realtà potrebbe dipendere da errori sopraelencati;

10. numero di US inserita nel rapporto che non corrisponde ad una scheda US.

11. US più antiche che ricevono un rapporto di sovrapposizione temporale rispetto ad US più recenti. Esempio: un muro di epoca romana che copre una pavimentazione medievale.

12. Medesimo rapporto fisico inserito nelle due US coinvolte: 1 copre 2, 2 copre 1.

Le casistiche sopradescritte dipendono in prevalenza da errori di immissione o banalmente di distrazione. E' stato osservato come in scavi da 30 US e circa 100 rapporti stratigrafici, in media emergano, anche dopo un ricontrollo autoptico, tra uno e 3-4 errori.

La strada scelta al momento da pyArchInit è quella di non correggere in automatico gli errori, dato che non è possibile evincere in automatico dove risieda l'errore. Per esempio potrei avere un problema di assenza di reciproci (caso 9), ma l'assenza potrebbe dipendere o da una dimenticanza nell'inserire i rapporti o da una effettiva non necessità di inserimento dovuta all'assenza di rapporti topografici (caso 8).

Per questi motivi  al momento viene generato un semplice report di testo in cui si segnala se la scheda corrispondente esiste (caso 10) o se il rapporto stratigrafico è rispettato (caso 9).

Riportiamo di seguito un esempio di controllo lanciato su uno scavo a fine giornata.
Vengono generati 2 report:

#. rapporti_us.txt: verifica sia i reciproci che l'assenza di schede US.

#. def_strat_a_rapporti_US.txt: verifica la concordanza tra il rapporto stratigrafico e la definizione stratigrafica.


I report sono esportati nella cartella pyarchinit_report_forlder che si trova sotto al vostro Utente e si chiama rapporti_us.txt :

rapporti_us.txt
Report controllo Rapporti Stratigrafici - Sito: Via Cignani, 18 Rimini
Sito: 'Via Cignani, 18 Rimini ', #Area: '1', #US: 2 Coperto da US: 15: Rapporto non verificato
Sito: 'Via Cignani, 18 Rimini ', #Area: '1', #US: 2 Taglia US: 16: Rapporto non verificato
Sito: 'Via Cignani, 18 Rimini ', #Area: '1', #US: 1007 Taglia US: 977: Scheda US non esistente
Sito: 'Via Cignani, 18 Rimini ', #Area: '1', #US: 256 Riempie US: 255: Scheda US non esistente

def_strat_a_rapporti_US.txt
Sito: 'Via Cignani, 18 Rimini ', #Area: '1', US: 128 - 'Riempimento': lo strato Si lega a US: 127 - 'Strato di argilla'


Il sistema funziona per una singola accoppiata Sito - Area di scavo. Per lanciarlo non è necessario fare una query, ma è stata creato un sistema con 2 liste a tendina, sito e area, nella sezione Tools (NB: cliccando sull'icona con la doppia scheda è possibie "staccare" la finestra e usarla in maniera indipendente dalla scheda US)


A questo punto basta selezionare Sito e Area di scavo e lanciare il comando Check Go!!!


A questo punto basta andare ad aprire i relativi files e iniziare a verificare i rapporti. E' possibile per fare questo anche tenersi aperto il matrix interattivo per disegnare le US su Qgis. Nell'esempio sotto riportato, Abbiamo verificato perchè il sistema ci riporta l'errore US6 Gli si appoggia US12. Accendendo su Qgis le US possiamo verificare che vi sia adiacenza topografica, quindi il rapporto è possibile, mentre aprendo la scheda US di US12, vediamo che è stato inserito il medesimo rapporto US12 Gli si appoggia US6. A questo punto solo l'archeologo è in grado di capire come risolvere il paradosso e da cosa può dipendere.



Esportazione del matrix di Harris
----------------------------------------------

È possibile realizzare dei diagrammi stratigrafici che espongano la successione stratigrafica di qualsiasi istanza del database dopo una ricerca. Il sistema esporta due formati: un'immagine raster in .png e un vettoriale .svg modificabile. L'aspetto del matrix ovviamente tende ad essere ordinato quante meno US sono presenti. Tuttavia un primo tentativo di migliorare l'aspetto del diagramma ottenuto è stato rappresentato dall'aggiunta del raggruppamento per insiemi delle US basate sulla periodizzazione.
Dopo aver realizzato una ricerca sulla scheda US cliccare sul pulsante “Export Matrix”. Il matrix viene salvato all'interno della cartella pyarchinit_Matrix_folder all'interno del vostro utente.

Nell'esempio seguente mostriamo due semplici passaggi per avere pianta di struttura e matrix in 2 semplici passaggi:

1. Nella scheda US con il visualizzatore delle geometrie attivo cerchiamo l'ED01 del nostro scavo. In automatico su Qgis appare la pianta e nelle schede US appaiono solo i record corrispondenti ad ED01.



2. Andare nella sezione Tools e cliccare su “Export Matrix”



3. Viene esportato il matrix in formato .png e .svg e si trovano all'interno della cartella pyarchinit_Matrix_folder sotto al vostro Utente.




I files possono essere gestiti sia tramite GIMP che Inkscape, mentre, seguendo il blog a questo indirizzo è possibile trasformare il Matrix in un grafico interattivo tramite Yed.

Vai alla pagina del Blog `a link`_.

.. _a link: http://pyarchinit.blogspot.it/2015/04/this-afternoon-im-thinking-about-issues.html



Creazione dell'indice di ordine di successione stratigrafica
--------------------------------------------------------------

L'indice di successione stratigrafica è stato ideato per poter ovviare alla visualizzazione del GIS, che sovrappone i poligoni in base al loro ordine di immissione all'interno del database.

L'algoritmo realizzato (al momento altamente in via di sviluppo) crea un ordine di successione stratigrafica basato sui rapporti stratigrafici. Ogni US assume un valore univoco in base alla sua posizione nella stratigrafia e dai rapporti che ha con altre US.
Per esempio, se 1 copre 2, 2 copre 3 e 4, ma 3 e 4 non hanno rapporti tra di loro lo script genererà i seguenti valori:

.. table::

    === ============== ====================================
    US  Rapporto       Ordine di successione stratigrafica
    === ============== ====================================
    1	Copre 2   	   0
    2   Copre 3 e 4    1
    3   Coperto da 2   2
    4   Coperto da 2   3
    === ============== ====================================


Questo permetterà alla View SQL di visualizzare su base GIS le geometrie degli strati nel loro ordine stratigrafico originario, senza doversi preoccupare delle modalità di disegno delle US.


Il sistema funziona per singola Area di scavo. Quindi è necessario prima di tutto eseguire una ricerca che richiamo solo un'area di scavo di un sito. Dopo aver cliccato su nuova ricerca, basta inserire nome del sito e numero di Area.




A questo punto sarà necessario nella sezione Tools cliccare su “Ordine Stratigrafico”.


NOTA BENE: Il sistema funziona solo se due condizioni sono verificate
* Assenza di errori nell'inserimento dei rapporti stratigrafici
* Accordo con il valore di loop che esegue il software in fase di analisi dell stratigrafia. Questo è un parametro tecnico ed è settato a livello di codice su 500 Loop; questo implica che una singola US, per ogni singolo rapporto, viene scansionata 500 Volte. Se una US ha più di 500 rapporti, è possibile che il sistema non riesca a completare il ciclo. Al momento è stata testata su scavi aperti di estensione sotto gli 800 mq e in contesti urbani complessi e il sistema ha sempre funzionato. Se si riscontrassero problema, ovvero il sistema non esce dal loop, è necessario modificare il parametro nel codice in python. Dato che dai loop dipende anche la velocità di esecuzione, in futuro si potrebbe aggiungere una casella dove si setta manualmente il numero di loop massimo per singola US. Va considerato che per un pacchetto di circa 40 US in ambito urbano, il sistema richiede circa un minuto di lavoro, che aumenta progressivamente all'aumentare delle US e dei rapporti inseriti.

Il sistema manda invia all'utente una serie di messaggi (utilizzati per il debug del sistema), tra cui la richiesta di eseguire il matrix per verificare eventuali paradossi nella stratigrafia come US più antiche che coprono US più recenti.







Lanciando il matrix sarà possibile verificare la correttezza dei rapporti tramite l'immagine esportata nella cartella pyarchinit_Matrix_folder che si trova sotto al vostro Utente, e richiamare dal Matrix interattivo le US cliccando sul singolo numero, per poter verificare sovrapposizioni corrette, a quale US si fa riferimento, ecc..




Al messaggio "Inizio Sistema order layer" dare OK; "Uscita dal sistema order layer", dare OK ed attendere, senza impegnare il PC in altre operazioni. A volte possono servire anche 15 minuti per grandi scavi ( ma ne vale la pena!!!).

E' necessario attendere il messaggio "SISEMA DI ORDINAMENTO TERMINATO".




ATTENZIONE!!! Per motivi prettamente informatici, il sistema ricarica tutte le US del Database. Richiamate il vostro set di dati.


Se qualcosa fosse andato storto e per essere sicuri che il vostro scavo sia documentato in maniera corretta, è possibile verificare una serie di report che vengono estratti dal sistema di ordinamento. Si trovano all'interno di pyArchinIt Report_Folder sotto al vostro Utente.




Ecco come appare il layer di inserimento delle Unità Stratigrafiche (pyunitastrigrafiche) alla fine della digitalizzazione di tutte le US.



Ecco Il layer di visualizzazione delle Unità Stratigrafiche (pyarchinit_us_view) dopo la generazione dell'ordine stratigrafico pronto per essere esportato.




PROBLEMI NOTI: se si lancia il comando e sono presenti paradossi è possibile che il sistema non riuscendo a risolverli vada avanti all'infito. Oppure se si lancia il sistema su più Aree di uno scavo o su più scavi, il sistema va in loop e non c'è modo di abortire il processo. In tutti questi casi è necessario forzare l'arresto di Qgis.

Esportazione schede e indice delle US in formato PDF
-----------------------------------------------------

È possibile esportare sia le singole schede che l'indice delle US basandosi su qualsiasi ricerca o criterio di ordinamento. Alcuni dati vengono presi direttamente dalla us_table, mentre altri, come la quota minima e massima, sono ricavati per relazione dalle features dei layers.

Le modalità per esportare le schede sono molteplici. E' possibile fare una ricerca in scheda, oppure una ricerca sui layer in Qgis e visualizzare le US corrispondenti in scheda ed esportarle. I criteri di esportazione sono pressochè illimitati, potendo cercare su vari campi ed ordinare le schede in base a più modalità. Per esempio si potrebbero cercare tutte le schede relative al Medioevo ed esportare tutte le US ordinate per scavo e tipo di defizione. Un medesimo set di dati può essere esportato secondo ordinamenti differenti, dando la possibilità di creare elenchi consultabili secondo vari criteri.

Nell'esempio sottostante abbiamo cercato in scheda l'ED01 di un nostro scavo, selezionato a video le US che ci interessavano e aperto le schede US. Infine le abbiamo ordinate per numero di US.





Ora basta andare in sezione Tools -> Esportazione ed esportare Schede e Indice.

