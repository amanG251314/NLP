# Importing Libaries
from transformers import pipeline
import argparse

def getSentiment(sentences):
    """
    sentences : These are list of sentence on which we want sentiment score
    """
    #Loading Pretrained Model - It includes tokenizer, model etc
    classifier = pipeline("sentiment-analysis",model = "distilbert-base-uncased-finetuned-sst-2-english")

    # predicting sentiment score
    sentiments = classifier(sentences)

    return sentiments

if __name__ == "__main__":

    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='Sentiment analysis on sentences')
    
    # Add argument for sentences
    parser.add_argument('--sentence', nargs='+', type=str, help='Sentences for sentiment analysis separated by commas')
    
    # Parse arguments
    args = parser.parse_args()
    # Check if --sentence argument is provided
    if args.sentence:
        # Join the list of strings into a single comma-separated string
        input_string = ",".join(args.sentence)
        
        # Split the input string by commas to get individual sentences
        sentences_list = [sentence.strip() for sentence in input_string.split(',')]

        # Call the function with the list of sentences
        sentiment_scores = getSentiment(sentences_list)

        # Print sentiment scores
        for sentence, score in zip(sentences_list, sentiment_scores):
            print(f"Sentence: {sentence} | Sentiment: {score['label']} ({score['score']:.4f})")
    else:
        print("No sentences provided. Use --sentence followed by comma-separated sentences.")
