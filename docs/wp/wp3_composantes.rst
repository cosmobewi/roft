WP3 — Exhaustivité RG : g₀₀, gᵢⱼ, g₀ᵢ
=====================================

But
---
Vérifier que la traduction "champ d’horloges" :math:`R(x)=d\tau/dt`
recouvre bien **tous** les tests classiques de la relativité générale
et donc reste compatible avec l’axiome « gravité = modulation ».

Définition générale
-------------------
.. math::

   R(x) = \frac{1}{c}\,\sqrt{-\,g_{00} - 2 g_{0i}\frac{dx^i}{dt} - g_{ij}\frac{dx^i}{dt}\frac{dx^j}{dt}}.

Composantes à prendre en compte
-------------------------------

g_{00} — Potentiel gravitationnel
*********************************
- Responsable du redshift gravitationnel.  
- Suffit pour expliquer : Pound–Rebka, GPS (partie gravité), horloges à différentes altitudes.  
- **Lecture rythme** : ralentissement global des horloges (tempo modulé par la profondeur du potentiel).

g_{ij} — Courbure spatiale
**************************
- Nécessaire pour obtenir la bonne valeur de la déviation de la lumière par le Soleil.  
- En simple Newtonien (seulement g_{00}), on trouve un angle moitié trop petit :  

  .. math::

     \alpha_{Newton} \simeq \frac{2GM}{c^2 b}
     \qquad\text{vs.}\qquad
     \alpha_{RG} \simeq \frac{4GM}{c^2 b}.

- **Lecture rythme** : la structure spatiale impose une cohérence supplémentaire dans les battements → la lumière suit des “lignes de rythme” incurvées.

Observation confirmée par Eddington (1919) et toutes les lentilles gravitationnelles modernes.

g_{0i} — Gravitomagnétisme
**************************
- Apparaît quand la source est en rotation (cadre non statique).  
- Effets : Sagnac, Lense–Thirring, frame dragging.  
- Confirmés par Gravity Probe B, LAGEOS.  
- **Lecture rythme** : la rotation entraîne une modulation différentielle des horloges selon la direction (flux de tempo).  

Formule test :  

.. math::

   \vec{\Omega}_{LT} \;\simeq\; \frac{2G}{c^2 r^3}\,\vec{J}.

Exemple : pour LAGEOS autour de la Terre, la précession est de l’ordre de 31 milliarcsecondes/an.

Résumé dictionnaire
-------------------
.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Composante
     - Effet rythmique
     - Tests expérimentaux

   * - g_{00}
     - Ralentissement global des horloges
     - Pound–Rebka, GPS, horloges atomiques

   * - g_{ij}
     - Cohérence spatiale des flux de rythme
     - Déviation lumière (Eddington), périhélie de Mercure, lentilles

   * - g_{0i}
     - Flux de tempo dû aux rotations
     - Sagnac, Lense–Thirring (LAGEOS, GP-B)

Conclusion 
----------
Pour respecter **tous les tests classiques de la RG**, le champ d’horloges :math:`R(x)` doit inclure :

- g_{00} (potentiel)  
- g_{ij} (courbure spatiale)  
- g_{0i} (gravitomagnétisme)

**Lecture rythme** : la gravité ne se résume pas à ralentir les horloges,
mais aussi à organiser leurs **flux de battement** dans l’espace et sous l’effet des rotations.