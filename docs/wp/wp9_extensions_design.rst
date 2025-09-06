WP9 — Extensions numériques : design technique
===============================================

Résumé
------
Ce document décrit la conception des extensions numériques du moteur **clockphase** :
(1) **Kerr lent** (frame-dragging, :math:`g_{0i}`), (2) **géodésiques ODE complètes**
pour particules et photons, (3) **cosmologie FLRW**. Il précise les formules, les choix
numériques, les interfaces C++ et les jeux de tests de validation.

Conventions
-----------

- Unités : **SI** (m, s, kg, J, Hz).  
- Signature métrique : :math:`(-,+,+,+)`.  
- Coordonnées par défaut : :math:`x^\mu=(ct,x,y,z)` côté API ; conversions internes si nécessaire.  
- Tolérances numériques visées : erreurs relatives :math:`\le 10^{-9}` pour quadratures fermées,
  :math:`\le 10^{-6}` pour intégrations ODE.


Kerr lent (frame-dragging g_{0i})
---------------------------------

But
***
Introduire une métrique **Kerr au premier ordre en rotation** (paramètre de spin petit),
afin de modéliser les effets **gravitomagnétiques** : Sagnac gravitationnel et **Lense–Thirring**.

Formules (Boyer–Lindquist, ordre 1 en a)
****************************************

On note :math:`a = J/(Mc)` et :math:`r_s = 2GM/c^2`. À l’ordre linéaire en :math:`a` :
(en coordonnées :math:`(t,r,\theta,\phi)`)

.. math::

   g_{tt} = -\left(1-\frac{r_s}{r}\right),\quad
   g_{rr} = \left(1-\frac{r_s}{r}\right)^{-1},\quad
   g_{\theta\theta}=r^2,\quad
   g_{\phi\phi} = r^2\sin^2\theta,\\
   g_{t\phi} = -\,\frac{2GJ}{c^3}\,\frac{\sin^2\theta}{r}.

En particulier dans le plan équatorial (:math:`\theta=\pi/2`) : :math:`g_{t\phi}=-2GJ/(c^3 r)`.

Précession de Lense–Thirring (ordre de grandeur, orbite quasi-circulaire rayon r)
*********************************************************************************

.. math::

   \Omega_{LT} \;\simeq\; \frac{2GJ}{c^2 r^3}.

Pour la Terre : :math:`J \approx I\,\omega \approx (0.3307\,M_\oplus R_\oplus^2)\,\omega_\oplus`.
À :math:`r \sim 7000~\mathrm{km}`, on vise **∼ 39 mas/an** (ordre Gravity Probe B).

Conception API
**************
- Nouvelle classe : ``KerrSlow(M, J)`` (ou ``KerrSlow(M, a)``) implémentant :math:`g_{\mu\nu}(x)`.
- Conversion ``(ct,x,y,z) -> (t,r,\theta,\phi)`` en interne (avec :math:`t=ct/c`).
- Remonter **les termes hors diagonale** : :math:`g_{0i}` depuis :math:`g_{t\phi}` (projection locale).

Points numériques
*****************
- Éviter les singularités de coordonnées aux pôles (gérer :math:`\sin\theta \to 0`).
- Valider que :math:`a \ll r` (approximation premier ordre).
- Proposer un mode **équatorial** (trajets en :math:`\theta=\pi/2`) pour les tests rapides.

Tests (acceptation)
*******************
- **Lense–Thirring** : orbite polaire terrestre → :math:`\Omega_{LT}` dans la fourchette
  **35–45 mas/an** selon l’altitude (OK si écart < 10%).



Géodésiques ODE complètes
--------------------------

But
***
Intégrer les géodésiques **timelike** (particules) et **null** (photons) pour sortir du cadre statique
et mesurer : **déviation de la lumière**, **avance du périhélie**, **temps de vol**, etc.

Équations (forme standard)
**************************

.. math::

   \ddot x^\mu + \Gamma^\mu_{\alpha\beta}\,\dot x^\alpha \dot x^\beta = 0,\qquad
   \Gamma^\mu_{\alpha\beta} = \tfrac{1}{2} g^{\mu\nu}(\partial_\alpha g_{\nu\beta} + \partial_\beta g_{\nu\alpha} - \partial_\nu g_{\alpha\beta}).

Stratégie numérique
*******************

- Calculer :math:`\Gamma^\mu_{\alpha\beta}` par **différentiation numérique** (différences centrées d’ordre 2 ou 4).
- Intégrateur ODE : **Dormand–Prince (RK45)** avec pas adaptatif (tol.rel 1e−9, tol.abs 1e−12).
- **Normalisations** :  
  - timelike : imposer :math:`g_{\mu\nu}\dot x^\mu \dot x^\nu = -c^2`,  
  - null : imposer :math:`g_{\mu\nu}\dot x^\mu \dot x^\nu = 0` (vérif numérique).
- **Contrôles de qualité** : conserver les **quantités de mouvement** (énergie angulaire en Schwarzschild/Kerr),
  vérifier les invariants (écart < 1e−6 sur toute l’intégration).
- **Événements** : détection de minimum d’approche (impact b) pour photons ; périastre pour orbites elliptiques.

Observables & formules de référence
***********************************

- **Déviation de la lumière** (Schwarzschild) :

  .. math::

     \alpha \;\simeq\; \frac{4GM}{c^2 b}.

