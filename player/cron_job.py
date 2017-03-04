from .models import Profile, Leaderboard


def update_leaderboard():
    leaderboard = Profile.objects.raw('SELECT id, ROW_NUMBER() over (ORDER BY points DESC, points_update_timestamp DESC ) as rank  FROM player_profile ;')
    for player in leaderboard:
        Leaderboard.objects.update_or_create(rank=player.rank, defaults={'profile': player})
