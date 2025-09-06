WP19 — Gravité faible et synchronie (binaires larges)
=====================================================

Contexte observationnel
-----------------------

Les données de la mission **Gaia** (ESA) sur plus de 26 000 systèmes
d'étoiles binaires larges (séparation ~0.01–1 pc) montrent
des vitesses orbitales **30 à 40 % supérieures** aux prédictions
newtoniennes/relativistes classiques
dans le régime des **accélérations ultra-faibles**
(~10^-11 m s^-2). [Chae 2023–2025].

Ces excès persistent après contrôle instrumental et statistique.
Ils alimentent l'hypothèse d'une **gravité modifiée (MOND)**,
mais la ROFT propose une lecture alternative.

---

Lecture ROFT
------------

En **ROFT**, la gravité est lue comme une **modulation de rythme**.
Quand l'accélération devient très faible, les horloges des deux masses
ont tendance à être **plus synchrones avec le fond** :
le **contraste temporel** diminue, ce qui modifie la lecture orbitale.

On encode cela par un **facteur de synchronie** :math:`S(a)` appliqué
à la vitesse newtonienne :

.. math::

   v_{\rm ROFT}(r) \;=\; v_{\rm N}(r)\,\times\,S(a_{\rm N}(r))

avec :math:`a_{\rm N}(r)=GM/r^2`.

---

Forme effective du facteur
--------------------------

Pour retrouver l'ordre de grandeur mesuré (+30–40 %), on pose :

.. math::

   S(a) \;\approx\; \left(\frac{a_0}{a}\right)^{1/4},
   \quad a_0\simeq 1.2\times 10^{-10}\,\text{m s}^{-2}.

Ce qui donne :

- à :math:`a\simeq 4\times 10^{-11}` → :math:`S\simeq 1.32` (+32 %)  
- à :math:`a\simeq 3\times 10^{-11}` → :math:`S\simeq 1.41` (+41 %)

Pile dans la gamme observée par Gaia.

---

Conséquence conceptuelle
------------------------

- **RG + Newton** restent exactes dans leur domaine.  
- La ROFT n’ajoute pas une “nouvelle force”, mais un
  **facteur de synchronie temporelle** applicable uniquement
  aux régimes faibles.  
- L’effet se manifeste par une augmentation de vitesse orbitale
  mesurable, exactement comme vu dans Gaia.  

---

Résumé
------

Le WP19 montre que la ROFT :

- retrouve les excès de 30–40 % dans les binaires larges,  
- avec une interprétation simple : **synchronie partielle des horloges**,  
- et sans ajouter de champs exotiques ni casser Einstein/Newton.  

Une piste claire pour tester la ROFT par confrontation directe
aux données observationnelles.

.. seealso::

   - :doc:`wp19_details`