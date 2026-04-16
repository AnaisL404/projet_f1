import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_driver_stats_fast(driver_id):
    wins = 0
    podiums = 0
    championships = 0

    session = requests.Session()

    # 🔥 1. Tous les résultats (1 requête)
    results_url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit=10000"
    res = session.get(results_url)
    data = res.json()

    races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])

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
    seasons_data = seasons_res.json()

    seasons = seasons_data.get('MRData', {}).get('SeasonTable', {}).get('Seasons', [])

    # 🔥 3. Vérifier champion par saison
    for s in seasons:
        year = s['season']

        standings_url = f"{BASE_URL}/{year}/driverStandings.json"
        res = session.get(standings_url)

        if res.status_code != 200:
            continue

        data = res.json()

        try:
            champion = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][0]

            if champion['Driver']['driverId'] == driver_id:
                championships += 1
        except:
            continue

    return {
        "wins": wins,
        "podiums": podiums,
        "championships": championships
    }


# TEST
stats = get_driver_stats_fast("hamilton")
print(stats)