import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_driver_stats_fast(driver_id):
    wins = 0
    podiums = 0
    championships = 0

    # 🔥 1. Tous les résultats du pilote (UNE requête)
    results_url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit=10000"
    results = requests.get(results_url).json()

    races = results['MRData']['RaceTable']['Races']

    for race in races:
        result = race['Results'][0]
        position = result['position']

        if position == "1":
            wins += 1

        if position in ["1", "2", "3"]:
            podiums += 1

    # 🔥 2. Toutes les standings (UNE requête)
    standings_url = f"{BASE_URL}/driverStandings/1.json?limit=1000"
    standings = requests.get(standings_url).json()

    lists = standings['MRData']['StandingsTable']['StandingsLists']

    for season in lists:
        champion = season['DriverStandings'][0]
        if champion['Driver']['driverId'] == driver_id:
            championships += 1

    return {
        "wins": wins,
        "podiums": podiums,
        "championships": championships
    }


# 🔥 Test
stats = get_driver_stats_fast("hamilton")

print(stats)