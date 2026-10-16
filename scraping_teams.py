import json
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests


def scrape_team_results(start_year=1959, end_year=datetime.now().year):
    all_teams = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    print("Iniciando extração dos dados de equipes...")

    for year in range(start_year, end_year + 1):
        url = f"https://www.imo-official.org/results/team/year/{year}/"
        try:
            response = requests.get(url, headers=headers, timeout=12)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find(
                "script", attrs={"data-results-team-year-teams": True}
            )

            if script_tag and script_tag.string:
                teams_data = json.loads(script_tag.string)

                for team in teams_data:
                    scores = team.get("scores") or []
                    awards = team.get("awards") or {}

                    row = {
                        "year": year,
                        "country_code": team.get("code"),
                        "rank": team.get("rank"),
                        "total_points": team.get("total"),
                        "team_size": team.get("teamSize"),
                        # Preenche antecipadamente P1 até P7 com None
                        "p1": None,
                        "p2": None,
                        "p3": None,
                        "p4": None,
                        "p5": None,
                        "p6": None,
                        "p7": None,
                        "gold": awards.get("gold", 0),
                        "silver": awards.get("silver", 0),
                        "bronze": awards.get("bronze", 0),
                        "honourable_mention": awards.get("hm", 0),
                        "leader": team.get("leader"),
                        "deputy_leader": team.get("deputyLeader"),
                        "status": team.get("status"),
                    }

                    # Preenche as pontuações existentes no array
                    for idx, score in enumerate(scores, start=1):
                        row[f"p{idx}"] = score

                    all_teams.append(row)

                print(
                    f"✓ Ano {year}: {len(teams_data)} equipes processadas."
                )

        except Exception as e:
            print(f"✗ Erro ao processar o ano {year}: {e}")

    df = pd.DataFrame(all_teams)

    # Garante a ordem exata das colunas no CSV
    column_order = [
        "year",
        "country_code",
        "rank",
        "total_points",
        "team_size",
        "p1",
        "p2",
        "p3",
        "p4",
        "p5",
        "p6",
        "p7",
        "gold",
        "silver",
        "bronze",
        "honourable_mention",
        "leader",
        "deputy_leader",
        "status",
    ]

    df = df.reindex(columns=column_order)
    df.to_csv("imo_teams.csv", index=False, encoding="utf-8-sig")
    print(
        f"\nConcluído! {len(df)} registros de equipes salvos em 'imo_teams.csv'."
    )


if __name__ == "__main__":
    scrape_team_results()