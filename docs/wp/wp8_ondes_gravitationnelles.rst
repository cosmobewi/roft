.. _wp8_ondes_gravitationnelles:

WP8 — Ondes gravitationnelles en lecture rythme
===============================================

But
---
Montrer que les ondes gravitationnelles sont des **oscillations collectives du rythme des horloges**,
et non une « force » qui se propage dans un support matériel.

Formulation standard (RG)
-------------------------
- En relativité générale, les ondes gravitationnelles sont des **perturbations de la métrique** :math:`g_{\mu\nu}`.  
- Observable : variation périodique des distances entre masses tests.  
- LIGO/Virgo mesurent un **strain** :math:`h \sim \Delta L / L`.  
- Effet : les bras de l’interféromètre s’allongent et se raccourcissent alternativement.

Formulation rythme (ROFT)
-------------------------
- Champ des horloges :  

  .. math::

     R(x) = \frac{d\tau}{dt}

  oscille périodiquement sous l’effet de l’onde.  

- Deux horloges éloignées voient leur rythme **se déphaser alternativement** :  
  → différence de battement → signal détecté.  

- Pas besoin d’un « support » qui se déforme :  
  c’est une **désynchronisation rythmique propagée**.

Exemple simple (approximation linéaire)
---------------------------------------
Onde polarisée + se propageant en z :

.. math::

   ds^2 = -c^2 dt^2
   + (1+h\cos\omega t)\,dx^2
   + (1-h\cos\omega t)\,dy^2
   + dz^2.

- Lecture standard : la métrique oscille.  
- Lecture rythme : les tempos locaux :math:`R(x)` des horloges placées sur x et y
  battent **hors phase**, d’où le contraste mesurable.

Conséquences
------------
- **LIGO/Virgo** : mesure d’un **contraste rythmique différentiel**.  
- **ROFT** : onde = propagation d’une **désynchronisation des horloges**.  
- Pas besoin de postuler un « graviton » comme quantum de champ perturbatif :  
  les ondes sont déjà décrites comme des **modulations collectives globales**.

Résumé
------
- **En RG** : onde = perturbation de la métrique.  
- **En ROFT** : onde = propagation d’un **contraste de rythme**.  
- Les deux lectures sont cohérentes, mais la ROFT rend l’intuition plus tangible :  

  **l’espace ne se déforme pas, ce sont les horloges qui battent à contretemps.**

.. seealso::

   - Référence : `Gravitational wave <https://en.wikipedia.org/wiki/Gravitational_wave>`_  
   - Autres WP : :doc:`wp/wp5_composantes_RG`, :doc:`wp/wp4_exemples_calc`
