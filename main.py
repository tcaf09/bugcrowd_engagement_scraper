import requests
import json

def fetch_engagements(page):
    url = "https://bugcrowd.com/engagements-us.json?category=bug_bounty&sort_by=rewards&sort_direction=asc"
    res = requests.get(f'{url}&page={page}')
    json = res.json()
    engagements = json['engagements']
    return engagements

def main():
    page = 0
    engagements = fetch_engagements(page)
    total = engagements
    print(f'Page: {page}')
    page += 1
    while engagements != []:
        engagements = fetch_engagements(page)
        total.extend(engagements)
        print(f'Page: {page}')
        page += 1
    filtered = map(
        lambda x: {
            'name': x['name'], 
            'rewardSummary': x['rewardSummary'], 
            'productEngagementType': x['productEngagementType'],
            'scopeRank': x['scopeRank']
        },
        total
    )
    with open('output.json', 'w') as file:
        pretty = json.dumps(list(filtered), indent=4)
        file.write(pretty)



if __name__ == "__main__":
    main()
