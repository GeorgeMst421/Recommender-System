from math import sqrt
from math import pow

def jaccard_similarity(dict_1: dict, dict_2: dict):
    set_1 = set(dict_1.keys())
    set_2 = set(dict_2.keys())

    # Calculate intersection and union of sets
    intersection = set_1.intersection(set_2)
    union = set_1.union(set_2)

    # Calculate Jaccard similarity
    similarity = len(intersection) / len(union) if len(union) != 0 else 0.0

    return round(similarity, 2)


def dice_similarity(dict_1: dict, dict_2: dict):
    set_1 = set(dict_1.keys())
    set_2 = set(dict_2.keys())

    # Calculate intersection and sum of cardinalities of sets
    intersection = set_1.intersection(set_2)
    cardinality_sum = len(set_1) + len(set_2)

    # Calculate Dice similarity
    similarity = (2 * len(intersection) / cardinality_sum) if cardinality_sum != 0 else 0.0

    return round(similarity, 2)


def cosine_similarity(dict_1: dict[int:float], dict_2: dict[int:float]):
    common_items = [item_id for item_id in dict_1 if item_id in dict_2]

    if not common_items:
        return 0.0

    numerator = sum(dict_1[item_id] * dict_2[item_id] for item_id in common_items)

    magnitude_1 = sqrt(sum(pow(value, 2) for value in dict_1.values()))
    magnitude_2 = sqrt(sum(pow(value, 2) for value in dict_2.values()))
    similarity = numerator / (magnitude_1 * magnitude_2) if magnitude_1 * magnitude_2 != 0 else 0.0

    return round(similarity, 2)


def pearson_similarity(dict_1: dict[int: float], dict_2: dict[int: float]):
    common_items = [item_id for item_id in dict_1 if item_id in dict_2]

    if not common_items:
        return 0.0

    mean_1 = sum(dict_1.values()) / len(dict_1)
    mean_2 = sum(dict_2.values()) / len(dict_2)

    new_dict_1, new_dict_2 = {}, {}
    for id_ in dict_1:
        new_dict_1[id_] = dict_1[id_] - mean_1
    for id_ in dict_2:
        new_dict_2[id_] = dict_2[id_] - mean_2

    return cosine_similarity(new_dict_1, new_dict_2)

