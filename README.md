# Marco Pigna
# Word Frequency Extractor

## Overview
This Python script extracts and counts the occurrences of words from a given webpage. Analyzing word frequencies can be valuable in various applications, including cybersecurity, where identifying significant terms or patterns in textual content may aid in threat analysis, detection, or understanding communication trends.

## Functionality
1. Retrieves the HTML content of the specified URL.
2. Extracts all words from the HTML content using regular expressions.
3. Counts the occurrences of each word, ignoring words with a length less than the specified minimum.
4. Displays the top 10 most frequently occurring words.

## Command-line Options
- `--url` or `-u`: Specifies the URL of the webpage to extract words from (required).
- `--length` or `-l`: Specifies the minimum word length to consider (default: 0).

## Example
- python3 word_extractor.py -u http://google.com -l 5 
- The above will find the top 10 most occuring words on "htt://google.com" with minimum length 5
