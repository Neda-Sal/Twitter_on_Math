import pandas as pd
import emoji
import regex as re

from googletrans import Translator
from langdetect import detect


def remove_usernames(post):
    '''
    Function that takes in a string and removes any words with the symbol @ in it. Use this in a list comprehension.
    ---
    Input: <string>
    ---
    Returns: <string>
    '''
    
    post = post.split()
    to_remove = [word for word in post if '@' in word]    
    
    for word in to_remove:
        post.remove(word)

    return ' '.join(post)





def emoji_to_words(df, column):
    '''
    Function that changes emojis into their words descriptions, and adds a new column to the dataframe
    ---
    Input: <DataFrame> 
           <string> the column that you want to change
    ---
    Returns: adds the changed column to the df
    '''
    
    changed_list = [emoji.demojize(post, delimiters=("", "")) for post in df[column]]
    
    df[column + '_word_emojis'] = changed_list
    
    return df


def remove_non_eng_chars(df, column):
    '''
    Function that removes non english characters, and adds a new column to the dataframe
    ---
    Input: <DataFrame> 
           <string> the column that you want to change
    ---
    Returns: adds the changed column to the df
    '''
    
    df[column + '_eng_letters_only'] = df[column].str.replace(r'[^\x00-\x7F]+', '')
    
    return df



def removes_emojis_and_spec_chars(df, column):
    '''
    Function that removes special characters (#@/:%.,_-?!), and emojis. Adds a new column to the dataframe
    ---
    Input: <DataFrame> 
           <string> the column that you want to change
    ---
    Returns: adds the changed column to the df
    '''
    
    
    df[column + '_no_emojis_spec_chars'] = df[column].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
    
    return df



def change_langs(df, column):
    '''
    Function that translates all the posts in the dataframe column
    ---
    Input: <DataFrame> 
           <string> the column that you want to translate
    ---
    Returns: a list of the translated columns
    '''
    
    translator = Translator()
    english = [translator.translate(post).text for post in df[column]]
    
    return english
    
    












