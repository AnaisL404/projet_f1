import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_driver_stats_fast(driver_id):
    wins = 0
    podiums = 0
    championships = 0

    session = requests.Session()

    # 🔥 Résultats
    results_url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit=10000"
    res = session.get(results_url)

    if res.status_code != 200:
        print("Erreur API résultats :", res.status_code)
        return None

    data = res.json()
    races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])

    for race in races:
        result = race['Results'][0]
        position = result['position']

        if position == "1":
            wins += 1

        if position in ["1", "2", "3"]:
            podiums += 1

    # 🔥 Standings (FIX ICI 👇)
    standings_url = f"{BASE_URL}/driverStandings/1.json?limit=1000"
    res2 = session.get(standings_url)

    if res2.status_code != 200:
        print("Erreur API standings :", res2.status_code)
        return None

    data2 = res2.json()

    lists = data2.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])

    for season in lists:
        try:
            champion = season['DriverStandings'][0]
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