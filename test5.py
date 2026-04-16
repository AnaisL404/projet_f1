import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"


# 🔥 Récupérer TOUTES les courses (pagination)
def get_all_results(session, driver_id):
    all_races = []
    offset = 0
    limit = 100

    while True:
        url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit={limit}&offset={offset}"
        res = session.get(url)

        if res.status_code != 200:
            print("Erreur résultats:", res.status_code)
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

    # 🔥 1. Toutes les courses
    races = get_all_results(session, driver_id)

    for race in races:
        result = race['Results'][0]
        position = result['position']

        if position == "1":
            wins += 1

        if position in ["1", "2", "3"]:
            podiums += 1

    # 🔥 2. Récupérer toutes les saisons
    seasons_url = f"{BASE_URL}/seasons.json?limit=1000"
    seasons_res = session.get(seasons_url)

    if seasons_res.status_code != 200:
        print("Erreur saisons:", seasons_res.status_code)
        return None

    seasons_data = seasons_res.json()
    seasons = seasons_data.get('MRData', {}).get('SeasonTable', {}).get('Seasons', [])

    # 🔥 3. Calcul des championnats (FIX FIABLE)
    for s in seasons:
        year = s['season']

        standings_url = f"{BASE_URL}/{year}/driverStandings.json"
        res = session.get(standings_url)

        if res.status_code != 200:
            continue

        data = res.json()

        standings_lists = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])

        if not standings_lists:
            continue

        driver_standings = standings_lists[0].get('DriverStandings', [])

        if not driver_standings:
            continue

        champion = driver_standings[0]

        if champion.get('Driver', {}).get('driverId') == driver_id:
            championships += 1

    return {
        "wins": wins,
        "podiums": podiums,
        "championships": championships
    }


# 🔥 TEST
if __name__ == "__main__":
    stats = get_driver_stats("hamilton")

    print("\n=== STATS ===")
    print(f"Wins: {stats['wins']} 🏆")
    print(f"Podiums: {stats['podiums']} 🥇🥈🥉")
    print(f"Championships: {stats['championships']} 👑")