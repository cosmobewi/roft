WP2 — Champ d'horloges R(x)=dτ/dt
=================================

But
---
Définir un champ scalaire opérationnel qui encode la cadence locale des horloges.

Définition
----------
On introduit :

.. math::

   R(x) \;\equiv\; \frac{d\tau}{dt}
   \;=\;\frac{1}{c}\,\sqrt{-\,g_{\mu\nu}(x)\,\frac{dx^\mu}{dt}\,\frac{dx^\nu}{dt}}.

- **Lecture standard** : facteur de dilatation du temps propre par rapport au temps coordonné.  
- **Lecture rythme** : le champ :math:`R(x)` est la "vitesse de battement" des horloges locales.

Cas statique (faible champ)
---------------------------
Pour une métrique de type Schwarzschild et vitesses modérées :

.. math::

   R(x) \;\simeq\; \sqrt{1+\frac{2\Phi}{c^2}-\frac{v^2}{c^2}}.

- **Lecture standard** : correction par potentiel et vitesse.  
- **Lecture rythme** : :math:`\Phi` règle le tempo global, :math:`v` désynchronise localement.

Extension : rotation et gravitomagnétisme
-----------------------------------------
Si la métrique a des termes hors diagonale :math:`g_{0i}` (par ex. cadre en rotation, Lense–Thirring) :

.. math::

   R(x) = \frac{1}{c}\sqrt{-\,g_{00} - 2 g_{0i}\frac{dx^i}{dt} - g_{ij}\frac{dx^i}{dt}\frac{dx^j}{dt}}.

- **Lecture standard** : apparition d’effets de type "gravitomagnétique".  
- **Lecture rythme** : les horloges ressentent une modulation supplémentaire liée aux flux de rotation.

Dictionnaire g_{\mu\nu} ↔ R(x)
------------------------------
- :math:`g_{00}` → ralentissement dû au potentiel (tempo global).  
- :math:`g_{0i}` → effets de rotation (décalage de phase, Sagnac).  
- :math:`g_{ij}` → courbure spatiale (trajet des rayons, cohérence des tempos).

Conclusion
----------
Le champ :math:`R(x)` traduit la métrique entière en termes de **rythmes d’horloges**.  
Il devient une variable de travail universelle : comparer deux observateurs revient à comparer leurs :math:`R(x)`.
