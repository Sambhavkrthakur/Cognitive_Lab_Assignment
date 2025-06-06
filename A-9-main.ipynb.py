{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "510b3ede",
   "metadata": {},
   "source": [
    "# NLP using Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8e9252e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\miyas\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\miyas\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package wordnet to\n",
      "[nltk_data]     C:\\Users\\miyas\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package wordnet is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import string\n",
    "import re\n",
    "import nltk\n",
    "nltk.download('punkt')\n",
    "from nltk.tokenize import word_tokenize\n",
    "import nltk\n",
    "nltk.download('stopwords')\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer,LancasterStemmer,WordNetLemmatizer\n",
    "from nltk.tokenize import sent_tokenize\n",
    "from nltk import pos_tag\n",
    "nltk.download('wordnet')\n",
    "from nltk.corpus import wordnet"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2470c29",
   "metadata": {},
   "source": [
    "\n",
    "## Text Preprocessing and Analysis\n",
    "1. Write a unique paragraph (5-6 sentences) about your favorite topic (e.g., sports, technology, food, books, etc.).  \n",
    "2. Convert text to lowercase and remove punctuation.  \n",
    "3. Tokenize the text into words and sentences.  \n",
    "4. Remove stopwords (using NLTK's stopwords list).  \n",
    "5. Display word frequency distribution (excluding stopwords).  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e11a445",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nCristiano Ronaldo, often referred to as CR7, is one of the greatest football players of all time. \\nBorn in Madeira, Portugal, he began his professional career with Sporting CP. \\nHe gained global recognition during his time at Manchester United, where he won his first Ballon d'Or. \\nRonaldo later moved to Real Madrid, becoming the club's all-time top scorer. \\nKnown for his incredible work ethic and athleticism, he has won numerous titles, including multiple Champions League trophies. \\nBeyond football, Ronaldo is also a philanthropist and a global icon in sports and fashion. \\n\""
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "paragraph='''\n",
    "Cristiano Ronaldo, often referred to as CR7, is one of the greatest football players of all time. \n",
    "Born in Madeira, Portugal, he began his professional career with Sporting CP. \n",
    "He gained global recognition during his time at Manchester United, where he won his first Ballon d'Or. \n",
    "Ronaldo later moved to Real Madrid, becoming the club's all-time top scorer. \n",
    "Known for his incredible work ethic and athleticism, he has won numerous titles, including multiple Champions League trophies. \n",
    "Beyond football, Ronaldo is also a philanthropist and a global icon in sports and fashion. \n",
    "'''\n",
    "paragraph"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a14c46cb",
   "metadata": {},
   "source": [
    "# coverting into lowercase andd removeing punctuation\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d0ef7e93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\ncristiano ronaldo often referred to as cr7 is one of the greatest football players of all time \\nborn in madeira portugal he began his professional career with sporting cp \\nhe gained global recognition during his time at manchester united where he won his first ballon dor \\nronaldo later moved to real madrid becoming the clubs alltime top scorer \\nknown for his incredible work ethic and athleticism he has won numerous titles including multiple champions league trophies \\nbeyond football ronaldo is also a philanthropist and a global icon in sports and fashion \\n'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "paragraph=paragraph.lower()\n",
    "paragraph=paragraph.translate(str.maketrans('', '', string.punctuation))\n",
    "paragraph"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6834af5c",
   "metadata": {},
   "source": [
    "# tokenize into words and sentences\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c4c2695e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(91, 1)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "words=word_tokenize(paragraph)\n",
    "sentences=sent_tokenize(paragraph)\n",
    "len(words), len(sentences)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fedd060",
   "metadata": {},
   "source": [
    "# removing stopwords\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a27d4691",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "58"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stop_words=set(stopwords.words('english'))\n",
    "filtered_words=[word for word in words if word not in stop_words]\n",
    "len(filtered_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "707b5e6b",
   "metadata": {},
   "source": [
    "# word frequency\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ce303303",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "word",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "count",
         "rawType": "int64",
         "type": "integer"
        }
       ],
       "conversionMethod": "pd.DataFrame",
       "ref": "c58c5c6a-b529-4a78-bad6-5d123ecf83b7",
       "rows": [
        [
         "0",
         "ronaldo",
         "3"
        ],
        [
         "2",
         "global",
         "2"
        ],
        [
         "3",
         "football",
         "2"
        ],
        [
         "1",
         "time",
         "2"
        ],
        [
         "40",
         "cristiano",
         "1"
        ],
        [
         "30",
         "athleticism",
         "1"
        ],
        [
         "31",
         "ballon",
         "1"
        ],
        [
         "32",
         "becoming",
         "1"
        ],
        [
         "33",
         "began",
         "1"
        ],
        [
         "34",
         "beyond",
         "1"
        ]
       ],
       "shape": {
        "columns": 2,
        "rows": 10
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>word</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ronaldo</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>global</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>football</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>time</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>cristiano</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>athleticism</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>ballon</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>becoming</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>began</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>beyond</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           word  count\n",
       "0       ronaldo      3\n",
       "2        global      2\n",
       "3      football      2\n",
       "1          time      2\n",
       "40    cristiano      1\n",
       "30  athleticism      1\n",
       "31       ballon      1\n",
       "32     becoming      1\n",
       "33        began      1\n",
       "34       beyond      1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.DataFrame(filtered_words, columns=['word'])\n",
    "df.value_counts().reset_index(name='count').rename(columns={'index':'word'}).sort_values(by='count', ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e0aac6a",
   "metadata": {},
   "source": [
    "# Q2: Stemming and Lemma za on \n",
    "1. Take the tokenized words from Ques on 1 (after stopword removal). \n",
    "2. Apply stemming using NLTK's PorterStemmer and LancasterStemmer. \n",
    "3. Apply lemma za on using NLTK's WordNetLemma zer. \n",
    "4. Compare and display results of both techniques."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "28637cc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "filtered_words=list(set(filtered_words))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7a6fd49",
   "metadata": {},
   "source": [
    "# stemming\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "37fb3aae",
   "metadata": {},
   "outputs": [],
   "source": [
    "stemmer=PorterStemmer()\n",
    "stemmed_words=[stemmer.stem(word) for word in filtered_words]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "82118bc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "lancaster_stemmer=LancasterStemmer()\n",
    "lancaster_words=[lancaster_stemmer.stem(word) for word in filtered_words]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "52ab08a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "wordnet_lemmatizer=WordNetLemmatizer()\n",
    "wordnet_words=[wordnet_lemmatizer.lemmatize(word) for word in filtered_words]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a29ab32b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "original",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "stemmed",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "lancaster",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "lemmatized",
         "rawType": "object",
         "type": "string"
        }
       ],
       "conversionMethod": "pd.DataFrame",
       "ref": "de911c6b-f8fb-4648-9c78-4c35f8e3ec4c",
       "rows": [
        [
         "0",
         "moved",
         "move",
         "mov",
         "moved"
        ],
        [
         "1",
         "recognition",
         "recognit",
         "recognit",
         "recognition"
        ],
        [
         "2",
         "portugal",
         "portug",
         "portug",
         "portugal"
        ],
        [
         "3",
         "work",
         "work",
         "work",
         "work"
        ],
        [
         "4",
         "real",
         "real",
         "real",
         "real"
        ],
        [
         "5",
         "fashion",
         "fashion",
         "fash",
         "fashion"
        ],
        [
         "6",
         "champions",
         "champion",
         "champ",
         "champion"
        ],
        [
         "7",
         "becoming",
         "becom",
         "becom",
         "becoming"
        ],
        [
         "8",
         "including",
         "includ",
         "includ",
         "including"
        ],
        [
         "9",
         "philanthropist",
         "philanthropist",
         "philanthrop",
         "philanthropist"
        ],
        [
         "10",
         "cr7",
         "cr7",
         "cr7",
         "cr7"
        ],
        [
         "11",
         "players",
         "player",
         "play",
         "player"
        ],
        [
         "12",
         "began",
         "began",
         "beg",
         "began"
        ],
        [
         "13",
         "sporting",
         "sport",
         "sport",
         "sporting"
        ],
        [
         "14",
         "gained",
         "gain",
         "gain",
         "gained"
        ],
        [
         "15",
         "united",
         "unit",
         "unit",
         "united"
        ],
        [
         "16",
         "also",
         "also",
         "also",
         "also"
        ],
        [
         "17",
         "career",
         "career",
         "car",
         "career"
        ],
        [
         "18",
         "clubs",
         "club",
         "club",
         "club"
        ],
        [
         "19",
         "madeira",
         "madeira",
         "madeir",
         "madeira"
        ],
        [
         "20",
         "ronaldo",
         "ronaldo",
         "ronaldo",
         "ronaldo"
        ],
        [
         "21",
         "ethic",
         "ethic",
         "eth",
         "ethic"
        ],
        [
         "22",
         "born",
         "born",
         "born",
         "born"
        ],
        [
         "23",
         "professional",
         "profession",
         "profess",
         "professional"
        ],
        [
         "24",
         "top",
         "top",
         "top",
         "top"
        ],
        [
         "25",
         "titles",
         "titl",
         "titl",
         "title"
        ],
        [
         "26",
         "beyond",
         "beyond",
         "beyond",
         "beyond"
        ],
        [
         "27",
         "cristiano",
         "cristiano",
         "cristiano",
         "cristiano"
        ],
        [
         "28",
         "football",
         "footbal",
         "footbal",
         "football"
        ],
        [
         "29",
         "later",
         "later",
         "lat",
         "later"
        ],
        [
         "30",
         "numerous",
         "numer",
         "num",
         "numerous"
        ],
        [
         "31",
         "alltime",
         "alltim",
         "alltim",
         "alltime"
        ],
        [
         "32",
         "first",
         "first",
         "first",
         "first"
        ],
        [
         "33",
         "athleticism",
         "athletic",
         "athlet",
         "athleticism"
        ],
        [
         "34",
         "referred",
         "refer",
         "refer",
         "referred"
        ],
        [
         "35",
         "trophies",
         "trophi",
         "troph",
         "trophy"
        ],
        [
         "36",
         "incredible",
         "incred",
         "incred",
         "incredible"
        ],
        [
         "37",
         "one",
         "one",
         "on",
         "one"
        ],
        [
         "38",
         "ballon",
         "ballon",
         "ballon",
         "ballon"
        ],
        [
         "39",
         "cp",
         "cp",
         "cp",
         "cp"
        ],
        [
         "40",
         "known",
         "known",
         "known",
         "known"
        ],
        [
         "41",
         "time",
         "time",
         "tim",
         "time"
        ],
        [
         "42",
         "multiple",
         "multipl",
         "multipl",
         "multiple"
        ],
        [
         "43",
         "madrid",
         "madrid",
         "madrid",
         "madrid"
        ],
        [
         "44",
         "icon",
         "icon",
         "icon",
         "icon"
        ],
        [
         "45",
         "global",
         "global",
         "glob",
         "global"
        ],
        [
         "46",
         "league",
         "leagu",
         "leagu",
         "league"
        ],
        [
         "47",
         "scorer",
         "scorer",
         "scor",
         "scorer"
        ],
        [
         "48",
         "sports",
         "sport",
         "sport",
         "sport"
        ],
        [
         "49",
         "often",
         "often",
         "oft",
         "often"
        ]
       ],
       "shape": {
        "columns": 4,
        "rows": 53
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>original</th>\n",
       "      <th>stemmed</th>\n",
       "      <th>lancaster</th>\n",
       "      <th>lemmatized</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>moved</td>\n",
       "      <td>move</td>\n",
       "      <td>mov</td>\n",
       "      <td>moved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>recognition</td>\n",
       "      <td>recognit</td>\n",
       "      <td>recognit</td>\n",
       "      <td>recognition</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>portugal</td>\n",
       "      <td>portug</td>\n",
       "      <td>portug</td>\n",
       "      <td>portugal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>work</td>\n",
       "      <td>work</td>\n",
       "      <td>work</td>\n",
       "      <td>work</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>real</td>\n",
       "      <td>real</td>\n",
       "      <td>real</td>\n",
       "      <td>real</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>fashion</td>\n",
       "      <td>fashion</td>\n",
       "      <td>fash</td>\n",
       "      <td>fashion</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>champions</td>\n",
       "      <td>champion</td>\n",
       "      <td>champ</td>\n",
       "      <td>champion</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>becoming</td>\n",
       "      <td>becom</td>\n",
       "      <td>becom</td>\n",
       "      <td>becoming</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>including</td>\n",
       "      <td>includ</td>\n",
       "      <td>includ</td>\n",
       "      <td>including</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>philanthropist</td>\n",
       "      <td>philanthropist</td>\n",
       "      <td>philanthrop</td>\n",
       "      <td>philanthropist</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>cr7</td>\n",
       "      <td>cr7</td>\n",
       "      <td>cr7</td>\n",
       "      <td>cr7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>players</td>\n",
       "      <td>player</td>\n",
       "      <td>play</td>\n",
       "      <td>player</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>began</td>\n",
       "      <td>began</td>\n",
       "      <td>beg</td>\n",
       "      <td>began</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>sporting</td>\n",
       "      <td>sport</td>\n",
       "      <td>sport</td>\n",
       "      <td>sporting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>gained</td>\n",
       "      <td>gain</td>\n",
       "      <td>gain</td>\n",
       "      <td>gained</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>united</td>\n",
       "      <td>unit</td>\n",
       "      <td>unit</td>\n",
       "      <td>united</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>also</td>\n",
       "      <td>also</td>\n",
       "      <td>also</td>\n",
       "      <td>also</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>career</td>\n",
       "      <td>career</td>\n",
       "      <td>car</td>\n",
       "      <td>career</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>clubs</td>\n",
       "      <td>club</td>\n",
       "      <td>club</td>\n",
       "      <td>club</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>madeira</td>\n",
       "      <td>madeira</td>\n",
       "      <td>madeir</td>\n",
       "      <td>madeira</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>ronaldo</td>\n",
       "      <td>ronaldo</td>\n",
       "      <td>ronaldo</td>\n",
       "      <td>ronaldo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>ethic</td>\n",
       "      <td>ethic</td>\n",
       "      <td>eth</td>\n",
       "      <td>ethic</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>born</td>\n",
       "      <td>born</td>\n",
       "      <td>born</td>\n",
       "      <td>born</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>professional</td>\n",
       "      <td>profession</td>\n",
       "      <td>profess</td>\n",
       "      <td>professional</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>top</td>\n",
       "      <td>top</td>\n",
       "      <td>top</td>\n",
       "      <td>top</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>titles</td>\n",
       "      <td>titl</td>\n",
       "      <td>titl</td>\n",
       "      <td>title</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>beyond</td>\n",
       "      <td>beyond</td>\n",
       "      <td>beyond</td>\n",
       "      <td>beyond</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>cristiano</td>\n",
       "      <td>cristiano</td>\n",
       "      <td>cristiano</td>\n",
       "      <td>cristiano</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>football</td>\n",
       "      <td>footbal</td>\n",
       "      <td>footbal</td>\n",
       "      <td>football</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>later</td>\n",
       "      <td>later</td>\n",
       "      <td>lat</td>\n",
       "      <td>later</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>numerous</td>\n",
       "      <td>numer</td>\n",
       "      <td>num</td>\n",
       "      <td>numerous</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>alltime</td>\n",
       "      <td>alltim</td>\n",
       "      <td>alltim</td>\n",
       "      <td>alltime</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>first</td>\n",
       "      <td>first</td>\n",
       "      <td>first</td>\n",
       "      <td>first</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>athleticism</td>\n",
       "      <td>athletic</td>\n",
       "      <td>athlet</td>\n",
       "      <td>athleticism</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>referred</td>\n",
       "      <td>refer</td>\n",
       "      <td>refer</td>\n",
       "      <td>referred</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>trophies</td>\n",
       "      <td>trophi</td>\n",
       "      <td>troph</td>\n",
       "      <td>trophy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>incredible</td>\n",
       "      <td>incred</td>\n",
       "      <td>incred</td>\n",
       "      <td>incredible</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>one</td>\n",
       "      <td>one</td>\n",
       "      <td>on</td>\n",
       "      <td>one</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>ballon</td>\n",
       "      <td>ballon</td>\n",
       "      <td>ballon</td>\n",
       "      <td>ballon</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>cp</td>\n",
       "      <td>cp</td>\n",
       "      <td>cp</td>\n",
       "      <td>cp</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>known</td>\n",
       "      <td>known</td>\n",
       "      <td>known</td>\n",
       "      <td>known</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>time</td>\n",
       "      <td>time</td>\n",
       "      <td>tim</td>\n",
       "      <td>time</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>multiple</td>\n",
       "      <td>multipl</td>\n",
       "      <td>multipl</td>\n",
       "      <td>multiple</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>madrid</td>\n",
       "      <td>madrid</td>\n",
       "      <td>madrid</td>\n",
       "      <td>madrid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>icon</td>\n",
       "      <td>icon</td>\n",
       "      <td>icon</td>\n",
       "      <td>icon</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>global</td>\n",
       "      <td>global</td>\n",
       "      <td>glob</td>\n",
       "      <td>global</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>league</td>\n",
       "      <td>leagu</td>\n",
       "      <td>leagu</td>\n",
       "      <td>league</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>scorer</td>\n",
       "      <td>scorer</td>\n",
       "      <td>scor</td>\n",
       "      <td>scorer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>sports</td>\n",
       "      <td>sport</td>\n",
       "      <td>sport</td>\n",
       "      <td>sport</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>often</td>\n",
       "      <td>often</td>\n",
       "      <td>oft</td>\n",
       "      <td>often</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>greatest</td>\n",
       "      <td>greatest</td>\n",
       "      <td>greatest</td>\n",
       "      <td>greatest</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>manchester</td>\n",
       "      <td>manchest</td>\n",
       "      <td>manchest</td>\n",
       "      <td>manchester</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>dor</td>\n",
       "      <td>dor</td>\n",
       "      <td>dor</td>\n",
       "      <td>dor</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          original         stemmed    lancaster      lemmatized\n",
       "0            moved            move          mov           moved\n",
       "1      recognition        recognit     recognit     recognition\n",
       "2         portugal          portug       portug        portugal\n",
       "3             work            work         work            work\n",
       "4             real            real         real            real\n",
       "5          fashion         fashion         fash         fashion\n",
       "6        champions        champion        champ        champion\n",
       "7         becoming           becom        becom        becoming\n",
       "8        including          includ       includ       including\n",
       "9   philanthropist  philanthropist  philanthrop  philanthropist\n",
       "10             cr7             cr7          cr7             cr7\n",
       "11         players          player         play          player\n",
       "12           began           began          beg           began\n",
       "13        sporting           sport        sport        sporting\n",
       "14          gained            gain         gain          gained\n",
       "15          united            unit         unit          united\n",
       "16            also            also         also            also\n",
       "17          career          career          car          career\n",
       "18           clubs            club         club            club\n",
       "19         madeira         madeira       madeir         madeira\n",
       "20         ronaldo         ronaldo      ronaldo         ronaldo\n",
       "21           ethic           ethic          eth           ethic\n",
       "22            born            born         born            born\n",
       "23    professional      profession      profess    professional\n",
       "24             top             top          top             top\n",
       "25          titles            titl         titl           title\n",
       "26          beyond          beyond       beyond          beyond\n",
       "27       cristiano       cristiano    cristiano       cristiano\n",
       "28        football         footbal      footbal        football\n",
       "29           later           later          lat           later\n",
       "30        numerous           numer          num        numerous\n",
       "31         alltime          alltim       alltim         alltime\n",
       "32           first           first        first           first\n",
       "33     athleticism        athletic       athlet     athleticism\n",
       "34        referred           refer        refer        referred\n",
       "35        trophies          trophi        troph          trophy\n",
       "36      incredible          incred       incred      incredible\n",
       "37             one             one           on             one\n",
       "38          ballon          ballon       ballon          ballon\n",
       "39              cp              cp           cp              cp\n",
       "40           known           known        known           known\n",
       "41            time            time          tim            time\n",
       "42        multiple         multipl      multipl        multiple\n",
       "43          madrid          madrid       madrid          madrid\n",
       "44            icon            icon         icon            icon\n",
       "45          global          global         glob          global\n",
       "46          league           leagu        leagu          league\n",
       "47          scorer          scorer         scor          scorer\n",
       "48          sports           sport        sport           sport\n",
       "49           often           often          oft           often\n",
       "50        greatest        greatest     greatest        greatest\n",
       "51      manchester        manchest     manchest      manchester\n",
       "52             dor             dor          dor             dor"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.DataFrame({'original':filtered_words, 'stemmed':stemmed_words, 'lancaster':lancaster_words, 'lemmatized':wordnet_words})\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc371b0f",
   "metadata": {},
   "source": [
    "# Q3. Regular Expressions and Text Splitting\n",
    "1. Take the original text from Question 1.  \n",
    "2. Use regular expressions to:  \n",
    "     a. Extract all words with more than 5 letters.  \n",
    "     b. Extract all numbers (if any exist in the text).  \n",
    "     c. Extract all capitalized words.  \n",
    "3. Use text splitting techniques to:  \n",
    "     a. Split the text into words containing only alphabets (removing digits and special characters).  \n",
    "     b. Extract words starting with a vowel.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "18d0bb71",
   "metadata": {},
   "outputs": [],
   "source": [
    "paragraph='''\n",
    "Cristiano Ronaldo, often referred to as CR7, is one of the greatest football players of all time. \n",
    "Born in Madeira, Portugal, he began his professional career with Sporting CP. \n",
    "He gained global recognition during his time at Manchester United, where he won his first Ballon d'Or. \n",
    "Ronaldo later moved to Real Madrid, becoming the club's all-time top scorer. \n",
    "Known for his incredible work ethic and athleticism, he has won numerous titles, including multiple Champions League trophies. \n",
    "Beyond football, Ronaldo is also a philanthropist and a global icon in sports and fashion. \n",
    "Visit https://www.cristianoronaldo.com for more details. \n",
    "He has scored over 800 career goals and has a net worth of $500 million.\n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "259f436d",
   "metadata": {},
   "source": [
    "# extracting all words whose lenth is greater than 5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a8580fbb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cristiano',\n",
       " 'Ronaldo',\n",
       " 'often',\n",
       " 'referred',\n",
       " 'greatest',\n",
       " 'football',\n",
       " 'players',\n",
       " 'Madeira',\n",
       " 'Portugal',\n",
       " 'began',\n",
       " 'professional',\n",
       " 'career',\n",
       " 'Sporting',\n",
       " 'gained',\n",
       " 'global',\n",
       " 'recognition',\n",
       " 'during',\n",
       " 'Manchester',\n",
       " 'United',\n",
       " 'where',\n",
       " 'first',\n",
       " 'Ballon',\n",
       " 'Ronaldo',\n",
       " 'later',\n",
       " 'moved',\n",
       " 'Madrid',\n",
       " 'becoming',\n",
       " 'scorer',\n",
       " 'Known',\n",
       " 'incredible',\n",
       " 'ethic',\n",
       " 'athleticism',\n",
       " 'numerous',\n",
       " 'titles',\n",
       " 'including',\n",
       " 'multiple',\n",
       " 'Champions',\n",
       " 'League',\n",
       " 'trophies',\n",
       " 'Beyond',\n",
       " 'football',\n",
       " 'Ronaldo',\n",
       " 'philanthropist',\n",
       " 'global',\n",
       " 'sports',\n",
       " 'fashion',\n",
       " 'Visit',\n",
       " 'https',\n",
       " 'cristianoronaldo',\n",
       " 'details',\n",
       " 'scored',\n",
       " 'career',\n",
       " 'goals',\n",
       " 'worth',\n",
       " 'million']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pattern=r'\\b[a-zA-Z]{5,}\\b'\n",
    "filtered_words=re.findall(pattern, paragraph)\n",
    "filtered_words"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61e24d2d",
   "metadata": {},
   "source": [
    "# extracting all numbers\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "754419b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['800', '500']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re_pattern=r'\\b\\d+\\b'\n",
    "filtered_numbers=re.findall(re_pattern, paragraph)\n",
    "filtered_numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5644f4a2",
   "metadata": {},
   "source": [
    "# extracting Capitalized Words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "78e96da9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cristiano',\n",
       " 'Ronaldo',\n",
       " 'Born',\n",
       " 'Madeira',\n",
       " 'Portugal',\n",
       " 'Sporting',\n",
       " 'He',\n",
       " 'Manchester',\n",
       " 'United',\n",
       " 'Ballon',\n",
       " 'Or',\n",
       " 'Ronaldo',\n",
       " 'Real',\n",
       " 'Madrid',\n",
       " 'Known',\n",
       " 'Champions',\n",
       " 'League',\n",
       " 'Beyond',\n",
       " 'Ronaldo',\n",
       " 'Visit',\n",
       " 'He']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "capitalized_words = re.findall(r'\\b[A-Z][a-z]*\\b', paragraph)\n",
    "capitalized_words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8e17a7b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cristiano',\n",
       " 'Ronaldo',\n",
       " 'often',\n",
       " 'referred',\n",
       " 'to',\n",
       " 'as',\n",
       " 'is',\n",
       " 'one',\n",
       " 'of',\n",
       " 'the',\n",
       " 'greatest',\n",
       " 'football',\n",
       " 'players',\n",
       " 'of',\n",
       " 'all',\n",
       " 'time',\n",
       " 'Born',\n",
       " 'in',\n",
       " 'Madeira',\n",
       " 'Portugal',\n",
       " 'he',\n",
       " 'began',\n",
       " 'his',\n",
       " 'professional',\n",
       " 'career',\n",
       " 'with',\n",
       " 'Sporting',\n",
       " 'CP',\n",
       " 'He',\n",
       " 'gained',\n",
       " 'global',\n",
       " 'recognition',\n",
       " 'during',\n",
       " 'his',\n",
       " 'time',\n",
       " 'at',\n",
       " 'Manchester',\n",
       " 'United',\n",
       " 'where',\n",
       " 'he',\n",
       " 'won',\n",
       " 'his',\n",
       " 'first',\n",
       " 'Ballon',\n",
       " 'd',\n",
       " 'Or',\n",
       " 'Ronaldo',\n",
       " 'later',\n",
       " 'moved',\n",
       " 'to',\n",
       " 'Real',\n",
       " 'Madrid',\n",
       " 'becoming',\n",
       " 'the',\n",
       " 'club',\n",
       " 's',\n",
       " 'all',\n",
       " 'time',\n",
       " 'top',\n",
       " 'scorer',\n",
       " 'Known',\n",
       " 'for',\n",
       " 'his',\n",
       " 'incredible',\n",
       " 'work',\n",
       " 'ethic',\n",
       " 'and',\n",
       " 'athleticism',\n",
       " 'he',\n",
       " 'has',\n",
       " 'won',\n",
       " 'numerous',\n",
       " 'titles',\n",
       " 'including',\n",
       " 'multiple',\n",
       " 'Champions',\n",
       " 'League',\n",
       " 'trophies',\n",
       " 'Beyond',\n",
       " 'football',\n",
       " 'Ronaldo',\n",
       " 'is',\n",
       " 'also',\n",
       " 'a',\n",
       " 'philanthropist',\n",
       " 'and',\n",
       " 'a',\n",
       " 'global',\n",
       " 'icon',\n",
       " 'in',\n",
       " 'sports',\n",
       " 'and',\n",
       " 'fashion',\n",
       " 'Visit',\n",
       " 'https',\n",
       " 'www',\n",
       " 'cristianoronaldo',\n",
       " 'com',\n",
       " 'for',\n",
       " 'more',\n",
       " 'details',\n",
       " 'He',\n",
       " 'has',\n",
       " 'scored',\n",
       " 'over',\n",
       " 'career',\n",
       " 'goals',\n",
       " 'and',\n",
       " 'has',\n",
       " 'a',\n",
       " 'net',\n",
       " 'worth',\n",
       " 'of',\n",
       " 'million']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "alphabetic_words = re.findall(r'\\b[a-zA-Z]+\\b', paragraph)\n",
    "alphabetic_words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "95f13cbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['often',\n",
       " 'as',\n",
       " 'is',\n",
       " 'one',\n",
       " 'of',\n",
       " 'of',\n",
       " 'all',\n",
       " 'in',\n",
       " 'at',\n",
       " 'United',\n",
       " 'Or',\n",
       " 'all',\n",
       " 'incredible',\n",
       " 'ethic',\n",
       " 'and',\n",
       " 'athleticism',\n",
       " 'including',\n",
       " 'is',\n",
       " 'also',\n",
       " 'a',\n",
       " 'and',\n",
       " 'a',\n",
       " 'icon',\n",
       " 'in',\n",
       " 'and',\n",
       " 'over',\n",
       " 'and',\n",
       " 'a',\n",
       " 'of']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vowels_start= re.findall(r'\\b[aeiouAEIOU]\\w*', paragraph)\n",
    "vowels_start"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d45e862b",
   "metadata": {},
   "source": [
    "# Q4. Custom Tokenization & Regex-based Text Cleaning  \n",
    "1. Take the original text from Question 1.  \n",
    "2. Write a custom tokenization function that:  \n",
    "    a. Removes punctuation and special symbols, but keeps contractions (e.g., \"isn't\" should not be split into \"is\" and \"n't\").  \n",
    "    b. Handles hyphenated words as a single token (e.g., \"state-of-the-art\" remains a single token).  \n",
    "    c. Tokenizes numbers separately but keeps decimal numbers intact (e.g., \"3.14\" should remain as is).  \n",
    "3. Use Regex Substitutions (`re.sub`) to:  \n",
    "    a. Replace email addresses with `<EMAIL>` placeholder.  \n",
    "    b. Replace URLs with `<URL>` placeholder.  \n",
    "    c. Replace phone numbers (formats: `123-456-7890` or `+91 9876543210`) with `<PHONE>` placeholder.  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f7d04bca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def custom_tokenizer(text):\n",
    "    pattern = r\"\\b\\w+(?:-\\w+)*\\b|\\b\\d+\\.\\d+\\b|\\b\\d+\\b\"\n",
    "    tokens = re.findall(pattern, text)\n",
    "    return tokens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "87757b4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cristiano',\n",
       " 'Ronaldo',\n",
       " 'often',\n",
       " 'referred',\n",
       " 'to',\n",
       " 'as',\n",
       " 'CR7',\n",
       " 'is',\n",
       " 'one',\n",
       " 'of',\n",
       " 'the',\n",
       " 'greatest',\n",
       " 'football',\n",
       " 'players',\n",
       " 'of',\n",
       " 'all',\n",
       " 'time',\n",
       " 'Born',\n",
       " 'in',\n",
       " 'Madeira',\n",
       " 'Portugal',\n",
       " 'he',\n",
       " 'began',\n",
       " 'his',\n",
       " 'professional',\n",
       " 'career',\n",
       " 'with',\n",
       " 'Sporting',\n",
       " 'CP',\n",
       " 'He',\n",
       " 'gained',\n",
       " 'global',\n",
       " 'recognition',\n",
       " 'during',\n",
       " 'his',\n",
       " 'time',\n",
       " 'at',\n",
       " 'Manchester',\n",
       " 'United',\n",
       " 'where',\n",
       " 'he',\n",
       " 'won',\n",
       " 'his',\n",
       " 'first',\n",
       " 'Ballon',\n",
       " 'd',\n",
       " 'Or',\n",
       " 'Ronaldo',\n",
       " 'later',\n",
       " 'moved',\n",
       " 'to',\n",
       " 'Real',\n",
       " 'Madrid',\n",
       " 'becoming',\n",
       " 'the',\n",
       " 'club',\n",
       " 's',\n",
       " 'all-time',\n",
       " 'top',\n",
       " 'scorer',\n",
       " 'Known',\n",
       " 'for',\n",
       " 'his',\n",
       " 'incredible',\n",
       " 'work',\n",
       " 'ethic',\n",
       " 'and',\n",
       " 'athleticism',\n",
       " 'he',\n",
       " 'has',\n",
       " 'won',\n",
       " 'numerous',\n",
       " 'titles',\n",
       " 'including',\n",
       " 'multiple',\n",
       " 'Champions',\n",
       " 'League',\n",
       " 'trophies',\n",
       " 'Beyond',\n",
       " 'football',\n",
       " 'Ronaldo',\n",
       " 'is',\n",
       " 'also',\n",
       " 'a',\n",
       " 'philanthropist',\n",
       " 'and',\n",
       " 'a',\n",
       " 'global',\n",
       " 'icon',\n",
       " 'in',\n",
       " 'sports',\n",
       " 'and',\n",
       " 'fashion',\n",
       " 'Visit',\n",
       " 'https',\n",
       " 'www',\n",
       " 'cristianoronaldo',\n",
       " 'com',\n",
       " 'for',\n",
       " 'more',\n",
       " 'details',\n",
       " 'He',\n",
       " 'has',\n",
       " 'scored',\n",
       " 'over',\n",
       " '800',\n",
       " 'career',\n",
       " 'goals',\n",
       " 'and',\n",
       " 'has',\n",
       " 'a',\n",
       " 'net',\n",
       " 'worth',\n",
       " 'of',\n",
       " '500',\n",
       " 'million']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custom_tokens = custom_tokenizer(paragraph)\n",
    "custom_tokens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5fb46321",
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_text(text):\n",
    "    text = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,3}', '<EMAIL>', text)\n",
    "    text = re.sub(r'https?://\\S+', '<URL>', text)\n",
    "    text = re.sub(r'(?:\\+?\\d{1,3}[-.\\s]?)?(?:\\(?\\d{3}\\)?[-.\\s]?)?\\d{3}[-.\\s]?\\d{4}', '<PHONE>', text)\n",
    "    return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18e4d8ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nCristiano Ronaldo, often referred to as CR7, is one of the greatest football players of all time. \\nBorn in Madeira, Portugal, he began his professional career with Sporting CP. \\nHe gained global recognition during his time at Manchester United, where he won his first Ballon d'Or. \\nRonaldo later moved to Real Madrid, becoming the club's all-time top scorer. \\nKnown for his incredible work ethic and athleticism, he has won numerous titles, including multiple Champions League trophies. \\nBeyond football, Ronaldo is also a philanthropist and a global icon in sports and fashion. \\nVisit <URL> for more details. \\nHe has scored over 800 career goals and has a net worth of $500 million.\\n\""
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clean_text(paragraph)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}