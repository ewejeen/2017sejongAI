python
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

input_reviews = ["It won BEST FILM, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. JUST BRILLIANT."
    ]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)

    probabilities = classifier.prob_classify(extract_features(review.split()))

    predicted_sentiment = probabilities.max()

    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))
