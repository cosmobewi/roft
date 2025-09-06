=============================
WP7 — Plan de tests complet
=============================

Objectif
========
Valider numériquement que la librairie **clockphase** (WP6 standalone) retombe sur
les prédictions RG + MQ (formulées en « rythme d’horloges ») pour les cas classiques.

Critères généraux
=================
- Unités **SI** strictes (m, s, kg, J, Hz).
- Tolérances : erreur relative **< 1e-6** quand c’est numérique stable ; sinon tolérance absolue documentée.
- Sorties de tests **lisibles** (valeurs calculées vs attendues).
- Tests regroupés dans `ctest` (ou exécutable unique multiprise si souhaité).

Jeux de tests
=============

1) Altitudes (Δh)
-----------------
**But** : vérifier le redshift gravitationnel local en champ faible.

Formule de référence : :math:`\Delta\nu/\nu \simeq g\,\Delta h/c^2`.

Cas testé : :math:`\Delta h = 1000~\mathrm{m}` → **~9.4 ns/jour** d’avance.

Seuils d’acceptation : |Δτ(meas) − 9.4 ns| < 2 ns par jour (intégration simple).

2) GPS (gravité + vitesse)
--------------------------
**But** : vérifier +45.7 µs/j (gravité) et −7.2 µs/j (vitesse), net +38.5 µs/j.

Formules :

.. math::

   \left.\frac{\Delta\nu}{\nu}\right|_{\rm grav} = \frac{\mu}{c^2}\left(\frac{1}{R_\oplus}-\frac{1}{r}\right),\quad
   \left.\frac{\Delta\nu}{\nu}\right|_{\rm vit} = -\frac{v^2}{2c^2},\ v=\sqrt{\mu/r}.

Seuils : ±0.2 µs/j pour chaque terme, ±0.5 µs/j sur le net.

3) Pound–Rebka (22.5 m)
-----------------------
**But** : redshift gravitationnel sur 22.5 m, valeur attendue **2.45e-15**.

Seuil : |Δν/ν − 2.45e-15| < 2e-17.

4) Muons cosmiques
------------------
**But** : vérifier la **dilatation du temps** via la probabilité de survie.

Formule : :math:`P(d)=\exp(-d/(\gamma c \tau_0))` avec :math:`\tau_0=2.197~\mu s`.

Cas : d=15 km, γ=10 → ~0.10 ; γ=20 → ~0.32.  
Seuils : ±0.01 absolu.

5) Interférométrie atomique (NR)
--------------------------------
**But** : phase gravitationnelle **Δφ ≈ (m g Δh / ħ) T** (ou **k_eff g T²**).

Seuil : erreur relative < 1e-6 pour la formule NR.

6) Retard de Shapiro
--------------------
**But** : délai **Δt = (2GM/c³) ln( (r1+r2+R)/(r1+r2−R) )**.

Cas numériques jouets (valeurs fixes) ; tolérance relative 1e-9 (formule fermée).

7) Déviation de la lumière
--------------------------
**But** : vérifier l’angle **α ≈ 4GM/(c² b)** avec Schwarzschild.

Seuil : erreur relative 1e-6 (géométrie radiale simple).

Rapports & CI
=============
- Chaque test imprime : valeur calculée, valeur attendue, écart, verdict **[OK]/[FAIL]**.
- Intégration **CTest** recommandée (cf. `CMakeLists.addon.txt`).
