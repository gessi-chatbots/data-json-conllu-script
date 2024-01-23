import json
from io import open


def main():
    with open('datasets/reviews.json', 'r') as t_frex_dataset_file:
        t_frex_reviews = json.load(t_frex_dataset_file)

    with open('datasets/reviews_annotated.txt', "r", encoding="utf-8") as conllu_dataset_file:
        conllu_lines = conllu_dataset_file.readlines()

    ids_conllu_dataset = {line.split('_')[0].split('="')[1] for line in conllu_lines if 'id="' in line}

    common_reviews = []

    for app in t_frex_reviews:
        for review in app['reviews']:
            if review['reviewId'] in ids_conllu_dataset:
                common_reviews.append(review)

    # Temporary, it can be done in the previous line
    with open("results/common_reviews.json", "a") as file:
        for review in common_reviews:
            json.dump(review, file)
            file.write('\n')


if __name__ == '__main__':
    main()
