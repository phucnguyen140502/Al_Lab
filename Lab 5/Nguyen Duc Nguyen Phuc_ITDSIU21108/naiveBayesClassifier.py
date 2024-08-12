import pandas as pd
import numpy as np
import sys


class NaiveBayesFilter:
    def __init__(self):
        self.data = []
        self.vocabulary = []  # returns tuple of unique words
        self.p_spam = 0  # Probability of Spam
        self.p_ham = 0  # Probability of Ham
        # Initiate parameters
        self.parameters_spam = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_spam: ', self.parameters_spam)
        self.parameters_ham = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_ham: ', self.parameters_spam)

    def fit(self, X, y):
        # creating vocabulary and cleaning set
        for sms in X:
            for word in sms:
                self.vocabulary.append(word)

        # Set returns tuple of unique words
        self.vocabulary = list(set(self.vocabulary))

        # Create a default dictionary with each unique word a count of zero
        word_count_per_sms = {unique_word: [0] * len(X)
                              for unique_word in self.vocabulary}

        # Loop over the training set and count the number of times each unique word occurs
        for index, sms in enumerate(X):
            for word in sms:
                word_count_per_sms[word][index] += 1

        word_counts = pd.DataFrame(word_count_per_sms)

        self.data = pd.concat([X, word_counts, y], axis=1)
        print(self.data)

        # Isolating spam and ham messages first
        spam_messages = self.data[self.data['Label'] == 'spam']
        ham_messages = self.data[self.data['Label'] == 'ham']

        # P(Spam) and P(Ham)
        self.p_spam = len(spam_messages) / len(X)
        self.p_ham = len(ham_messages) / len(X)

        # N_Spam
        n_words_per_spam_messages = spam_messages['SMS'].apply(len)
        n_spam = n_words_per_spam_messages.sum()

        # N_Ham
        n_words_per_ham_messages = ham_messages['SMS'].apply(len)
        n_ham = n_words_per_ham_messages.sum()

        # N_Vocabulary
        n_vocabulary = len(self.vocabulary)

        print('Number of words in spam messages is: ' + str(n_spam) + '\n')
        print('Number of words in ham messages is: ' + str(n_ham) + '\n')
        print('Number of unique words are: ' + str(n_vocabulary))

        # Calculate parameters
        for word in self.vocabulary:
            # spam_messages already defined in a cell above
            n_word_given_spam = spam_messages[word].sum()
            p_word_given_spam = (n_word_given_spam / n_spam)
            self.parameters_spam[word] = p_word_given_spam

            # ham_messages already defined in a cell above
            n_word_given_ham = ham_messages[word].sum()
            p_word_given_ham = (n_word_given_ham / n_ham)
            self.parameters_ham[word] = p_word_given_ham

        return self.data

    def predict(self, X):
        prob = []
        print('Length of test data: ', len(X))
        predict_label = []
        for sms in X:
            for word in sms:
                p_s = self.p_spam
                p_h = self.p_ham
                if word in self.parameters_spam:
                    p_s *= self.parameters_spam[word]
                if word in self.parameters_ham:
                    p_h *= self.parameters_ham[word]
                prob.append([round(p_h, 8), round(p_s, 8)])
        np.set_printoptions(threshold=sys.maxsize)

        label = ['ham', 'spam']
        for i in range(0, len(X)):
            predict_label.append(label[np.argmax(prob[i])])
        print(predict_label)
        return predict_label

    def predict_proba(self, X):
        proba = []
        for sms in X:
            for word in sms:
                p_s = self.p_spam
                p_h = self.p_ham
                if word in self.parameters_spam:
                    p_s *= self.parameters_spam[word]
                if word in self.parameters_ham:
                    p_h *= self.parameters_ham[word]
                proba.append([round(p_h, 8), round(p_s, 8)])
        np.set_printoptions(threshold=sys.maxsize)
        return proba

    def score(self, true_labels, predict_labels):
        match = [i for i, j in zip(true_labels, predict_labels) if i == j]
        recall = len(match) / len(true_labels)
        return recall