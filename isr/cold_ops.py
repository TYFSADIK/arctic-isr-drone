"""Cold-weather planning helpers: usable flight time vs temperature and glove-friendly UI limits."""


def usable_capacity_fraction(temp_c: float, heated=False) -> float:
    """Rough LiPo/Li-ion usable capacity vs pack temperature.

    Placeholder curve. Replace it with measurements from the cold-soak-battery-rig repo.
    """
    t = max(temp_c, 15.0) if heated else temp_c
    if t >= 20:
        return 1.0
    if t <= -30:
        return 0.35
    return 0.35 + 0.65 * (t + 30) / 50.0


def flight_time_min(nominal_min: float, temp_c: float, heated=False, reserve=0.25) -> float:
    return nominal_min * usable_capacity_fraction(temp_c, heated) * (1 - reserve)


# Glove usability: minimum touch target and button spacing for heavy mitts.
GLOVE_MIN_TARGET_MM = 15
GLOVE_MIN_SPACING_MM = 8


def check_layout(buttons_mm):
    """buttons_mm: [(name, width, height)] -> list of problems."""
    return [f"{n}: {w}x{h} mm < {GLOVE_MIN_TARGET_MM} mm" for n, w, h in buttons_mm
            if min(w, h) < GLOVE_MIN_TARGET_MM]
