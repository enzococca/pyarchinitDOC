**************
Linee guida
**************

Per fare un titolo::

    Titolo
    ******
    puoi iniziare a scrivere qui




.. _ancora_il_capitolo:

per fare un capitolo::

    capitolo
    ========

    .. _ancora_il_capitolo:

    puoi iniziare a scrivere qui

.. note::
    '.. _ancora_il_capitolo:' serve per ancorare un capitolo alla pagina

    vedi  :ref:`riferimento capitolo e note <rif>`


per fare una sezione::

    sezione
    -------
    puoi iniziare a scrivere qui


per fare una sottosezione::

    sottosezione
    ++++++++++++
    puoi iniziare a scrivere qui

per fare un paragrafo::

    paragrafo
    ^^^^^^^^^
    puoi iniziare a scrivere qui

**Enfasi:**::

    *corsivo*

    **bold**

*corsivo*

**bold**

**Elenchi**::

    elenco puntato

    * a
    * b

    elenco numerato

    #. a
    #. b

elenco puntato

    * a
    * b

elenco numerato

    #. a
    #. b

**Costruire una tavola:**::

    .. _table:

    +-----+-------+------+
    |titolo             |
    +-----+-------+------+
    |1             3     |
    +-----+-------+------+
    |A    |   B   |  C   |
    +-----+-------+------+

    Oppure:

    ===     ===     ===
    A       B       C
    ===     ===     ===
    1       AS      CC
    2
    ===     ===     ===

.. _table:

    +-----+-------+------+
    |titolo              |
    +-----+-------+------+
    |1             3     |
    +-----+-------+------+
    |A    |   B   |  C   |
    +-----+-------+------+

    Oppure:

    ===     ===     ===
    A       B       C
    ===     ===     ===
    1       AS      CC
    2
    ===     ===     ===

.. _rif:

**riferimenti a capitoli e note**::


    vedi capitolo ancora_il_capitolo_.

vedi capitolo ancora_il_capitolo_.



**Note a piè di pagina:**::

    scrivi qualcosa che dovrà andare come nota a piè di pagina [#]_

    .. [#] questa è la nota apiè di pagina.

scrivi qualcosa che dovrà andare come nota a piè di pagina [#]_

    .. [#] questa è la nota apiè di pagina.

**Inserisci le figure e le immagini**

Le figure e le immagini  vanno salvate nella cartella ./_images

*per inserire una immagine*::


        .. image:: ./_images/pyarchinit_logo.png
            :width: 10 cm
            :align: center

.. image:: ./_images/pyarchinit_logo.png
    :width: 10 cm
    :align: center

*per inserire una figura*::

        .. _figura_[#]:

        .. only:: html


        .. figure:: ./_images/pyarchinit_logo.png
            :width: 10 cm
            :align: center

            : Logo Pyarchinit.

.. _figura_[#]:

.. only:: html


.. figure:: ./_images/pyarchinit_logo.png
    :width: 10 cm
    :align: center

    : Logo Pyarchinit.

**Aggiungere note , warning, error, tips, important**

*aggiungere nota*::

    .. note::
        scrivo qualcona nella nota

.. note::
    scrivo qualcosa nella nota

*aggiungere warning*::

    .. warning::
        scrivo qualcona nel warning

.. warning::
    scrivo qualcosa nel warning

*aggiungere error*::

    .. error::
        scrivo qualcona nell'error

.. error::
    scrivo qualcosa nell'error


*aggiungere tips*::

    .. tip::
        scrivo qualcona nel tip

.. tip::
    scrivo qualcosa nel tips


*aggiungere qualcosa d'importante*::

    .. important::
        scrivo qualcona in important

.. important::
    scrivo qualcosa in important

