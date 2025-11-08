#Step 1: Text Cleaning and Preprocessing
import string

def clean_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase

    start = text.find('*** START')
    end = text.find('*** END')

    if start != -1 and end != -1:
        text = text[start:end]

    #to remove punctuations
    for char in string.punctuation:
        text = text.replace(char, '')

    #to remove digits
    for char in '0123456789':
        text = text. replace(char,'')

    words = text.split()
    return ' '.join(words)

#Step 2: Removing stop words
import nltk
from nltk.corpus import stopwords

# nltk.download('stopwords') #Uncomment this line if you haven't downloaded the stopwords corpus yet

def remove_stop_words(text):
    """Removes stop words from the files."""
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)


#Step 3: Word Frequency Analysis
def word_frequency(text):
    freq_dict = {}
    words = text.split()

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict

#Step 4:Commuting Summary Statistics - understood how to create it with AI
def print_top_words(freq_dict, title, top_n = 10):
    """Prints the top N most common words in the text."""
    items = list(freq_dict.items())
    items.sort(key=lambda x: x[1], reverse=True)

    print(f"Top {top_n} most common words in {title}:")
    for word, freq in items [:top_n]:
        print(f"{word}: {freq}")

def summary_statistics(text, freq_dict):
    """Compute key statistics for a given piece of text, such as total words, 
    unique words, average word length and vocabulary richness."""

    total_words = len(text.split())

    #number of unique words
    unique_words = len(freq_dict)

    #Average word length
    total_chars = sum(len(word) * count for word, count in freq_dict.items())
    avg_word_length = total_chars / total_words if total_words > 0 else 0

    #Vocabulary richness, so what percentage of the total words are unique
    vocab_richness = unique_words / total_words if total_words > 0 else 0

    return total_words, unique_words, avg_word_length, vocab_richness

def compare_vocabulary(freq1, freq2):
    """Return words that appear in text 1, but not text 2"""

    unique_to_text1 = set(freq1.keys()) - set(freq2.keys())
    return list(unique_to_text1)

def print_summary(title, text, freq_dict):
    """Print summary statistics for a given text."""
    total_words, unique_words, avg_word_length, vocab_richness = summary_statistics(text, freq_dict)
    print(f"Summary statistics for {title}:")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Vocabulary richness: {vocab_richness:.2%}")

#Created with AI:
import matplotlib.pyplot as plt

def plot_top_words(freq_dict, title, top_n=10):
    """
    Plot a simple bar chart showing the top N most common words in the text.
    """
    items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words = [word for word, freq in items]
    frequencies = [freq for word, freq in items]

    plt.figure(figsize=(10, 5))
    plt.bar(words, frequencies, color='blue')
    plt.title(f'Top {top_n} Most Common Words in {title}')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


### Optional Technique 1: Natural Language Processing (NLP) 

nltk.download('vader_lexicon') #used AI to understand how to use the VADER lexicon for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text, title):
    """Analyze the sentiment of the given text."""

    SIA = SentimentIntensityAnalyzer()
    sentences = text.split('.')

    total_positive, total_negative, total_neutral, total_compound = 0, 0, 0, 0
    count = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 3: #To skip empty or very short sentences
            scores = SIA.polarity_scores(sentence)
            total_positive += scores['pos']
            total_negative += scores['neg']
            total_neutral += scores['neu']
            total_compound += scores['compound']
            count += 1
        
    if count == 0:
        print(f"No sentences found for {title}.")
        return
        
    avg_positive = total_positive / count
    avg_negative = total_negative / count
    avg_neutral = total_neutral / count
    avg_compound = total_compound / count

    print(f"Sentiment analysis for {title}:")
    print(f"Average Positive: {avg_positive:.2f}")
    print(f"Average Negative: {avg_negative:.2f}")
    print(f"Average Neutral: {avg_neutral:.2f}")
    print(f"Average Compound: {avg_compound:.2f}")



def main():
    time_machine_text = clean_text("pg35.txt")
    lost_world_text = clean_text("pg139.txt")

    time_machine_text = remove_stop_words(time_machine_text)
    lost_world_text = remove_stop_words(lost_world_text)

    time_machine_freq = word_frequency(time_machine_text)
    lost_world_freq = word_frequency(lost_world_text)

    print_top_words(time_machine_freq, "The Time Machine")
    print_top_words(lost_world_freq, "The Lost World")

    print_summary("The Time Machine", time_machine_text, time_machine_freq)
    print_summary("The Lost World", lost_world_text, lost_world_freq)

    diff_words = compare_vocabulary(time_machine_freq, lost_world_freq)
    print(f"Words that appear in The Time Machine but not in The Lost World: {len(diff_words)}")
    print(diff_words[:10])  # Print the first 10 unique words for testing

    plot_top_words(time_machine_freq, "The Time Machine")
    plot_top_words(lost_world_freq, "The Lost World")

    print("Sentiment Analysis:")
    analyze_sentiment(time_machine_text, "The Time Machine")
    analyze_sentiment(lost_world_text, "The Lost World")

if __name__ == "__main__":
    main()

main()