# ScholarMate 

Your AI-powered graduate program application assistant.

Applying to competitive graduate programs is tedious. ScholarMate automates the entire process - from researching programs to generating tailored essays.

Just provide your background and ScholarMate will take care of the rest.


## Key Features

- Essay topic research and outlining 
- Contextual essay body generation
- Program search and recommendation
- Resume analysis and keyword extraction
- Text analysis and correction
- Automated application form filling

## Getting Started

### Installation

```
git clone https://github.com/mousavil/scholarmate
pip install -r requirements.txt
```

### Usage

```
python main.py
```

Follow the prompts to provide your background, desired programs, and other details. ScholarMate will take care of the rest!

Generated essays and applications can be found in the `output/` folder.

## How it Works

- User provides background, goals, programs of interest 
- Resume is parsed to extract key skills and experiences  
- Database is searched to recommend target schools and programs
- Essay outline is generated using NLP techniques
- Essay body is generated based on user context  
- Applications are automated using Selenium

## Sample Inputs:

```
University Name: Standford University
Program Name : Computer Science
Resume: Bachelor of Computer Engineering, Ferdowsi University of Mashhad, GPA 3.5 of 4, TA of Data Mining Course, 5 years of work experience
```

## Pre-processed sample input for feeding crawler:
```University Name = 'Standford University'
Program Name  = 'Computer Science'
Keywords = ['Bachelor of Computer Engineering', ' Ferdowsi University of Mashhad', ' GPA 3.5 of 4', ' TA of Data Mining Course', ' 3 years of work experience', 'united', 'states', 'stanford', 'university', '3.0', 'joint', 'computer', 'science', 'msmba', 'degree', 'msc', 'english', 'logic', 'automata', 'complexity', 'probability', 'algorithmic', 'analysis', 'computer', 'organization', 'systems', 'cs', '107', '35', 'units', 'principles', 'computer', 'systems', 'cs', '140', 'operating', 'systems', 'systems', 'programming', 'cs', '143', 'compilers', 'cs', '144', 'introduction', 'computer', 'networking', 'cs', '145', 'introduction', 'databases', 'cs', '148', 'introduction', 'computer', 'graphics', 'imaging', 'cs', '210b', 'software', 'project', 'experience', 'corporate', 'partners', 'cs', '221', 'artificial', 'intelligence', 'principles', 'techniques', 'cs', '243', 'program', 'analysis', 'optimizations', 'cs', '248', 'interactive', 'computer', 'graphics']
```

## Contributing

ScholarMate is built on open source - contributions welcome!

Some ideas for improvements:

- Support for more programs/countries
- Additional application types 
- Improved NLP analysis
- Essay revision suggestions
- User profile management

Let's make applying to graduate programs easy!
