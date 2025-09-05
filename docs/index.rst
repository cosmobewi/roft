==========================================
Documentation — Pont RG–MQ et extensions
==========================================

Introduction
============
Ce projet explore la résolution du « problème du temps » en gravité quantique
en établissant un pont simple et testable entre :

- la **relativité générale (RG)**, où le temps est le temps propre :math:`d\tau`,  
- la **mécanique quantique (MQ/QFT)**, où le temps est encodé dans la phase
  :math:`\exp(-iEt/\hbar)`.

La clé est l’équation-pont :

.. math::

   \nu_{\text{obs}} = \frac{E}{h}\,\frac{d\tau}{dt}.

Cette documentation suit un découpage en « Work Packages » (WP) retraçant
le cheminement théorique, numérique et expérimental.

Table des matières
==================

.. toctree::
   :maxdepth: 2
   :caption: Contenu

   wp1_rg_classique
   wp2_champ_horloges
   wp3_mq_qft_courbe
   wp4_exemples_calc
   wp5_composantes
   wp6_impl_lib
   wp7_tests
   wp8_doc_integration
   wp9_extensions_design
   wp10_scientifique
   wp10_vulgarise

Navigation
==========
- **WP1–WP5** : bases théoriques (RG, MQ, pont).  
- **WP6–WP7** : implémentation C++ standalone + validation numérique.  
- **WP8–WP9** : documentation intégrée et extensions (Kerr, géodésiques, FLRW).  
- **WP10** : résolution du problème du temps, limites restantes, ouverture
  vers la gravité quantique complète.
