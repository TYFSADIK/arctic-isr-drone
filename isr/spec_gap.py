"""Spec-gap calculator: what a Lepton hobby build can and cannot do vs the target spec.

Uses Johnson-style pixels-on-target criteria (critical dimension ~0.5 m for a
person, 2.3 m for a vehicle): detection ~1.5 px, recognition ~6 px, identification ~12 px.
"""
import math

CRITERIA_PX = {"detect": 1.5, "recognise": 6.0, "identify": 12.0}
TARGETS_M = {"person": 0.5, "snowmobile": 1.2, "vehicle": 2.3}


def ifov_rad(hfov_deg=57.0, width_px=160):
    return math.radians(hfov_deg) / width_px


def max_range_m(target="person", task="detect", hfov_deg=57.0, width_px=160):
    return TARGETS_M[target] / (CRITERIA_PX[task] * ifov_rad(hfov_deg, width_px))


def table(spec_ranges_m: dict, hfov_deg=57.0, width_px=160):
    """spec_ranges_m: {("person","detect"): 300, ...} -> rows of (target, task, spec, achieved, gap%)."""
    rows = []
    for (target, task), spec in spec_ranges_m.items():
        got = max_range_m(target, task, hfov_deg, width_px)
        rows.append((target, task, spec, round(got), round(100 * (got - spec) / spec)))
    return rows


def markdown(rows):
    lines = ["| Target | Task | Spec range (m) | Hobby build (m) | Gap |", "|---|---|---|---|---|"]
    lines += [f"| {t} | {k} | {s} | {g} | {p:+d}% |" for t, k, s, g, p in rows]
    return "\n".join(lines)
