import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def get_all_results(session, driver_id):
    all_races = []
    offset = 0
    limit = 100

    while True:
        url = f"{BASE_URL}/drivers/{driver_id}/results.json?limit={limit}&offset={offset}"
        res = session.get(url)
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

    # 🔥 1. TOUS les résultats (avec pagination)
    races = get_all_results(session, driver_id)

    for race in races:
        result = race['Results'][0]
        position = result['position']

        if position == "1":
            wins += 1

        if position in ["1", "2", "3"]:
            podiums += 1

    # 🔥 2. Saisons
    seasons_url = f"{BASE_URL}/seasons.json?limit=1000"
    seasons_res = session.get(seasons_url)
    seasons_data = seasons_res.json()

    seasons = seasons_data.get('MRData', {}).get('SeasonTable', {}).get('Seasons', [])

    # 🔥 3. Titres
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
stats = get_driver_stats("hamilton")
print(stats)