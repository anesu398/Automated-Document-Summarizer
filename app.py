import argparse
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Function to generate document summary
def generate_summary(text, length):
    sentences = sent_tokenize(text)
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

    # Calculate TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)

    # Calculate sentence scores based on cosine similarity
    sentence_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix).flatten()

    # Sort sentences by score and select top sentences for summary
    ranked_sentences = sorted(((score, sentence) for score, sentence in zip(sentence_scores, sentences)), reverse=True)
    summary_sentences = [sentence for _, sentence in ranked_sentences[:length]]

    return '\n'.join(summary_sentences)

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Automated Document Summarizer')
    parser.add_argument('--input_file', required=True, help='Path to input document file')
    parser.add_argument('--output_file', required=True, help='Path to save the generated summary')
    parser.add_argument('--length', type=int, required=True, help='Length of the summary (number of sentences)')
    args = parser.parse_args()

    # Read input document
    with open(args.input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Generate summary
    summary = generate_summary(text, args.length)

    # Save summary to output file
    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(summary)

if __name__ == "__main__":
    main()
