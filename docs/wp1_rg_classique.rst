===============================
WP1 — RG classique en langage "rythme"
===============================

1. Temps propre : la règle du tempo
===================================
Une horloge locale mesure son temps propre :

.. math::

   d\tau \;=\; \frac{1}{c}\,\sqrt{-\,g_{\mu\nu}\,dx^\mu dx^\nu}.

- **Lecture standard** : longueur de la ligne d’univers.
- **Lecture rythme** : cadence du métronome interne (horloge de Compton) modulée par la géométrie.


2. Limite faible champ (approximation Newtonienne)
==================================================
Métrique statique, faible champ :

.. math::

   g_{00} \simeq -\Big(1 + \frac{2\Phi}{c^2}\Big),
   \qquad \Phi(r) = -\,\frac{GM}{r}.

Alors :

.. math::

   \frac{d\tau}{dt} \;\simeq\; 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}.

- **Lecture standard** : dilatation du temps (gravité + vitesse).  
- **Lecture rythme** : le potentiel \Phi ralentit le métronome, la vitesse v ajoute une désynchronisation.


3. Équation de Poisson (Newton comme limite de RG)
==================================================
Depuis Einstein :

.. math::

   G_{00} = \frac{8\pi G}{c^4}T_{00},\qquad T_{00}\simeq \rho c^2.

On obtient :

.. math::

   G_{00} \approx \frac{2}{c^2}\,\nabla^2 \Phi
   \;\Rightarrow\;
   \boxed{\;\nabla^2\Phi = 4\pi G \rho\;}.

- **Lecture standard** : équation de Newton pour le potentiel.  
- **Lecture rythme** : la densité de matière fixe la carte des tempos locaux.


4. Redshift gravitationnel
==========================
Deux observateurs statiques comparent leurs horloges :

.. math::

   \frac{\nu_2}{\nu_1}
   = \sqrt{\frac{-g_{00}(1)}{-g_{00}(2)}}.

Faible champ :

.. math::

   \frac{\Delta\nu}{\nu} \;\simeq\; -\,\frac{\Delta\Phi}{c^2}.

- **Lecture standard** : fréquence décalée.  
- **Lecture rythme** : l’horloge plus profonde dans le potentiel bat plus lentement.


5. Géodésiques = chemins de rythme extrême
==========================================
Les géodésiques maximisent (ou minimisent) :

.. math::

   \int d\tau.

- **Lecture standard** : trajectoire libre.  
- **Lecture rythme** : chemin où le métronome accumule le plus de temps propre possible.
