import requests
from collections import defaultdict

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_all_results(session, driver_id):
    all_races = []
    offset = 0
    limit = 100

    while True:
        url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit={limit}&offset={offset}"
        res = session.get(url)
        if res.status_code != 200:
            break
        data = res.json()
        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        if not races:
            break
        all_races.extend(races)
        offset += limit
    return all_races

def get_driver_stats(driver_id):
    wins = 0
    podiums = 0
    championships = 0

    session = requests.Session()

    # 1. Toutes les courses
    races = get_all_results(session, driver_id)

    # Pour calculer champion par saison
    season_points = defaultdict(lambda: defaultdict(int))  # season -> driverId -> points

    for race in races:
        season = race['season']
        for result in race['Results']:
            pid = result['Driver']['driverId']
            points = float(result['points'])
            season_points[season][pid] += points

        # Stats pilote ciblé
        result = race['Results'][0]  # on prend le pilote principal
        position = result['position']
        if result['Driver']['driverId'] == driver_id:
            if position == "1":
                wins += 1
            if position in ["1","2","3"]:
                podiums += 1

    # 2. Calcul champion par saison
    for season, drivers in season_points.items():
        max_points = max(drivers.values())
        champions = [pid for pid, pts in drivers.items() if pts == max_points]
        if driver_id in champions:
            championships += 1

    return {
        "wins": wins,
        "podiums": podiums,
        "championships": championships
    }

# TEST
if __name__ == "__main__":
    stats = get_driver_stats("hamilton")
    print("\n=== STATS ===")
    print(f"Wins: {stats['wins']} 🏆")
    print(f"Podiums: {stats['podiums']} 🥇🥈🥉")
    print(f"Championships: {stats['championships']} 👑")
    