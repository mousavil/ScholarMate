

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from textblob import Word
from textblob import TextBlob
import string
import nltk
import re
from nltk import tokenize, PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def correct_sentence_spelling(sentence):
    sentence = TextBlob(sentence)
    result = sentence.correct()
    return result

def correct_word_spelling(word):
    word = Word(word)
    result = word.correct()
    return result


def remove_html_tag(df):
    df['academic_req'] = df['academic_req'].str.replace(r'<[^<>]*>', '', regex=True)

def remove_punctuation(df):
    list_of_col = ['structure',
                   'academic_req',
                   'facts',
                   'city',]
    for col in list_of_col:
        df[col] = df[col].str.replace(r'[^\w\s]+', '')

def lower_case_data(df):
    list_of_col = ['country_name',
                   'university_name',
                   'program_name',
                   'program_type',
                   'language',
                   'structure',
                   'academic_req',
                   'facts',
                   'city', ]
    for col in list_of_col:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.lower()


def replace_null_data(df):
    average_ielts_score_each_country = dict()
    for (i, x) in enumerate(df['country_name']):
        average_ielts_score_each_country[x] = [0, 0, 0]

    for (i, x) in enumerate(df['country_name']):
        if not pd.isnull(df['ielts_score'][i]):
            average_ielts_score_each_country[x][0] += df['ielts_score'][i]
            average_ielts_score_each_country[x][1] += 1

    mean = df["ielts_score"].mean()
    for country in average_ielts_score_each_country:
        a = average_ielts_score_each_country[country][0]
        b = average_ielts_score_each_country[country][1]
        if b > 0:
            average_ielts_score_each_country[country][2] = a/b
        else:
            average_ielts_score_each_country[country][2] = mean

    for (i, x) in enumerate(df['ielts_score']):
        if pd.isnull(df.loc[i, 'ielts_score']):
            country = df.at[i, 'country_name']
            df.at[i, 'ielts_score'] = average_ielts_score_each_country[country][2]


def remove_noisy_data(df):
    program_count = dict()
    for x in df['program_type']:
        if pd.notnull(x):
            program_count[x] = 0

    for x in df['program_type']:
        if pd.notnull(x):
            program_count[x] += 1

    for (i, x) in enumerate(df['program_type']):
        if program_count[x] < 3:
            df.drop(i, inplace=True)

    df.reset_index(drop=True, inplace=True)





def program_description(df, id):
    i = id
    des = ""
    des += df['country_name'][i] + '\n'
    des += df['university_name'][i] + '\n'
    des += df['program_name'][i] + '\n'
    des += df['program_type'][i] + '\n'
    des += str(df['duration'][i]) + '\n'
    des += df['language'][i] + '\n'
    des += "total tution : " + str(df['total_tution'][i]) + '\n'
    des += "ielts score needed : " + str(df['ielts_score'][i]) + '\n'
    des += df['structure'][i] + '\n'
    return des



def tokenize_data(df):
    nltk.download('punkt')
    nltk.download('wordnet')

    df['search_token'] = 'a'

    for (i, a) in enumerate(df['country_name']):
        if i % 1000 == 0:
            print('search_token', i)
        b = df['university_name'][i]
        c = df['program_name'][i]
        st = a + ' ' + b + ' ' + c
        df.at[i, 'search_token'] = nltk.word_tokenize(st)


    df['extracted_tokens'] = 'b'
    for (i, a) in enumerate(df['country_name']):
        if i % 1000 == 0:
            print('extracted_tokens', i)
        b = df['university_name'][i]
        c = df['university_rank'][i]
        d = df['program_name'][i]
        e = df['program_type'][i]
        f = df['language'][i]
        g = df['structure'][i]
        if pd.isnull(c):
            c = ""
        if pd.isnull(d):
            d = ""
        if pd.isnull(e):
            e = ""
        if pd.isnull(f):
            f = ""
        if pd.isnull(g):
            g = ""

        st = a+' '+b+' '+str(c)+' '+d+' '+e+' '+f+' '+g
        df.at[i, 'extracted_tokens'] = nltk.word_tokenize(st)





def remove_stop_words(df):
    nltk.download('stopwords')

    for (i, tok) in enumerate(df['extracted_tokens']):
        if i % 1000 == 0:
            print('stopword', i)
        new_token_list = [t for t in tok if not t in stopwords.words("english")]
        df.at[i, 'extracted_tokens'] = new_token_list




def generate_wordcould(df):
    text = ""
    for tok in df['extracted_tokens']:
        for x in tok:
            text += x
            text += ' '

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=5).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()



