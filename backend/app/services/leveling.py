def xp_from_minutes(minutes: int) -> int:
    return max(0, minutes)

def level_from_minutes(total_minutes: int) -> int:
    xp = xp_from_minutes(total_minutes)
    return int((xp / 300) ** 0.5)  # Level floor

def next_level_progress(total_minutes: int):
    xp = xp_from_minutes(total_minutes)
    level = level_from_minutes(total_minutes)
    cur_req = 300 * (level ** 2)
    next_req = 300 * ((level + 1) ** 2)
    return {
        "level": level,
        "xp": xp,
        "current_level_floor": cur_req,
        "next_level_req": next_req,
        "to_next": max(0, next_req - xp),
        "pct": 0.0 if next_req == cur_req else (xp - cur_req) / (next_req - cur_req)
    }
