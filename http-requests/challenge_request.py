import requests
from random import choice


def get_joke(term):
    response_json = requests.get(
        "https://icanhazdadjoke.com/search",
        headers={"Accept": "application/json"},
        params={"term": term}
    ).json()

    return response_json


def print_jokes(term):
    jokes = get_joke(term)
    results = jokes["results"]
    total_jokes = jokes["total_jokes"]

    if total_jokes > 1:
        print(
            f"I've got {total_jokes} jokes about {term}. Here's one:\n",
            choice(results)['joke']
        )
    elif total_jokes == 1:
        print(
            f"I've got one joke about {term}. Here it is:\n",
            results[0]['joke']
        )
    else:
        print(f"Sorry, I don't have any jokes about {term}! Please try again.")


if __name__ == '__main__':
    term = input("Let me tell you a joke! Give me a topic: ")
    print_jokes(term)
