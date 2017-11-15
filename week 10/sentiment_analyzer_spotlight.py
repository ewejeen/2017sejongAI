from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

def extract_features(words):
    return dict([(word, True) for word in words])


if __name__=='__main__':
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    features_pos = [(extract_features(movie_reviews.words(
        fileids=[f])), 'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(
        fileids=[f])), 'Negative') for f in fileids_neg]

threshold = 0.8
num_pos = int(threshold * len(features_pos))
num_neg = int(threshold * len(features_neg))

features_train = features_pos[:num_pos] + features_neg[:num_neg]
features_test = features_pos[num_pos:] + features_neg[num_neg:]

print('\nNumber of training datapoints:', len(features_train))
print('Number of test datapoints:', len(features_test))

classifier = NaiveBayesClassifier.train(features_train)
print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test))

N = 15
print('\nTop ' + str(N) + ' most informative words:')
for i, item in enumerate(classifier.most_informative_features()):
    print(str(i+1) + '. ' + item[0])
    if i == N - 1:
        break

input_reviews = [
    "Everything about this movie is outstanding -- the performances, the way the true events are handled, the cinematography. ",
    "In this day of digital news, this movie makes us stand back and realize what we may lose in the way of investigative journalism as we slowly kill off print media.",
    "The lengths the directors go to to achieve a sense of authenticity is remarkable. ",
    "We are there in Boston in 2001-2002. We get to know enough about each character to make him or her real, but not enough to create side dramas. ",
    "The focus remains the child abuse scandal in the archdiocese in Boston.",
    "That reflects the conflict the characters face and deal with when events make them rethink the focus of their article.",
    "The movie is riveting, though we know the outcome."
    ]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)

    probabilities = classifier.prob_classify(extract_features(review.split()))

    predicted_sentiment = probabilities.max()

    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))
