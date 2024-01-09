import requests
import click 
import re
from bs4 import BeautifulSoup

#function to print the top 10 occurences of a word with minimum length
def print_top_occurences(sorted_occurences, top_n):
    
    #error handling for extended minimum length
    if len(sorted_occurences) < 10:
        print("Top 10 not found. Please change minimum length and try again!")
        return
    
    for i in range(top_n):
        print(sorted_occurences[i][0] + " " + str(sorted_occurences[i][1]) + " occurence(s)")   
    
        
#function that creates a dictionary of word occurences
def create_dictionary(all_words, min_length):
    html_dict = {}
    for word in all_words:
        if len(word) < min_length:
            continue
        if word not in html_dict:
            html_dict[word] = 1
        else:
            html_dict[word] +=1   
    return html_dict

#function that uses BeautifulSoup object to extract text and create list of all words
def get_words(html_doc):
    #create beautiful soup object with html content
    soup = BeautifulSoup(html_doc, 'html.parser')
    #gets all text omitting html tags/metadata
    text_only = soup.get_text()
    #uses regex to find all words in text
    all_words = re.findall(r'\w+', text_only)
    #return list of words
    return all_words
       
#method that prints html content based on passed url
def get_html(target_url):
    try:
        #get information from passed url
        resp = requests.get(target_url)
    except requests.exceptions.RequestException:
        print("This URL is not reachable. Exiting....")
        exit(1)
    return resp.content.decode()

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Specifies the minimum word length to consider (default: 0)')

def main(url, length):
    #get word list
    list_of_words = get_words(get_html(url))
    #create dictionary using word list includes word + number of occurrences
    occurence_dictionary = create_dictionary(list_of_words, length)
    #order the occurence dictionary
    sorted_dictionary = sorted(occurence_dictionary.items(), key = lambda x: x[1], reverse = True)
    #print top 10 occurrences 
    print_top_occurences(sorted_dictionary,10)
    
if __name__ == '__main__':
    main()