def calculate_total_tution(df):
    df['total_tution'] = 0
    df['tution_permonth'] = 0.0
    for (i, a) in enumerate(df['duration']):
        st = df['tuition_price_specification'][i]
        tt = df['tution_1_money'][i]
        currency = df['tution_1_currency'][i]
        if pd.isnull(a) or pd.isnull(st) or pd.isnull(tt) or pd.isnull(currency):
            continue

        zarib = 1
        if 'months' in a:
            a = a.replace('months', '')

        elif 'month' in a:
            a = a.replace('month', '')

        elif 'days' in a:
            a = a.replace('days', '')
            zerib = 30


        mo = int(a)
        mo = (mo + zarib-1) // zarib

        money1 = int(tt)
        money2 = money1
        tmp = df['tution_2_money'][i]
        total = 0
        if pd.notnull(tmp):
            money2 = int(tmp)

        if 'Full' in st:
            total = money1

        if 'Year' in st:
            total = money1 + ((mo//12)-1)*money2

        if 'Semester' in st:
            total = money1 + ((mo//6)-1)*money2

        if 'Module' in st:
            total = money1 + ((mo//6)-1)*money2

        if 'Credit' in st:
            total = money1 + ((mo//6)-1)*money2

        if 'Trimester' in st:
            total = money1 + ((mo//4)-1)*money2

        if 'Quarter' in st:
            total = money1 + ((mo//3)-1)*money2

        if 'Month' in st:
            total = money1 + (mo-1)*money2

        total = max(total, 0)

        if 'EUR' in currency:
            total *= 1.08514

        if 'CAD' in currency:
            total *= 0.740107

        if 'GBP' in currency:
            total *= 1.23383

        if 'AUD' in currency:
            total *= 0.668356

        df.at[i, 'total_tution'] = total
        df.at[i, 'tution_permonth'] = total/mo




def lemmatization_data(word):
    lemmetizer = WordNetLemmatizer()
    return lemmetizer.lemmatize(word)


def stemming_data(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word)


def tution_boxplot_diagram(df):
    Y = df['tution_permonth'].values
    Y = Y[np.nonzero(Y)]
    q1 = np.quantile(Y, 0.25)
    q3 = np.quantile(Y, 0.75)
    x1, y1 = [-200, 48000], [1.5*(q3-q1) + q3, 1.5*(q3-q1) + q3]
    plt.plot(x1, y1, marker='o')
    plt.plot(Y, 'bo', ms=2)
    plt.show()


def get_input(university_name,program_name,resume):
    a = university_name
    b = program_name
    c = resume
    key_words = c.split(',')
    a = correct_sentence_spelling(a)
    b = correct_sentence_spelling(b)
    a = str(a)
    b = str(b)
    a = a.lower()
    b = b.lower()
    serch_words = nltk.word_tokenize(a+" "+b)
    return (key_words, serch_words)


def search_program(df, keywords, serch_words):
    point_list = []
    for (i, x) in enumerate(df['search_token']):
        point = 0
        for y in serch_words:
            if y in x:
                point += 1

        if point > 0:
            point_list.append((point, i))

    point_list.sort()
    l = point_list[-5:]
    l.reverse()
    id = 1
    for (p,i) in l:
        print("OPTION " + str(id) + " )")
        id += 1
        print(program_description(df, i))

    w = input("which option you choose? : ")
    w = int(w)
    id = l[w-1][1]
    keywords.extend(df['extracted_tokens'][id])
    return keywords


def cleaning_data(df):
    remove_html_tag(df)
    remove_punctuation(df)
    lower_case_data(df)
    remove_noisy_data(df)
    replace_null_data(df)

def preprocessing_and_get_keywords(university_name,program_name,resume):
    df = pd.read_csv('./data/dataset.csv')
    cleaning_data(df)
    tokenize_data(df)
    remove_stop_words(df)
    generate_wordcould(df)
    calculate_total_tution(df)
    tution_boxplot_diagram(df)
    (a, b) = get_input(university_name,program_name,resume)
    keywords = search_program(df, a, b)
    print(keywords)
    return keywords



# if __name__ == '__main__':
#     preprocessing_and_get_keywords()





# RangeIndex: 60425 entries, 0 to 60424
# Data columns (total 23 columns):
#  #   Column                       Non-Null Count  Dtype
# ---  ------                       --------------  -----
#  0   country_name                 60425 non-null  object
#  1   country_code                 60425 non-null  object
#  2   university_name              60425 non-null  object
#  3   university_rank              34901 non-null  float64
#  4   program_name                 60425 non-null  object
#  5   program_type                 60425 non-null  object
#  6   deadline                     29219 non-null  object
#  7   duration                     51656 non-null  object
#  8   language                     60404 non-null  object
#  9   tution_1_currency            53773 non-null  object
#  10  tution_1_money               53773 non-null  float64
#  11  tution_1_type                53773 non-null  object
#  12  tution_2_currency            48086 non-null  object
#  13  tution_2_money               48086 non-null  float64
#  14  tution_2_type                48086 non-null  object
#  15  tuition_price_specification  53776 non-null  object
#  16  start_date                   39093 non-null  object
#  17  ielts_score                  47357 non-null  float64
#  18  structure                    50523 non-null  object
#  19  academic_req                 59647 non-null  object
#  20  facts                        60403 non-null  object
#  21  city                         56075 non-null  object
#  22  program_url                  60425 non-null  object
# dtypes: float64(4), object(19)