=================================
WP4 — Cahier d'exemples calculés
=================================

But
===
Fournir des cas concrets où l’unification **horloge interne (Compton)** × **modulation relativiste (d\tau/dt)** donne exactement les résultats observés.

Rappel (pont)
=============
.. math::

   \nu_{\text{obs}} = \frac{E}{h}\,\frac{d\tau}{dt},
   \qquad
   \frac{d\tau}{dt}\simeq 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2},
   \qquad
   \frac{\Delta\nu}{\nu}\simeq \frac{\Delta\Phi}{c^2}-\frac{\Delta(v^2)}{2c^2}.


A) Deux altitudes (écart \Delta h)
==================================
Formule locale (faible champ) :

.. math::

   \frac{\Delta\nu}{\nu}\;\simeq\;\frac{g\,\Delta h}{c^2}.

Numérique : :math:`\Delta h=1000~\mathrm{m}` →

.. math::

   \frac{\Delta\nu}{\nu} \approx 1.09\times 10^{-13}.

Gain par jour : ~9.4 ns/jour.


B) GPS (gravité + vitesse)
==========================
Altitude : :math:`h \approx 20\,200~\mathrm{km}`, rayon :math:`r=R_\oplus+h`.

Décalage gravitationnel :

.. math::

   \left.\frac{\Delta\nu}{\nu}\right|_{\rm grav}
   = \frac{\mu_\oplus}{c^2}\left(\frac{1}{R_\oplus}-\frac{1}{r}\right)
   \approx 5.285\times 10^{-10} \;\Rightarrow\; +45.7~\mu s/j.

Dilatation par la vitesse :

.. math::

   \left.\frac{\Delta\nu}{\nu}\right|_{\rm vit}
   \simeq -\frac{v^2}{2c^2} \approx -8.34\times 10^{-11}
   \;\Rightarrow\; -7.2~\mu s/j.

Bilan net :

.. math::

   +38.5~\mu s/j.

Correction appliquée dans le système.


C) Pound–Rebka (22,5 m)
=======================
.. math::

   \frac{\Delta\nu}{\nu}\approx \frac{g\,\Delta h}{c^2}
   = \frac{9.81\times 22.5}{c^2}
   \approx 2.45\times 10^{-15}.

Énergie photon Mössbauer : :math:`E=14.4~\mathrm{keV}` →

.. math::

   \Delta E \approx 3.5\times 10^{-11}~\mathrm{eV}.

Vitesse Doppler équivalente : ~0.74 µm/s.


D) Muons cosmiques
==================
Durée de vie au repos : :math:`\tau_0 = 2.197~\mu s`.  
Portée sans dilatation : ~659 m.  
Atmosphère : ~15 km.  

Probabilité de survie :

.. math::

   P(d)=\exp\!\left(-\,\frac{d}{\gamma c \tau_0}\right).

- \gamma=10 → survie ~10%.  
- \gamma=20 → survie ~32%.

Observation : ils atteignent le sol → confirmé.


E) Interférométrie atomique (Mach–Zehnder gravitaire)
=====================================================
Lagrangien non-relativiste :

.. math::

   L \approx \tfrac{1}{2}mv^2 - m\Phi.

Phase sur un bras : :math:`\varphi=\tfrac{1}{\hbar}\int L\,dt`.  
Deux bras séparés verticalement \Delta h, durée T :

.. math::

   \Delta\varphi \;\approx\;\frac{m g \Delta h}{\hbar}\,T.

Version impulsions lumineuses :

.. math::

   \Delta\varphi = k_{\rm eff}\,g\,T^2.


F) Retard de Shapiro
====================
Pour un rayon lumineux rasant une masse :

.. math::

   \Delta t \;\approx\; \frac{2GM}{c^3}\,\ln\!\frac{r_1+r_2+R}{r_1+r_2-R}.

Lecture rythme : le faisceau traverse une zone où R(x)<1 (tempo ralenti), accumulant un retard.


G) Proximité d’un horizon (Schwarzschild)
=========================================
.. math::

   \frac{d\tau}{dt}=\sqrt{1-\frac{r_s}{r}},\qquad r_s=\frac{2GM}{c^2}.

Exemple trou noir 10 M_\odot → r_s≈29.5 km.

- r=1.1 r_s → d\tau/dt≈0.302 (tempo ralenti ×3.3).  
- r=1.01 r_s → d\tau/dt≈0.0995 (tempo ralenti ×10).


Conclusion WP4
==============
Tous ces exemples montrent que l’approche “horloge de Compton × d\tau/dt” retombe **exactement** sur les résultats expérimentaux connus.  
La lecture “rythme” rend tangible l’effet de la gravité comme une modulation universelle des tempos.
