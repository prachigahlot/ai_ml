import re
from collections import defaultdict

def analyze_journal(file_path):
    """Analyze a journal text file and return statistics."""
    
    # Define emotion words to track
    emotion_words = {
        'happy': ['happy', 'joy', 'joyful', 'excited', 'content', 'cheerful', 'delighted'],
        'sad': ['sad', 'unhappy', 'depressed', 'gloomy', 'miserable', 'heartbroken'],
        'angry': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'frustrated'],
        'confused': ['confused', 'uncertain', 'doubtful', 'puzzled', 'bewildered'],
        'afraid': ['afraid', 'scared', 'fearful', 'terrified', 'anxious', 'nervous'],
        'surprised': ['surprised', 'amazed', 'astonished', 'shocked']
    }
    
    # Initialize counters
    stats = {
        'total_lines': 0,
        'total_words': 0,
        'emotion_counts': defaultdict(int),
        'word_counts': defaultdict(int)
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stats['total_lines'] += 1
                
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Clean and split line into words
                words = re.findall(r"\b[\w'-]+\b", line.lower())
                stats['total_words'] += len(words)
                
                # Count each word
                for word in words:
                    stats['word_counts'][word] += 1
                
                # Check for emotion words
                for emotion, variants in emotion_words.items():
                    for variant in variants:
                        if variant in words:
                            stats['emotion_counts'][emotion] += 1
                            break  # count each emotion only once per line
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    
    return stats

def display_results(stats):
    """Display the analysis results in a readable format."""
    if not stats:
        return
    
    print("\n=== Journal Analysis Results ===")
    print(f"Total lines: {stats['total_lines']}")
    print(f"Total words: {stats['total_words']}")
    
    print("\nEmotion Word Counts:")
    for emotion, count in sorted(stats['emotion_counts'].items(), key=lambda x: x[1], reverse=True):
        print(f"- {emotion.capitalize()}: {count}")
    
    print("\nTop 10 Most Frequent Words:")
    top_words = sorted(stats['word_counts'].items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top_words:
        print(f"- {word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to your journal file (.txt): ")
    stats = analyze_journal(file_path)
    
    if stats:
        display_results(stats)