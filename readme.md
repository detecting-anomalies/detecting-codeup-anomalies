# Anomalous Findings in the Codeup Web Data


## Main Questions and their Answers
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

    - The most frequently visited lesson accessed consistently for each program are as follows:
        - Program 1 - javascript
        - Program 2 - also javascript
        - Program 3 - css
        - Program 4 - again, javascript

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    
    - One cohort, Jemison, fell into the date range for three major data spikes (Feb, April, and July of 2020).
    - There does not appear to be a spike in regards to Web Dev.

3. Are students who, when active, hardly access the curriculum? If so, what information do you have about these students?

    - There is one specific student we dug deeper into, whose user id is 62:
        - They started on 2020-09-21 and ended on 2021-03-30, about 3 months.
        - The accessed the pages in 2018, all within an hour of each other, well before they started at Codeup.
        - They were in the Jupiter cohort.
        - They were in the web dev program and only accessed Codeups page 4 times while a student; the homepage, java-ii, java-iii, and spring.
        - All of the ip’s traced back to San Antonio, TX.

4. Is there any suspicious activity, such as users/machines/ect accessing the curriculum who shouldn’t be? Does it appear that any web scraping is happening? Are there any suspicious ip addresses?

    - Here are some, while not explicitly suspicious, they are definitely odd this:
        - Every staff request over the course of this timeframe is by one single staff member, but they originate from 9 different ip addresses.
        - An overwhelming majority of the data is from users with no information, which we took to be non-students, and most of those were not 		 people simply looking at the homepage.
        - Around 10% of the people to visit the home paged ended up being students.
        - There were at least three individuals during this timeframe who scraped hundreds of pages in the curriculum.

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

    - Among programs 1, 2, and 4, javascript, spring, html, and classification were the most commonly looked at after graduation.
    - In program 3, there were no post graduation queries.

7. Which lessons are least accessed?

    - Four of the least accessed lessons were:
        - ‘creating a repository’
        - ‘the data science pipeline’
        - ‘python series’
        - ’stats simulation’
