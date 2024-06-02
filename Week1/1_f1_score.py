def exercise1(tp, fp, fn):
    if not all(isinstance(i, int) for i in [tp, fp, fn]):
        print("tp, fp, fn must be int")

    if not all(tp>0, fp>0, fn>0):
        print("tp, fp, fn must be greater than zero")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1_score}')