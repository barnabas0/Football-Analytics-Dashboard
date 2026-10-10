from statsbombpy import sb

def get_competitions():
    """Return comps available through StatsBomb."""
    return sb.competitions()

def get_matches(competitions_id, season_id):
    return sb.matches(
        competition_id=competitions_id,
        season_id=season_id
    )

def get_events(match_id):
    return sb.events(match_id=match_id)