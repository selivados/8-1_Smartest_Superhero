import requests


def choose_smartest_superhero(compared_superheroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    superheroes = requests.get(url).json()
    result = []
    for superhero in superheroes:
        if superhero['name'] in compared_superheroes:
            info = (superhero['name'], superhero['powerstats']['intelligence'])
            result.append(info)
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    print(f'Самый умный супергерой - {sorted_result[0][0]}, его интеллект равен {sorted_result[0][1]}.')


if __name__ == '__main__':
    choose_smartest_superhero(['Hulk', 'Captain America', 'Thanos'])
