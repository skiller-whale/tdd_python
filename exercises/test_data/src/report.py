"""Generates multi-section text reports for player profiles.

The report includes sections for:
- Player identification (name, ID, email)
- Stats (games played, won, win rate)
- Performance (average attempts, fastest win)
- Activity (first/last played dates)
- Ranking (rank, percentile)
- Achievements (trophy list or none)
"""


def generate_player_report(player_data):
    """Generates a multi-section text report for a player profile.

    The report includes these sections:

      === PlayerName ===
      ID: player_id
      Email: email

      --- Stats ---
      Games Played: N
      Games Won: N
      Win Rate: N.N%

      --- Performance ---
      Average Attempts: N.N
      Fastest Win: N guess(es)

      --- Activity ---
      First Played: YYYY-MM-DD
      Last Played: YYYY-MM-DD

      --- Ranking ---
      Rank: #N
      Percentile: Top N%

      --- Achievements ---
      🏆 Achievement 1
      🏆 Achievement 2
    """
    return f"""=== {player_data['player_name']} ===
ID: {player_data['player_id']}
Email: {player_data['email']}

--- Stats ---
Games Played: {player_data['games_played']}
Games Won: {player_data['games_won']}
Win Rate: {player_data['win_rate'] * 100:.1f}%

--- Performance ---
Average Attempts: {player_data['average_attempts']:.1f}
Fastest Win: {player_data['fastest_win']} guess(es)

--- Activity ---
First Played: {player_data['first_played'][:10]}
Last Played: {player_data['last_played'][:10]}

--- Ranking ---
Rank: #{player_data['rank']}
Percentile: Top {player_data['percentile']}%

--- Achievements ---
{format_achievements(player_data['achievements'])}""".strip()


def format_achievements(achievements):
    """Formats a list of achievement names into a display string.

    Returns "No achievements yet." for an empty list, or each
    achievement on its own line with a trophy emoji prefix.
    """
    if len(achievements) == 0:
        return "No achievements yet."
    return "\n".join(f"🏆 {a}" for a in achievements)
