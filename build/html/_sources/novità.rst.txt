.. image:: ./_images/logo_3.png
   :align: right
   
Novità
***********************************************

I cambiamenti che hanno interessato la nuova release di pyArchInit sono:

    *Scheda Print Map*

    *Scheda Impacchetta per Geopackage*

    *Funzione MeveCost*

    *Funzione conversione in Spatialite 5*

    *Funzione importazione layer vettoriali*

    *Raggruppamenti Layer*

    *WMS vincoli archeologici filtrati per comune*

    *WFS Toponomastica, WMS IGM 25000, WMS catasto e BaseMap(Google e Wikimidia)*

    *Cambio colore del background delle schede*

    *Inserimento layer stratigrafia verticale*

    *Geocoding: ricerca indirizzi*

    *Harris Matrix per Extended Matrix*

    *Totalopenstaion2pyarchinit*

    *Controllo rapporti stratigrafici*

    *Inserimento rapporti inverso*

.. note::
    Queste nuove caratteristiche sono state inserite tra il 2021 e il 2022

**************************************************************************



Scheda Print Map
====================================
.. image:: ./_images/print_map.png
   :align: center

La scheda Print Map nasce con l'intento di facilitare e automatizzare l'esportazione  delle mappe di scavo o survey, al
fine di redigere, in modo standarzizzato la documentazione. La scheda si presenta con dei template pronti all'uso in
differenti formati e scale di visualizzazione. Inoltre sono abilitate a prendere le info dal db di pyarchinit. Questa
scheda permette anche di personalizzare e creare nuovi template. Per approfondimenti si rimanda alla sezione **Schede
plugin**.




**************************************************************************

Scheda Impacchetta per Geopackage
================================= 
.. image:: ./_images/gpkg.png
   :align: center

Questa scheda permette di impacchettare i layer selezionati  nel Layer panel(sia vettori che raster) in un file Geopackage.
Per il funzionamento e maggiori dettagli si rimanda alla sezione **Schede Plugin**


   

**********************************************************************************

Funzione MeveCost
================= 
.. image:: ./_images/movecost.png
   :align: center

Questa Funzione permette di fare analisi di costo sul territorio importando un dtm oppure facendolo scaricare automaticamente in base all'area d'interesse.
Fornisce la possibilità di calcolare la superficie non isotropa dei costi accumulati, i percorsi meno costosi e i corridoi meno costosi usando una serie di 
funzioni di costo relative al movimento umano che possono essere selezionate dall'utente. Richiede solo un modello digitale del terreno, una posizione 
iniziale e (opzionalmente) una posizione di destinazione.Per il funzionamento e maggiori dettagli si rimanda alla sezione Funzioni


**************************************************************************

Funzione conversione in Spatialite5
===================================
.. image:: ./_images/toolbox.png
   :align: center

Questa funzione permette di convertire un db spatialite 3 o 4 di pyarchinit in spatialite 5
Per il funzionamento e maggiori dettagli si rimanda alla sezione Funzioni


   

**************************************************************************

Funzione importazione layer vettoriali 
====================================== 

La nuova struttura *Importazione Dati* all'interno dei DB di pyarchinit è stata migliorata. Ora è possibile
importare anche le geometrie e sono visuaizzate in automatiche il nome dei campi e l'attributo.




**************************************************************************

Raggruppamenti Layer
====================
.. image:: ./_images/Layer_plus.png
   :align: center

Dalla scheda Sito quando vengo richiamati i layer per disegnare , essi sono raggruppati e ordinati in gruppi nel layer panel



**************************************************************************



WMS vincoli archeologici filtrati per comune
============================================
.. image:: ./_images/radar.png
   :align: center

Dalla scheda sito si può richiamare il wms dei vincoli in rete sula base del comune di apparteneza



**************************************************************************


WFS Toponomastica, WMS IGM 25000, WMS catasto e BaseMap(Google e Wikimidia)
===========================================================================
.. image:: ./_images/basemap.png
   :align: center

Dalla scheda sito si possono richiamare il wfs toponomastica ricavato dal IGM 25000, il wms igm 25000,wms catastale e
due basemap di Google e Wikimidia



**************************************************************************


Cambio colore del background delle schede
========================================== 
é stato cambiato il background delle schede per una migliore visualizzazione

**************************************************************************


Inserimento layer stratigrafia Verticale
=========================================
In questa nuova versione sono stati inseriti due nuovi layer che gestiscono la startigrafia verticale:
*pyunitastratigrafiche_usm* e *pyquote_usm*. Essi hanno anche delle view indipendenti che possono essere richiamate dalla
scheda US-USM


**************************************************************************

Geocoding: ricerca indirizzi
=========================================
Nella scheda Sito è stato aggiunto una barra di ricerca d'indirizzi sulla base di OpenStreetMap.
una volta ricercato l'idirizzo desiderato, verrà aggiunto un layer puntuale nel map canvas



**************************************************************************

Harris matrix per Extended Matrix Tool
=========================================
questa nuova funzione permette di esportare un matrix di Harris in un graphml gestibile con yED ed è associato ad un template
il graphml prodotto è compatibile con l'Extended Matrix Tool



**************************************************************************

Totalopenstation2pyarchinit
=========================================
.. image:: ./_images/tops.png
   :align: center

Questa scheda permette d'importare i dati grezzi di diverse stazioni totali nei layer pyrchinit_quote, pyarchinit riferimenti
e pyarchinit campionature

Controllo rapporti stratigrafici
======================================

Sono state inserite nuovi tipi di controllo per i rapporti stratigrafici, in particolare la funzione controlla anche
sulla base del periodo e dell'unità tipo


Funzione inserimento rapporti stratigrafici inverso
===================================================

L'utente potrà scegliere durante l'inserimento dei rapporti stratigrafici, se vorrà inserire il rapporto inverso.
Questa funzione ha tre particolarità:

    #. crea una nuova scheda se la scheda non esiste ed inserisce il rapporto inverso

    #. se la scheda esiste ma non esiste il rapporto inverso, verrà aggiungto

    #. se la scheda esiste e anche il rapporto inverso, il rapporto inverso verrà aggiornato