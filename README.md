![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Words for breakfast

The historian Theodore Zeldin wrote in 2015 in *The hidden pleasures of life* that it’s impossible to know in advance what’s worth knowing, and that for one piece of knowledge to connect to another, an individual’s imagination is necessary. But how to find out what should be connected?
> Every morning I would like to include in my breakfast a taster of new book from any part of the world, in any subject, summarised in a thousand words, whose author has something to say that may be of universal interest, though it might escape the attention of most people because it is imprisoned in the category-cage of a speciality … those half a million books that appear each year are part of humanity’s struggle with ignorance, and they are part of the world I want to connect with.
(Theodore Zeldin. The hidden pleasures of life: a new way of remembering the past and imagining the future. London: MacLehose Press 2016, pp382-383)

Simply stated, this site attempts to provide that.

# Note
**This project has gone horribly and irretrievably wrong in pretty well everything it set out to do, and failed in probably every single point. In fact, in many aspects, it has gone backwards since I started it, and it’s certainly a backwards step from my previous projects.**


**Superusers**
* jplsu03; djn0th2119; maeve.maccoll@gmail.com
* jplsu05; suyn0th2119; james05@jamestest.com


# User experience (UX)

## User stories
### 1. As a first time visitor I would like to
* easily understand the main purpose of the site and be reassured that I have found a site which may have what I am looking for
* be able to browse contents easily and straightforwardly
* be able to read examples of the site content
* be able to buy one or more books easily and straightforwardly
* be able to register a new account easily and straightforwardly
* be able to easily navigate throughout the site to find content

### 2. As a returning visitor, I would like to
* login to my account
* read book summaries
* make book purchases

## Strategy (user needs and business objectives)
1. The website exists to bring to interested reader a wide knowledge of the latest developments in scholarship and other well-informed and considered writing across the full range of subjects and disciplines
* The site must present an up to date and wide range of summaries by book authors
* It must have a shop selling the books summarised and related books
* Users must be able to log in and access the summaries and make purchases
* Comments on summaries may be allowed so that users may engage in informed and respectful debate
All of this requires at least one site administrator to add summaries, administer the store, and oversee discussions, with appropriate permissions to be able to do all this.

2. The user stories envisage an audience of informed people who follow scholarship and intellectual debates, as well as people who might not join but who have an interest in a particular book or subject.
* The site’s distinctive feature is hosting summaries of books by the authors themselves.
  * Simple search function for authors, books, and subjects
  * Straightforward cross-referencing
  * Opportunities to buy books
  * Links between book summaries and the bookshop
* The site operates through a subscription scheme, which provides its main income.
  * Straightforward procedure to sign up, sign in, edit the account, and if necessary remove it
  * Limited access to summaries for non-subscribers
* The site will sell books as an additional source of income and to provide a service to subscribers
  * Opportunities to buy books
  * Links between book summaries and the bookshop
  * Straightforward process to administer the bookshop, including updating stock list, monitoring purchases, dealing with enquiries, etc

## Scope (functional specifications and context requirements)
1. At its most basic, the website hosts summaries of books written by the authors themselves, accessible by subscribers
* List of summaries / summaries search by author, title, subject, date, etc
* Links from summaries to bookshop and vice versa

2. Registration
* Sign up facility, including creating a password-protected account

3. Log in
* Once registered, users must  be able to easily login to their accounts to amend them and check purchases.

4. Log out
* If required logging out should be straightforward.

5. Search & retrieve
* The search function must be clear and intuitive, to find book summaries by author, title, date, subject, or keyword.
* The function should also retrieve if preferred books for purchase

6. Summaries
* Summaries should be clearly and pleasantly presented
* They should be available only to logged-in subscribers

7. Bookshop
* The site must allow users to edit existing entries, either their own of those submitted by others.

8. Some users will find it helpful or necessary to contact the site administrator 
* A contact email

9. Bookshop administration
* There must be administrative facility to update and check stock in the database and otherwise manage the bookshop

9. Aspects to save till later:
* Logged in users should be able to leave comments and generate a discussion about the summaries
* Non-subscribing users should be allowed to access articles on a limited or trial basis

## Structure (interaction and information design)
1. The site has a simple structure.

Users will arrive on the home page, with a simple image and overview of the site. From here they have choices to find out more about the site, look at the summaries, go to the bookshop, or log in or register.

2. Home
* Welcome text
* Search

3. About
* Expand on what the site does and what its ideas are
* Search

4. Authors’ summaries
* Search
* Options for exploring, eg, subject, what’s new, etc

5. Bookshop
* All available books
* Checkout procedure

6. Register
* Registration form

7. Login
* Login form

8. Profile (when logged in)
* Options to see account details, including personal information and items purchased

9. Logout
* Logs the user out and takes them back to the login page

## Skeleton (interface, navigation, and information design)
1. Wireframe mock-ups were developed on [Figma](https://www.figma.com/file/dhYyUyA69hWrAzR1oFXFk3/Words-for-breakfast?node-id=6%3A9)

2. Colour scheme and imagery
* Straightforward and sober – mainly black and white, with a small injection of colour (orange)

3. Main image
* The main image is taken from the [The Baillie Gifford Prize for Non-Fiction](https://thebailliegiffordprize.co.uk/) (since changed)

4. Fonts
* Two variable Google Fonts were chosen, which go well together, both fairly formal, Kreon and Open Sans. Sans Serif is the fallback font in case the font isn't imported into the site correctly.

## Surface (visual design)
1. A very simple logo was designed in PowerPoint, which hints at a coffee cup and a book. On larger screens there is a navigation bar, and on smaller screens a toggler icon leading to the navigation.

2. On all screen sizes the footer will contain just an email link and a copyright notice. The footer is differentiated from the body of the page through coloration.

3. The Home page, also the Glossary, is presented as relatively uncluttered, with simply a welcome message, a search bar, and the glossary itself.

4. The About page is basically text, with a straightforward books image. The site’s users won’t be too troubled by blocks of text.

5. The Register, Sign In, and Profile pages are similar and all simple, with site branding and orange colour.

6. When searching on the Summaries page for summaries (or arriving there after carrying out a search), book images are shown in the search results. The summaries themselves have an image at the top, either the book cover or an image from the book.

7. The Bookshop page unceremoniously displays available books and provides a shop checkout.

# Data
Because of the stability and regularity of the data, both of subscribers and of books, SQL is an appropriate data management approach, in this case using [PostgreSQL](https://www.postgresql.org/) with Django.

## Books model
The fields used in ‘books’ are
* title
* author_surname
* author_firstname
* publisher
* date
* isbn
* book_format
* pages
* sku
* category (ForeignKey)
* image_url
* image

The fields used in ‘categories’ are:
* friendly_name
* name

## Checkout model
The fields used in ‘order (which align with those in Stripe) are
* order_number
* user_profile (profile:ForeignKey)
* full_name
* email
* phone_number
* country
* postcode
* town_or_city
* street_address1
* street_address2
* county
* date
* order_total
* delivery_cost
* grand_total
* original_basket
* stripe_pid

## Profiles model
The fields used in ‘profiles’ are
* user
* default_phone_number
* default_street_address1
* default_street_address2
* default_town_or_city
* default_county
* default_postcode
* default_country
* subscriber_status

## Summaries model
The fields used in ‘summaries’ are
* summaries_title
* author_surname (books: ForeignKey)
* author_firstname (books: ForeignKey)
* title (books: ForeignKey)
* date (books: ForeignKey)
* category (ForeignKey)

The Books model can only be added to in the site administration. For profiles, users can create their own accounts (or accounts can be created in the administration).

## Subscribers / users collection
When registering an account, the user provides:
* full name
* email (used as the unique identifier)
* password (hashed)

# Features

## Existing features
N/A

## Features left to implement
All

## Issues and bugs
Too many to note

# Technologies used
## Languages
* HTML5
* CSS3
* JavaScript
* Python
* Django

## Frameworks, libraries & programs
* Gitpod
* [Git](https://git-scm.com/)
  * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/)
  * GitHub is used to store the projects code after being pushed from Git.
* Heroku
  * The site is deployed on Heroku
* AWS
  * Static files are delivered by AWS

* [Django](https://www.djangoproject.com/)

* [jQuery](https://jquery.com/)
  * jQuery was used to simplify the use of JavaScript

* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
  * Google Fonts was used to import into style.css the variable fonts used throughout (Kreon and Open Sans)

* [Figma](https://www.figma.com/)
  * Figma was used to create the wireframes during the design process.

# Testing
## Validators
N/A

## Testing user stories
### 1. As a first time visitor I would like to
* easily understand the main purpose of the site and be reassured that I have found a site which may have what I am looking for
* be able to register a new account easily and straightforwardly
* be able to easily navigate throughout the site to find content
* make searches and easily find definitions
* contribute a new term, with definition and other information
* edit or if necessary delete terms that I’ve created
* if need be, contact website administrator

#### Response
N/A

### 2. As a returning visitor, I would like to
* continue the activities of the first visit, including searching, contributing, and editing
* return to any earlier to contributions to edit them

### Response
N/A

## Further testing
N/A

## Known bugs
Entire site

# Deployment
## Deploy the application to Heroku
The project is deployed to Heroku.

1. Set up the files that Heroku needs to run the application. First, a requirements.txt file is passed to  Heroku so it knows which applications and dependencies the app requires
  1.  In the terminal window (I use Gitpod)
‘pip3 freeze --local > requirements.txt’

2. The Procfile tells Heroku which file runs the app, and how to run it
  1. In the terminal window
‘echo web: python app.py > Procfile’
Make sure to delete a blank that may be added to the end of the Procfile.

3. At [Heroku](https://www.heroku.com/), if you don’t already have an account, create a free account

4. Create a new app on https://dashboard.heroku.com/apps. The name must be unique. Click ‘Create App’.

5. To connect the app, set up Automatic Deployment from the GitHub repository. Your GitHub profile should be displayed
  * Add the repository name, and click to connect to this app.

6. The environment variables should be within a hidden env.py file. To allow Heroku to read them:
  1. Click 'Settings', and 'Reveal Config Vars'
  2. Take the required variables from the env.py file:
  * IP: 0.0.0.0
  * PORT: 5000
  *

7. From the terminal, add, commit, and push to the repository one by one
  1. Procfile
  2. requirements.txt

8. 'Enable Automatic Deploys', and click 'Deploy Branch'.

## Deliver static files on AWS
It is necessary to create an [AWS](https://aws.amazon.com) account and set up an AWS S3 bucket to store static files for deployment. 

## GitHub pages - creating a clone
1. On GitHub, navigate to the main page of the repository.
2. Above the list of files, click Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy symbol
4. On your computer, open Git Bash
5. Change the current working directory to the location where you want the cloned directory.
6. Type 'git clone’, and then paste the URL just copied.

# Credits
## Code
1. I have used much code and taken many ideas from the Full Stack Frameworks Development walkthrough project, Boutique Ado. 
2. Bootstrap was used for the main layout elements of the site – forms, cards, navbar, and buttons, and Bootstrap [documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/) followed
3. For the Navbar, Bootstrap was supplemented with code taken from [Granta magazine](https://granta.com/)
4. Some home page layout taken from [Baillie Gifford Prize](https://thebailliegiffordprize.co.uk/) (since changed)
5. The favicon was generated using [favicon.io](https://favicon.io/) with adjustments used by [Kes Cardoso](https://github.com/kescardoso/stripeme/blob/master/templates/base.html)
6. CSS was supplemented by [Bulma](https://bulma.io/).
7. I regularly consulted
* [StackOverflow](https://stackoverflow.com/), eg on horizontal scroll on books pages: (Horizontally scrollable list of cards in Bootstrap)[https://stackoverflow.com/questions/35993300/horizontally-scrollable-list-of-cards-in-bootstrap]
* [W3Schools](https://www.w3schools.com/)
* [Geeks for Geeks](https://www.geeksforgeeks.org)

## Content
* Book listings and images [London Review Bookshop](https://www.londonreviewbookshop.co.uk/booklists)

## Acknowledgements
a Many thanks to the tutor support team for hanging on in during some long and painful queries

James Lancaster 29 November 2021

Heroku deployment
https://breakfast-words.herokuapp.com/

GitHub
https://github.com/james-lancaster/breakfast-words