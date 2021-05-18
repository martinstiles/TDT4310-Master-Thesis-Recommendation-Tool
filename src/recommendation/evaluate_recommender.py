"""
This is the code to find precision and recall (F-score) for the recommender,
based on the labeled data we have made.

eval_data = [
    {
        "query": ["...", ..],
        "relevance": [id, relevance]  # relevance --> 0 = not relevant, 1 = relevant,
        "language": "en" / "no"
    }
]
"""

from recommender import load_stemmed_data, recommender
import json


def load_data():
    with open("src/recommendation/evaluation_data.json") as file:
        data = json.load(file)
        eval_set_ids = [str(thesis_id) for thesis_id in data["thesis_ids"]]
        eval_data = data["relevance_data"]
        return eval_set_ids, eval_data


def get_f_score(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * precision * recall / (precision + recall)


def get_average(array):
    return sum(array) / len(array)


def main():
    # Load and join data
    stemmed_data = load_stemmed_data()
    eval_set_ids, eval_data = load_data()

    # Extract the stemmed data corresponding to the thesis_ids of the evaluation subset
    eval_subset = {key: value for (
        key, value) in stemmed_data.items() if key in eval_set_ids}

    # store the values so that we can compute average
    precision_values = []
    recall_values = []
    f_score_values = []

    for eval_object in eval_data:
        # relevant_ids is the positives
        query, relevant_ids, language = eval_object["query"], eval_object["relevant_ids"], eval_object["language"]
        relevant_ids = [str(thesis_id) for thesis_id in relevant_ids]
        
        # n represents the (maximum) number of theses the recommender will recommend
        # Can be tweaked to check the impact it has on precision and recall measurements
        n = 15

        # Get the recommendations based on the query
        recommendations = recommender(query, language, n, eval_subset)

        # Only retrieve the ids that also is in the subset (in case we use the entire data set for tf-idf)
        selected_ids = [obj["id"]
                        for obj in recommendations if obj["id"] in eval_set_ids]

        # The true posivies: selected and relevant
        true_positives = [
            thesis_id for thesis_id in selected_ids if thesis_id in relevant_ids]

        # compute every measurment
        precision = len(true_positives) / \
            n if len(selected_ids) > 0 else 0
        recall = len(true_positives) / len(relevant_ids)
        f_score = get_f_score(precision, recall)

        print("QUERY:", query)
        print("P = ", round(precision, 2))
        print("R = ", round(recall, 2))
        print("F = ", round(f_score, 2))
        print("")

        precision_values.append(precision)
        recall_values.append(recall)
        f_score_values.append(f_score)

    total_precision = get_average(precision_values)
    total_recall = get_average(recall_values)
    total_f_score = get_average(f_score_values)

    print("\nTOTAL:")
    print("Precision:", round(total_precision, 2))
    print("Recall:   ", round(total_recall,2))
    print("F-score:  ", round(total_f_score, 2))


if __name__ == "__main__":
    main()
