===================================================
WP5 — Composantes nécessaires pour tous les tests RG
===================================================

But
===
Vérifier que la traduction "champ d’horloges" :math:`R(x)=d\tau/dt` recouvre bien **tous** les tests classiques de la relativité générale.

Définition générale
===================
.. math::

   R(x) = \frac{1}{c}\,\sqrt{-\,g_{00} - 2 g_{0i}\frac{dx^i}{dt} - g_{ij}\frac{dx^i}{dt}\frac{dx^j}{dt}}.

Composantes à prendre en compte
===============================

1) g_{00} — Potentiel gravitationnel
------------------------------------
- Responsable du redshift gravitationnel.  
- Suffit pour expliquer les expériences : Pound–Rebka, GPS (partie gravité), horloges à différentes altitudes.  
- **Lecture rythme** : ralentissement global des horloges (tempo modulé par la profondeur du potentiel).

2) g_{ij} — Courbure spatiale
------------------------------
- Nécessaire pour obtenir la bonne valeur de la déviation de la lumière par le Soleil.  
- En simple Newtonien (seulement g_{00}), on trouve un angle moitié trop petit.  
- **Lecture rythme** : la structure spatiale impose une cohérence supplémentaire dans les battements → la lumière suit des “lignes de rythme” incurvées.

Formule test : déviation lumière
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. math::

   \alpha \;\simeq\; \frac{4GM}{c^2 b},

où b = distance minimale d’approche.  
Observation confirmée par Eddington (1919).

3) g_{0i} — Gravitomagnétisme
------------------------------
- Apparaît quand la source est en rotation (cadre non statique).  
- Effets : Sagnac, Lense–Thirring, frame dragging.  
- Confirmés expérimentalement par Gravity Probe B, LAGEOS.  
- **Lecture rythme** : la rotation entraîne une modulation différentielle des horloges selon la direction (flux de tempo).

Formule test : précession de Lense–Thirring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. math::

   \vec{\Omega}_{LT} \;\simeq\; \frac{2G}{c^2 r^3}\,\vec{J},

où J = moment cinétique de la Terre.

Résumé dictionnaire
===================
- g_{00} → ralentissement gravitationnel (tests : GPS, Pound–Rebka, horloges atomiques).  
- g_{ij} → déviation de la lumière, avance du périhélie (tests : Mercure, lentilles gravitationnelles).  
- g_{0i} → effets de rotation (tests : Sagnac, Lense–Thirring).

Conclusion WP5
==============
Pour respecter **tous les tests classiques de la RG**, le champ d’horloges :math:`R(x)` doit inclure :  
- g_{00} (potentiel)  
- g_{ij} (courbure spatiale)  
- g_{0i} (gravitomagnétisme)

**Lecture rythme** : la gravité ne se résume pas à ralentir les horloges, mais aussi à organiser leurs **flux de battement** dans l’espace et sous l’effet des rotations.
