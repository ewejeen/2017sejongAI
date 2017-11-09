from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

input_text = "The vehicle - carrying 'several' passengers - collided with a lorry driving at slow speed. Nobody was injured in the incident which city officials say was the fault of the human driver of the lorry. The man was subsequently given a ticket by police."

print("\nSentence Tokenizer:")
print(sent_tokenize(input_text))


print("\nWord Tokenizer : ")
print(word_tokenize(input_text))

print("\nWord Punct Tokenizer : ")
print(WordPunctTokenizer().tokenize(input_text))
