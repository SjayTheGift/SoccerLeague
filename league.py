import argparse
import sys
from collections import defaultdict

def parse_results(line):
    """Parse a single line of match results."""
    home_team, home_score, away_team, away_score = None, None, None, None
    match = line.split(', ')
    if len(match) == 2:
        home, away = match
        home_team, home_score = home.rsplit(' ', 1)
        away_team, away_score = away.rsplit(' ', 1)
        return (home_team, int(home_score), away_team, int(away_score))
    return None

def calculate_points(results):
    """Calculate the points for each team based on match results."""
    points = defaultdict(int)

    for home_team, home_score, away_team, away_score in results:
        # Initialize points for both teams if not already present
        points[home_team]
        points[away_team]

        if home_score > away_score:
            points[home_team] += 3  # Home win
        elif home_score < away_score:
            points[away_team] += 3  # Away win
        else:
            points[home_team] += 1  # Draw
            points[away_team] += 1   # Draw

    return points

def rank_teams(points):
    """Rank teams based on points and alphabetical order."""
    ranked = sorted(points.items(), key=lambda item: (-item[1], item[0]))
    return ranked

def format_output(ranked):
    """Format the output for display."""
    output = []
    current_rank = 1
    last_points = None
    for idx, (team, pts) in enumerate(ranked):
        if last_points is None or pts != last_points:
            current_rank = idx + 1
        last_points = pts
        point_label = "pt" if pts == 1 else "pts"
        output.append(f"{current_rank}. {team}, {pts} {point_label}")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description='Calculate league rankings from game results.')
    parser.add_argument('input_file', type=str, help='File containing game results')
    
    args = parser.parse_args()

    results = []
    with open(args.input_file, 'r') as f:
        for line in f:
            parsed = parse_results(line.strip())
            if parsed:
                results.append(parsed)

    points = calculate_points(results)
    ranked = rank_teams(points)
    output = format_output(ranked)
    print(output)

if __name__ == "__main__":
    main()