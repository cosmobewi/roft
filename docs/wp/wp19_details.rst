.. _wp19_details:

Annexe — Cheminement détaillé du WP19
=====================================

Objectif
--------

Expliquer pas à pas comment la **ROFT** interprète les vitesses
excessives (+30–40 %) observées dans les binaires larges
par Gaia, en régime de gravité ultra-faible.

---

1) Point de départ classique
----------------------------

Pour un système binaire de masse totale :math:`M`
et séparation :math:`r`, l’orbite quasi-circulaire
se calcule en newtonien/relativiste faible champ par :

.. math::

   v_{\rm N}(r) = \sqrt{\tfrac{GM}{r}}, \qquad
   a_{\rm N}(r) = \tfrac{GM}{r^2}.

---

2) Observation Gaia
-------------------

Les données sur plus de 26 000 systèmes montrent :

- Pour des accélérations :math:`a\sim 3-4\times 10^{-11}\,\text{m s}^{-2}`
- Les vitesses orbitales sont **30–40 % plus grandes**
  que la prédiction :math:`v_{\rm N}`.

Ces excès persistent après correction des biais instrumentaux.

---

3) Lecture ROFT
---------------

En **ROFT**, la gravité est lue comme une **modulation de rythme** :

- Aux fortes accélérations, les horloges sont fortement désynchronisées
  → :math:`S(a)\to 1` → Newton/RG suffisent.  
- Aux faibles accélérations, les horloges tendent à se synchroniser
  → le **contraste de rythme** diminue
  → la vitesse mesurée est amplifiée.

On introduit un **facteur de synchronie** :math:`S(a)` :

.. math::

   v_{\rm ROFT}(r) = v_{\rm N}(r)\,\times\,S(a_{\rm N}(r)).

---

4) Forme pratique du facteur
----------------------------

Par analogie avec la loi empirique MOND (Milgrom 1983),
on propose :

.. math::

   S(a) \simeq \left(\tfrac{a_0}{a}\right)^{1/4},
   \quad a_0\simeq 1.2\times 10^{-10}\,\text{m s}^{-2}.

- Si :math:`a\gg a_0` → :math:`S\to 1` → régime classique.  
- Si :math:`a\ll a_0` → :math:`S>1` → excès mesurable.  

---

5) Exemple numérique
--------------------

Prenons :math:`M=2\,M_\odot`.

- Pour :math:`r=2.99\times 10^{15}\,\text{m}` (20 000 UA) :  

  - Newton :
    :math:`v_{\rm N}=0.298\,\text{km/s}`,  
    :math:`a_{\rm N}=3.0\times 10^{-11}\,\text{m/s}^2`.

  - ROFT :
    :math:`S(a)=\left(\tfrac{1.2\times10^{-10}}{3.0\times10^{-11}}\right)^{1/4}\approx 1.41`,  
    donc :math:`v_{\rm ROFT}=0.42\,\text{km/s}`.  

  → **Excès = +41 %**.

- Pour :math:`r=2.58\times 10^{15}\,\text{m}` (17 200 UA) :  

  - Newton :
    :math:`v_{\rm N}=0.327\,\text{km/s}`,  
    :math:`a_{\rm N}=4.0\times 10^{-11}\,\text{m/s}^2`.  

  - ROFT :
    :math:`S(a)\approx 1.32`,  
    donc :math:`v_{\rm ROFT}=0.43\,\text{km/s}`.  

  → **Excès = +32 %**.

Ces valeurs reproduisent exactement les anomalies rapportées.

---

6) Conséquence
--------------

- La **RG et Newton** restent valides dans leur domaine (forte accélération).  
- L’excès observé en faible champ est interprété comme
  une **synchronie partielle des horloges**.  
- Pas besoin d’introduire de champs exotiques :
  la correction découle directement de la lecture rythmique.  

---

Résumé
------

La ROFT explique les observations Gaia en insérant un simple
facteur de synchronie dans les vitesses newtoniennes.
Ce facteur, fondé sur l’idée que *le temps perçu est une différence
de rythme*, donne exactement les +30–40 % observés.
