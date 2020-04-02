from sklearn.ensemble import RandomForestClassifier
from mido import MidiFile
import dataset

def test_model(model, x_test, y_test):
    """Tests the model provided and reports accuracy to output"""

    # Predict targets
    targets_predicted = model.predict(x_test)

    # Check accuracy
    total = len(y_test)
    accuracy = sum([1 if target == prediction else 0 for target, prediction in zip(y_test, targets_predicted)])

    print("\t{} objects tested. Total accuracy: {:.2f}%".format(
    total, accuracy / total * 100))

#classifier = RandomForestClassifier()
#classifier.fit(dataset.x_train, dataset.y_train)

#test_model(classifier, dataset.x_test, dataset.y_test)
