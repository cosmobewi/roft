#!/usr/bin/env python3
# WP19 — Newton vs ROFT (facteur de synchronie)
# Vue large + Vue zoom (bande observationnelle paramétrable)
#
# Exemple :
#   python wp19_illustration.py
#   python wp19_illustration.py --obs_min 1.25 --obs_max 1.35 --save_base wp19
#
# Par défaut : bande Gaia actuelle (+30 % / +40 %).

import argparse
import numpy as np
import matplotlib.pyplot as plt

# Constantes
G = 6.67430e-11
M_SUN = 1.98847e30
AU = 1.495978707e11

def v_newton(M, r):
    return np.sqrt(G * M / r)

def a_newton(M, r):
    return G * M / r**2

def S_sync(a, a0=1.2e-10, n=1.0):
    return (1.0 + (a0 / a)**n)**(1.0 / (4.0 * n))

def find_span_for_ratio(r_AU, ratio, target_min, target_max, pad_frac=0.2):
    mask = (ratio >= target_min) & (ratio <= target_max)
    if not np.any(mask):
        return None
    idx = np.where(mask)[0]
    x0, x1 = r_AU[idx[0]], r_AU[idx[-1]]
    dx = (x1 - x0) * pad_frac
    return max(r_AU[0], x0 - dx), min(r_AU[-1], x1 + dx)

def make_large_plot(r_AU, ratio, obs_min, obs_max):
    fig, ax = plt.subplots()
    ax.set_xscale("log")
    ax.plot(r_AU, ratio, label="v_ROFT / v_Newton")
    ax.axhline(obs_min, color="red", linestyle="--", label=f"{(obs_min-1)*100:.0f}%")
    ax.axhline(obs_max, color="orange", linestyle="--", label=f"{(obs_max-1)*100:.0f}%")
    ax.set_xlabel("Séparation (UA)")
    ax.set_ylabel("Excès de vitesse (ratio)")
    ax.set_title("Binaires larges — Newton vs ROFT (vue large)")
    ax.grid(True, which="both")
    ax.legend()
    return fig

def make_zoom_plot(r_AU, ratio, obs_min, obs_max, span, ypad=(0.05, 0.05)):
    fig, ax = plt.subplots()
    ax.plot(r_AU, ratio, label="v_ROFT / v_Newton")
    ax.axhline(obs_min, color="red", linestyle="--", label=f"{(obs_min-1)*100:.0f}%")
    ax.axhline(obs_max, color="orange", linestyle="--", label=f"{(obs_max-1)*100:.0f}%")
    if span is not None:
        ax.set_xlim(span[0], span[1])
    else:
        ax.set_xlim(1.5e4, 2.5e4)  # fallback
    ymin = obs_min - ypad[0]
    ymax = obs_max + ypad[1]
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel("Séparation (UA)")
    ax.set_ylabel("Excès de vitesse (ratio)")
    ax.set_title("Zone observationnelle (vue zoom)")
    ax.grid(True, which="both")
    ax.legend()
    return fig

def main():
    ap = argparse.ArgumentParser(description="WP19: Newton vs ROFT — vue large + zoom observationnel")
    ap.add_argument("--M_sun", type=float, default=2.0, help="Masse totale en masses solaires (défaut: 2)")
    ap.add_argument("--a0", type=float, default=1.2e-10, help="Échelle faible-a (défaut: 1.2e-10 m/s^2)")
    ap.add_argument("--n", type=float, default=1.0, help="Paramètre d’interpolation pour S(a) (défaut: 1.0)")
    ap.add_argument("--rmin_AU", type=float, default=1e4, help="Séparation min (UA) (défaut: 1e4)")
    ap.add_argument("--rmax_AU", type=float, default=1e5, help="Séparation max (UA) (défaut: 1e5)")
    ap.add_argument("--points", type=int, default=800, help="Nb de points (défaut: 800)")
    ap.add_argument("--obs_min", type=float, default=1.3, help="Borne basse du ratio observationnel (défaut: 1.3)")
    ap.add_argument("--obs_max", type=float, default=1.4, help="Borne haute du ratio observationnel (défaut: 1.4)")
    ap.add_argument("--save_base", type=str, help="Préfixe pour sauvegarder les figures (ex: figs/wp19)")
    args = ap.parse_args()

    M = args.M_sun * M_SUN
    r = np.logspace(np.log10(args.rmin_AU*AU), np.log10(args.rmax_AU*AU), args.points)
    r_AU = r / AU

    aN = a_newton(M, r)
    S = S_sync(aN, a0=args.a0, n=args.n)
    ratio = S

    # Points-clés console
    for R_AU in [1.0e4, 1.5e4, 2.0e4, 2.5e4, 3.0e4]:
        aN_val = a_newton(M, R_AU*AU)
        S_val = S_sync(aN_val, a0=args.a0, n=args.n)
        print(f"r = {R_AU:7.0f} UA | a_N = {aN_val: .3e} m/s^2 | "
              f"S = {S_val: .3f} | +{(S_val-1)*100: .1f}%")

    # Figures
    fig_large = make_large_plot(r_AU, ratio, args.obs_min, args.obs_max)
    span = find_span_for_ratio(r_AU, ratio, args.obs_min, args.obs_max, pad_frac=0.25)
    fig_zoom = make_zoom_plot(r_AU, ratio, args.obs_min, args.obs_max, span)

    if args.save_base:
        fig_large.savefig(f"{args.save_base}_large.png", dpi=300, bbox_inches="tight")
        fig_zoom.savefig(f"{args.save_base}_zoom.png",  dpi=300, bbox_inches="tight")
        print(f"✅ Figures enregistrées : {args.save_base}_large.png et {args.save_base}_zoom.png")
    else:
        plt.show()

if __name__ == "__main__":
    main()
