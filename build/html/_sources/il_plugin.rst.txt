.. image:: ./_images/logo_3.png
   :align: right
   
2 Il Plugin
--------------------------------

Il progetto pyArchInit nasce nel 2005 per la sperimentazione dell'uso del Free Open Source Software
(d'ora in poi citato come FOSS) in campo archeologico.

Il progetto, portato avanti in maniera indipendente e al di fuori dell'uso commerciale, ha potuto fin dall'inizio
sperimentare forme di sviluppo multidirezionali e metodologiche, nei software utilizzati, nei soggetti coinvolti e
negli oggetti di elaborazione, libero dalle pressioni che un progetto legato al business può avere.
pyArchInit è uno dei pochi progetti software FOSS dedicati ai Beni culturali, in cui del codice è scritto ex novo per
permettere ai professionisti del settore di sfruttare le potenzialità dell'informatica nel settore.

Va tenuta in considerazione inoltre la scarsa circolazione di denaro intorno allo sviluppo di nuove metodologie e
strumenti di lavoro per chi opera nelle cosiddette scienze umanistiche, spesso ancora identificate dal mercato come
insieme di studi settoriali fini a se stessi, legate a studi di ricerca di tipo universitario, che poco possono avere
con le problematiche lavorative al di fuori dell'ambito accademico.

Il basso investimento di risorse economiche unitamente ad una labile visibilità degli introiti ricavabili da simili
progetti, ha fatto sì che presso gli Enti universitari si sviluppassero soprattutto modalità di utilizzo di software,
proprietario e non, nati per scopi differenti ed impiegati per i propri bisogni; in alcuni casi si è dato vita ad uno
sviluppo di strumenti tecnologici creati ad hoc per l'archeologia, ma che spesso rimangono relegati all'interno
dell'Ateneo che li ha concepiti, soprattutto per motivi di diffusione delle licenze nel caso di software proprietario,
o per la difficoltà nella divulgazione del proprio metodo, qualora siano stati applicati software FOSS. Risultano infine
altamente rari quei contesti in cui gli sviluppatori degli strumenti per i Beni culturali siano direttamente dei
professionisti del settore, che creano le proprie soluzioni personalizzate senza l'intermediazione di informatici.

pyArchInit è un software FOSS, che si appoggia a sua volta su software FOSS, progettato e scritto da professionisti,
con codice sorgente aperto e ridistribuito liberamente all'esterno della comunità di sviluppo.


2.1 Struttura plugin
________________________________

Il plugin è stato studiato per avere una struttura flessibile in cui ogni parte può essere sostituita, riparata o
implementata in maniera abbastanza semplice. Di seguito mettiamo uno schema della struttura per permettere un’individuazione
rapida dei singoli componenti.

Provare a spiegare come sia il flusso dei dati per ogni file o per ogni funzione sarebbe ridondante e rimandiamo ad una
altra sede le spiegazioni tecniche di come funziona il plugin.


2.2 Toolbar
________________________________

Breve introduzione valida per tutte le schede contrassegnate nel riquadro rosso.
Inoltre ogni scheda, ha nella toolbar, alcune funzioni specifiche per quella scheda, ma verranno tratte nell paragrafo 3
"Le Schede"

.. image:: ./_images/toolbar.jpg
   :align: center

La parte alta di tutte le schede è dedicata alla pulsantiera per navigare tra i records del database: a sinistra è
presente la pulsantiera per andare avanti e indietro tra i records, aggiungere una nuova scheda, salvare il record,
eliminare, ricercare, ordinare e mostrare tutti i records, oltre ad un pulsante di “emergenza” per ricaricare il database.

I primi 4 pulsanti, guardandoli da sinistra verso destra, caratterizzati da una freccia verde, permettono di andare al
primo record o indietro di 1 record, di navigare al record successivo o visualizzare l’ultimo. NB: NELLA CASELLA REC STEP
è possibile decidere di quanti record avanzare o tornare indietro usando le frecce singole. FUNZIONE DISPOBILE AL MOMENTO
SOLO PER LA SCHEDA US.

Il pulsante con la scheda bianca e una piccola penna sopra serve a mettere l’interfaccia in modalità nuovo record.
Per salvare la creazione di un nuovo o una modifica apportata ad un record esistente cliccare sull’icona col dischetto.
Per eliminare il record corrente cliccare sul pulsante con foglio bianco barrato da una X rossa.
Tramite il pulsante con la lente di ingrandimento e new è possibile mettere la scheda in modalità di ricerca, e dopo
aver inserito i parametri, lanciare la ricerca dal pulsante successivo con lente di ingrandimento e search. La lente di
ingrandimento singola serve a visualizzare tutti i record presenti in una tabella.

Il pulsate con scheda bianca apre una finestra di dialogo per impostare l’ordinamento dei dati.

Nella parte sinistra sono presenti i criteri di ordinamento. Selezionandone uno è possibile, con le frecce posizionate
al centro, spostarli nella parte destra per utilizzarli come criteri di ordinamento scegliendo un ordine ascendente o
discendente. Cliccando su Ordina, sarà possibile visualizzare la nostra istanza di database secondo i criteri scelti.

ATTENZIONE SE NON SI IMPOSTA ALMENO UN TIPO DI ORDINAMENTO E SI ESCE LA SCHEDA DA UN ERRORE CHE SI PUO’ IGNORARE.
Nella parte destra è possibile controllare lo stato del database: in uso, in modalità ricerca o inserimento di un nuovo
record . Viene segnalato se il set di records ricercati è ordinato o meno, il numero del record corrente e il numero di
records totali consultabili. Il numero di record totali si riferisce alla cosiddetta “istanza di database”, ovvero non
necessariamente a tutti i record presenti nella tabella, ma al complesso di record richiamati dal database, che può
ovviamente variare da uno a molti oppure tutti, a seconda della ricerca impostata. La modalità “usa” si riferisce al
momento in cui è possibile consultare oppure modificare i record. L’ordinamento ci informerà se l’istanza di database è
stata ordinata in base ad un criterio, mentre il numero del record, corrisponde alla posizione del record visualizzato
in base all’istanza di database e al criterio di ordinamento scelto.