- **Avance du périhélie** (par orbite, faible excentricité) :

  .. math::

     \Delta\omega \;\simeq\; \frac{6\pi GM}{a(1-e^2)c^2}.

  Mercure : **~43 arcsec/siècle** (acceptation ±1 arcsec).

- **Temps de vol** / délai (peut recouper Shapiro via intégration ODE).

Tests (acceptation)
*******************
- Déflexion solaire au limbe : **1.75 arcsec ± 0.02**.  
- Périhélie Mercure : **43″/siècle ± 1″**.  
- Invariants (norme de :math:`\dot x^\mu`) conservés à :math:`< 10^{-6}`.



Cosmologie FLRW
---------------

But
***
Étendre la librairie aux métriques cosmologiques **FLRW à courbure spatiale nulle** (plat),
pour montrer que la lecture « rythme » se généralise au fond cosmologique.

Métrique & relations
********************

.. math::

   ds^2 = -c^2 dt^2 + a^2(t)\,[dr^2 + r^2 d\Omega^2],\qquad
   H(t) = \frac{\dot a}{a}.

- **Horloge comobile** : :math:`R = d\tau/dt = 1`.  
- **Observateur avec vitesse propre v** : :math:`R \simeq 1 - v^2/(2c^2)`.  
- **Redshift cosmologique** : :math:`1+z = a(t_0)/a(t_e)` (photon le long d’une géodésique nulle).

Conception API
**************

- Classe ``FLRW(H0, Omega_m, Omega_L)`` fournissant :math:`a(t)` (ou :math:`t(a)`) par quadrature.  
- Générateur de **rayons nuls** (lignes de visée) retournant temps de vol, distance comobile, redshift.  
- Calcul de **\tau(z)** pour observateurs comobiles et non comobiles.

Tests (acceptation)
*******************

- **Redshift** : vérifier :math:`(1+z) = a_0/a` à tolérance 1e−9.  
- **Âge de l’univers** (ΛCDM fiduciel) : ordre de grandeur correct (vérification simple).



Interfaces C++ proposées (extraits code)
----------------------------------------

.. code-block:: cpp

   // Kerr lent
   class KerrSlow : public IMetric {
   public:
     KerrSlow(double M, double J) : M_(M), J_(J) {}
     void g(const MetricPoint& p, double Gmn[4][4]) const override; // remplit g_{μν}
   private:
     double M_, J_;
   };

.. code-block:: cpp

   // Géodésiques (intégrateur générique)
   struct GeodesicState { std::array<double,4> x; std::array<double,4> u; };
   class GeodesicIntegrator {
   public:
     GeodesicIntegrator(const IMetric& g);
     GeodesicState step(const GeodesicState&, double h); // RK45 adaptatif
     // utilitaires: christoffel(x), normalize_timelike(u), normalize_null(u), events...
   private:
     const IMetric& g_;
   };

.. code-block:: cpp

   // FLRW plat (fond)
   class FLRW : public IMetric {
   public:
     FLRW(double H0, double Om, double OL);
     void g(const MetricPoint& p, double Gmn[4][4]) const override; // diag(-1, a^2, a^2, a^2)
     double a_of_t(double t) const;
     double t_of_a(double a) const;
   private:
     double H0_, Om_, OL_;
   };



Jeux de tests & validations
---------------------------

Kerr lent
*********

- Comparaison **\Omega_{LT}** avec la formule d’ordre 1 : écart < 10% pour orbites LEO–MEO.

Géodésiques
***********

- Déviation de la lumière : 1.75″ ± 0.02 au Soleil (impact b ≈ R_⊙).  
- Périhélie de Mercure : 43″/siècle ± 1″.  
- Conservation : :math:`|g_{\mu\nu}\dot x^\mu \dot x^\nu - c^2|/c^2 < 10^{-6}` (timelike) ; norme nulle < 1e−8 (null).

FLRW
****
- Redshift : :math:`|(1+z) - a_0/a|/(1+z) < 10^{-9}`.  
- Temps de vol vs distance comobile : cohérence à 1e−8 sur cas tests.

Contraintes & risques connus
-----------------------------
- **Singularités de coordonnées** (Kerr/BL aux pôles) : prévoir bascule locale (tétrade) pour les conversions.  
- **Validité ordre 1 en a** : garantir :math:`a/r \ll 1` (doc + assertions).  
- **Stiffness** près de :math:`r\to r_s` : limiter le pas min, changer de coord (tortue) si nécessaire (v2).  
- **Précision des dérivées** : calibrer le pas de différentiation numérique (h ~ 1e−5 r) avec étude d’erreur.


Roadmap & livrables WP9
------------------------
- `metrics/kerrslow.hpp/.cpp` (v1), tests Lense–Thirring.  
- `geodesic.hpp/.cpp` (RK45 + Γ^μ_{αβ} num), tests : déflexion, Mercure.  
- `metrics/flrw.hpp/.cpp` + helpers a(t)/t(a), tests redshift.  
- Scénarios JSON + exemples CLI.  
- Documentation `.rst` (cette page + how-to).

Conclusion
----------
Ces extensions donnent la couverture complète des **tests RG avancés** et ouvrent
la voie à des applications cosmologiques, tout en restant compatibles avec le cadre
« horloges internes × temps propre » déjà validé (WP1–WP7).
