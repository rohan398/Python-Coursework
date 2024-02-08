# Student Number : 22031444
import re
import numpy as np


def getwordssequence(words_file):
  """
    DEFINITION :  This function reads the contents of alice_words.txt which has characters in UPPER CASE separated by <SEP> in each line.
                  It removes the <SEP> from each line and returns list of strings (each line) in lower case.

    INPUT(s) :
          1. words_file : Name of the file

    OUTPUT(s) :
        list of word_sequences in lower case separated by delimiter <SEP>.

    EXAMPLE USAGE :
        w = getwordssequence('alice_words.txt')

    """
  all_lines = open(words_file, 'r').readlines()
  words_sequences = [[i.lower() for i in each_line.strip().split("<SEP>")] for each_line in all_lines]
  return words_sequences


def gettagssequence(tagged_file):
  """
    DEFINITION :   This function reads the contents of alice_tags.txt which has characters in UPPER CASE separated by <SEP> in each line.
                  It removes the <SEP> from each line and returns list of strings (each line) in lower case.

    INPUT(s) :
          1. tagged_file : Name of the file

    OUTPUT(s) :
        list of tags_sequence in lower case separated by delimiter <SEP>.

    EXAMPLE USAGE :
        t = gettagssequence('alice_tags.txt')

    """
  all_lines = open(tagged_file, 'r').readlines()
  tags_sequences = [each_line.strip().replace("<SEP>", "").lower() for each_line in all_lines]
  return tags_sequences


def find_positions(tags_sequences):
  """
    DEFINITION :  This function is to find the position of the noun phrases from the tagged sequences.

    INPUT(s) :
        1. tags_sequences : tags_sequences which are calculated in the gettagssequence(tagged_file) function.

    OUTPUT(s) :
        list of (list of tuple) of the matched pattern.

    EXAMPLE USAGE :
        t=gettagssequence('alice_tags.txt')
        m = find_positions(t)
    """
  positions = list()
  pattern = re.compile(r'[jn]?n')
  for seq in tags_sequences:
    each_seq_positions = list()
    for m in pattern.finditer(seq):
      each_seq_positions.append((m.start(), m.end()))
    positions.append(each_seq_positions)

  return positions


def find_noun_phrase(input_word, matches_list, words_sequences):
  """
    DEFINITION : This function takes as input one input word (input_word string), and
                the variables matches_list and words_sequences, and prints all noun phrases containing that word
                as well as the sentence number (starting counting from one, and not by zero, which would be the
                default in Python) in which they appear, formatted like this: sentence_id:noun_phrase.

                This function finds the noun phrases with the provided input parameters -> input_word, matches_list and
                word_sequences got from the file alice_words.txt. It prints all the noun phrases containing that word
                as well as the sentence number in the format: sentence_id:noun_phrase.

    INPUT(s) :
        1. input_word : word that needs to be searched.
        2. matches_list : list of (list of tuple) of the matched pattern (output from the find_positions function).
        3. words_sequences : list of list of word_sequences ( output from the getwordssequence function)

    OUTPUT(s) :
        Print the noun phrases containing the input_word.

    EXAMPLE USAGE :
        find_noun_phrases('disappointment', find_positions(tags_sequences), getwordssequence('alice_words.txt'))

    """
  for seq in range(len(words_sequences)):
    if input_word in words_sequences[seq]:
      seq_id = seq + 1
      for phrase in matches_list[seq]:
        if phrase[0] < words_sequences[seq].index(input_word) < phrase[1]:
          print("{}:{}".format(seq_id, " ".join(words_sequences[seq][phrase[0]: phrase[1]])))