import json
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests


def scrape_individual_results(start_year=1959, end_year=datetime.now().year):
    all_contestants = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    print("Iniciando extração dos dados individuais...")

    for year in range(start_year, end_year + 1):
        url = f"https://www.imo-official.org/results/individual/year/{year}/"
        try:
            response = requests.get(url, headers=headers, timeout=12)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # Busca a tag script pelo atributo específico de participantes
            script_tag = soup.find(
                "script",
                attrs={"data-results-individual-year-contestants": True},
            )

            if script_tag and script_tag.string:
                contestants_data = json.loads(script_tag.string)

                for person in contestants_data:
                    scores = person.get("scores") or []

                    # Monta o nome completo
                    first_name = person.get("name", "")
                    last_name = person.get("surname", "")
                    full_name = f"{first_name} {last_name}".strip()

                    row = {
                        "year": year,
                        "contestant_id": person.get("contestantId"),
                        "participation_id": person.get("participationId"),
                        "name": full_name,
                        "country_code": person.get("countryCode"),
                        "rank": person.get("rank"),
                        "total_points": person.get("total"),
                        "award": person.get("award"),
                        "is_anonymous": person.get("isAnonymous"),
                    }

                    # Adiciona dinamicamente as pontuações de cada problema (P1, P2, ...)
                    for idx, score in enumerate(scores, start=1):
                        row[f"p{idx}"] = score

                    all_contestants.append(row)

                print(
                    f"✓ Ano {year}: {len(contestants_data)} participantes processados."
                )

        except Exception as e:
            print(f"✗ Erro ao processar o ano {year}: {e}")

    df = pd.DataFrame(all_contestants)
    df.to_csv("imo_individual.csv", index=False, encoding="utf-8-sig")
    print(
        f"\nConcluído! {len(df)} registros individuais salvos em 'imo_individual.csv'."
    )


if __name__ == "__main__":
    scrape_individual_results()