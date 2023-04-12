import config
import time
import preprocess.main as preprocess
import crawler.main as crawler


#sample whole project input
# Standford University
# Computer Science
# Bachelor of Computer Engineering, Ferdowsi University of Mashhad, GPA of 4, TA of Data Mining Course, 3 years of work experience


university_name = input("Enter Name of desired university : ")
program_name = input('Enter major : ')
resume = input('Enter your resume : ')
keywords = preprocess.preprocessing_and_get_keywords(university_name,program_name,resume)

#sample processed input for crawler test only
# university_name = 'Standford University'
# program_name = 'Computer Science'
# keywords= ['Bachelor of Computer Engineering', ' Ferdowsi University of Mashhad', ' GPA of 4', ' TA of Data Mining Course', ' 3 years of work experience', 'united', 'states', 'stanford', 'university', '3.0', 'joint', 'computer', 'science', 'msmba', 'degree', 'msc', 'english', 'logic', 'automata', 'complexity', 'probability', 'algorithmic', 'analysis', 'computer', 'organization', 'systems', 'cs', '107', '35', 'units', 'principles', 'computer', 'systems', 'cs', '140', 'operating', 'systems', 'systems', 'programming', 'cs', '143', 'compilers', 'cs', '144', 'introduction', 'computer', 'networking', 'cs', '145', 'introduction', 'databases', 'cs', '148', 'introduction', 'computer', 'graphics', 'imaging', 'cs', '210b', 'software', 'project', 'experience', 'corporate', 'partners', 'cs', '221', 'artificial', 'intelligence', 'principles', 'techniques', 'cs', '243', 'program', 'analysis', 'optimizations', 'cs', '248', 'interactive', 'computer', 'graphics']

crawler.sign_in(url=config.SIGN_IN_URL,
        email=config.EMAIL,
        password=config.PASSWORD)

crawler.redirect_to_templates(config.TEMPLATE_URL)

crawler.select_essay()

crawler.fill_details(title=university_name,
                                    description=program_name,
                                    keywords=keywords)

crawler.fill_outline()

crawler.fill_points()

crawler.fill_editor()