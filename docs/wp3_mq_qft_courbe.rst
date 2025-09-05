=========================================
WP3 — MQ/QFT minimal en espace-temps courbe
=========================================

But
===
Montrer que la phase quantique encode naturellement les effets de la relativité générale au premier ordre.

1. Équation de Klein–Gordon courbe
==================================
Équation :

.. math::

   \big(\Box_g + \tfrac{m^2c^2}{\hbar^2}\big)\,\phi(x) = 0,
   \qquad \Box_g = \frac{1}{\sqrt{-g}}\partial_\mu\!\left(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\right).

Ansatz WKB :

.. math::

   \phi(x) \sim A(x)\,e^{\tfrac{i}{\hbar}S(x)}.

En insérant :

.. math::

   g^{\mu\nu}\,\partial_\mu S\,\partial_\nu S + m^2c^2 = 0.

- **Lecture standard** : équation eikonale, équivalente à la condition de masse relativiste.  
- **Lecture rythme** : la phase quantique avance en fonction du temps propre (l’horloge interne suit la géodésique).


2. Lagrangien non-relativiste en potentiel
==========================================
Développement faible vitesse + faible potentiel :

.. math::

   L \;\simeq\; -mc^2 + \tfrac{1}{2}m v^2 - m\Phi.

La phase accumulée :

.. math::

   \Delta\varphi \;=\; \frac{1}{\hbar}\int \Big(\tfrac{1}{2} m v^2 - m\Phi\Big)\,dt.

- **Lecture standard** : la mécanique quantique “voit” le potentiel de Newton.  
- **Lecture rythme** : chaque particule ajoute/diminue des battements selon sa cinétique et sa profondeur dans \Phi.


3. Phase de Compton modulée
============================
En réintroduisant le terme :math:`-mc^2t` :

.. math::

   \varphi(t) \;=\; -\,\frac{mc^2}{\hbar}\,t \;+\; \frac{1}{\hbar}\int\!\Big(\tfrac{1}{2} m v^2 - m\Phi\Big)\,dt.

- Le premier terme = oscillation de Compton (horloge interne).  
- Le second = modulation par vitesse et potentiel (relativité générale).

Ainsi, la **phase quantique** contient déjà le couple MQ + RG.

Conclusion
==========
- La QFT en espace-temps courbe redonne directement la condition géodésique (via l’ansatz WKB).  
- Le Lagrangien NR fait apparaître :math:`m\Phi/\hbar` → déphasages gravitationnels mesurables.  
- **Lecture rythme** : tout système quantique est une horloge de Compton dont la cadence est modulée par le potentiel gravitationnel et la vitesse.
