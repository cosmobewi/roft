WP5 — Cahier d'exemples calculés
================================

But
---
Fournir des cas concrets où l’unification **horloge interne (Compton)** × **modulation relativiste** (:math:`d\tau/dt`)
retombe exactement sur les résultats observés.

Rappel (pont)
-------------
.. math::

   \nu_{\text{obs}} = \frac{E}{h}\,\frac{d\tau}{dt},
   \qquad
   \frac{d\tau}{dt}\simeq 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2},
   \qquad
   \frac{\Delta\nu}{\nu}\simeq \frac{\Delta\Phi}{c^2}-\frac{\Delta(v^2)}{2c^2}.

.. admonition:: Constantes & lecture des signes
   :class: important

   - c = 299 792 458 m/s  
   - g ≃ 9.81 m/s²  
   - G = 6.67430×10⁻¹¹ m³·kg⁻¹·s⁻²  
   - R⊕ = 6371 km  

   Potentiel newtonien : Φ < 0  

   | En faible champ : Δν/ν ≃ ΔΦ/c² – Δ(v²)/(2c²).  
   | Un point **plus haut** (potentiel moins négatif) → fréquence **plus grande**.


A) Deux altitudes (écart Δh)
----------------------------
Formule locale (faible champ) :

.. math::

   \frac{\Delta\nu}{\nu}\;\simeq\;\frac{g\,\Delta h}{c^2}.

**Numérique.** Δh = 1000 m →

.. math::

   \frac{\Delta\nu}{\nu} \approx 1.09\times 10^{-13}.

Gain par jour : ~9.4 ns/jour.

.. admonition:: Lecture ROFT
   :class: tip

   Même horloge E/h, **modulation** par dτ/dt via ΔΦ.


B) GPS (gravité + vitesse)
--------------------------
Altitude : h ≈ 20 200 km, rayon r = R⊕ + h, vitesse orbitale v ≃ 3.874 km/s.

Décalage gravitationnel :

.. math::

   \left.\frac{\Delta\nu}{\nu}\right|_{\rm grav}
   = \frac{\mu_\oplus}{c^2}\left(\frac{1}{R_\oplus}-\frac{1}{r}\right)
   \approx 5.285\times 10^{-10}
   \;\Rightarrow\; +45.7~\mu s/j.

Dilatation par la vitesse :

.. math::

   \left.\frac{\Delta\nu}{\nu}\right|_{\rm vit}
   \simeq -\frac{v^2}{2c^2} \approx -8.34\times 10^{-11}
   \;\Rightarrow\; -7.2~\mu s/j.

Bilan net :

.. math::

   +38.5~\mu s/j.

Correction appliquée dans le système.

.. admonition:: Lecture ROFT
   :class: tip
   
   ν = E/h modulée par **gravité + vitesse** → dτ/dt combine les deux contributions.


C) Pound–Rebka (22,5 m)
-----------------------
.. math::

   \frac{\Delta\nu}{\nu}\approx \frac{g\,\Delta h}{c^2}
   = \frac{9.81\times 22.5}{c^2}
   \approx 2.45\times 10^{-15}.

Énergie photon Mössbauer : E = 14.4 keV →

.. math::

   \Delta E \approx 3.5\times 10^{-11}\ \text{eV}.

Vitesse Doppler équivalente : ~0.74 μm/s (ordre de grandeur).

.. admonition:: Lecture ROFT
   :class: tip
   
   Décalage = **contraste de rythme** entre deux altitudes.


D) Muons cosmiques
------------------
Durée de vie au repos : τ₀ = 2.197 μs.  
Portée sans dilatation : ~659 m.  
Atmosphère : ~15 km.

Probabilité de survie :

.. math::

   P(d)=\exp\!\left(-\,\frac{d}{\gamma c \tau_0}\right).

- γ = 10 → survie ~10 %.  
- γ = 20 → survie ~32 %.

Condition de traversée 15 km : γ c τ₀ ≳ 15 km → γ ≳ 23.

**Observation.** Ils atteignent le sol → confirmé.

.. admonition:: Lecture ROFT
   :class: tip
   
   La **vitesse** atténue le rythme local : dτ/dt = γ⁻¹.


E) Interférométrie atomique (Mach–Zehnder gravitaire)
-----------------------------------------------------
Lagrangien non-relativiste :

.. math::

   L \approx \tfrac{1}{2}mv^2 - m\Phi.

Phase sur un bras : φ = (1/ħ) ∫ L dt.  
Deux bras séparés verticalement Δh, durée T :

.. math::

   \Delta\varphi \;\approx\;\frac{m g \Delta h}{\hbar}\,T.

Version impulsions lumineuses (k_eff = |k₁ – k₂|) :

.. math::

   \Delta\varphi = k_{\rm eff}\,g\,T^2.

.. admonition:: Lecture ROFT
   :class: tip
   
   La **phase** accumule la cadence (E/ħ) pondérée par dτ.


F) Retard de Shapiro
--------------------
Pour un rayon lumineux rasant une masse :

.. math::

   \Delta t \;\approx\; \frac{2GM}{c^3}\,\ln\!\frac{r_1+r_2+R}{r_1+r_2-R}.

Testé (Cassini/planètes) — dépend **logarithmiquement** de la géométrie.

.. admonition:: Lecture ROFT
   :class: tip
   
   Le faisceau traverse une zone où R(x) < 1 (tempo ralenti), d’où un retard cumulé.


G) Proximité d’un horizon (Schwarzschild)
-----------------------------------------
.. math::

   \frac{d\tau}{dt}=\sqrt{1-\frac{r_s}{r}},\qquad r_s=\frac{2GM}{c^2}.

Exemple trou noir 10 M⊙ → rₛ ≈ 29.5 km.

- r = 1.1 rₛ → dτ/dt ≈ 0.302 (tempo ralenti ×3.3).  
- r = 1.01 rₛ → dτ/dt ≈ 0.0995 (tempo ralenti ×10).

Pour un observateur lointain, à r → rₛ, dτ/dt → 0.

.. admonition:: Lecture ROFT
   :class: tip
   
   **Figement du rythme** à l’horizon : limite du spectre de visibilité.


Résumé “axiome ↔ observable”
----------------------------
.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - Axiome ROFT
     - Formule clef
     - Cas test

   * - Rythme (E/h)
     - :math:`\nu = E/h`
     - Muons (durée de vie), interférométrie (phase)

   * - Gravité = modulation
     - :math:`d\tau/dt \simeq 1+\Phi/c^2 - v^2/(2c^2)`
     - Altitudes, GPS, Shapiro, horizon

   * - Contraste = mesure
     - :math:`\Delta\nu/\nu \simeq \Delta\Phi/c^2 - \Delta(v^2)/(2c^2)`
     - Pound–Rebka, GPS (bilan), spectres

   * - Visibilité (spectre)
     - :math:`\Delta\nu>0` visible ; :math:`\Delta\nu=0` synchrone ; :math:`d\tau/dt\to 0` figé
     - Matière noire (synchrone), lumière, trous noirs


Conclusion
----------
Tous ces exemples confirment que l’approche **horloge de Compton × dτ/dt** produit
les mêmes prédictions que la RG/MQ testées expérimentalement.  
La lecture “rythme” rend tangible la gravité comme **modulation universelle** des tempos
et clarifie que l’observable réel est toujours un **contraste de rythme**.