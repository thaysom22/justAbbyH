# justAbbyH Stories - TESTING

[README](./README.md)

[View website on Heroku](https://just-abby-h.herokuapp.com/)

## Table of Contents

1. [Automated testing](#automated-testing)
	* Validation services
	* Note on testing for this project
2. [User stories testing](#user-stories-testing)
3. [Manual testing](#manual-testing)
4. [Bugs discovered](#bugs-discovered)
	* Solved bugs
	* Unsolved bugs

## Automated testing

#### Validation Services

* [W3C Markup Validation]() for HTML.
* [W3C CSS Validation]() for CSS.
* [JSHint]() for JavaScript.

#### Note on testing for this project

With more time and experience I would like to write Python unit tests for the code in Django apps for this project aiming for highest coverage as possible. I would also have liked to include Jasmine unit tests for the significantly complex Javascript functions in Stripe.js file.

In the interests of time and to focus my efforts on the areas that the project assessment criteria reward, I decided that unit testing was not a priority for this project submission but should certainly be added in future. Ideally, I would have followed a Test Driven Development (TDD) approach of writing failing tests befoe implementing respective functions: however time did not allow for this project. This is a process I will seek to follow in my future Django devlopement work. 

## User stories testing

This section goes through all user stories from the [README](./README.md) file and confirms they are satisfied.

New user:

1. As a new user, I want to be able to find out information about the author, so that I can decide whether I want to subscribe.

* The about page is linked from the navigation menu and the footer from the homepage and every page except subscribe pages. 
* The about page displays a picture and short biography. 
* The navigation menu also displays social media links.

2. As a new user, I want to be able to see a selection of stories by the author, so that I can decide whether I want to subscribe.

* The stories page is linked from the navigation menu and the footer from the homepage and every page except subscribe pages. 
* The stories page is also linked from a main section of the homepage via a prominent button.
* The stories page displays all stories in database as image links with titles. The user can scroll through this list and click on any image to open up a details page for the selected story which displays reading time, publish date and a description.

3. As a new user, I want to be able to contact the author and to connect via social media, so that can decide whether I want to subscribe. 

* The footer is displayed on the homepage and all pages except subscribe pages and contains social media links. 
* The expanded navbar on mobile/tablet also dislays social media links.
* The about page displays social media and an email link.

4. As a new user, I want to be informed about benefits subscribing and how to subscribe, so that I can decide whether I want to, and I know how to subscribe.

* Subscribe links are displayed prominently to unsubscribed users in the navigation, footer and in a main section of the homepage. 
* When an unsubscribed user clicks on an individual story link they are shown a link to subscribe to get access. 
* The subscribe page dipslays information about payment amount and benefits clearly at top of page.

5. As a new user, I want to be able to make a simple, secure payment to initiate a subscription, so that I can access author's stories

* The subscribe page contains a single form with a prominent button to subscribe
* The user is then shown a subscription successful page with information instructing them to access email and follow an activation link to login.

6. As a new user, I want to be shown feedback on the status of my payment and subscription, so that I am resassured I have been provided with what I have paid for and I know what further action to take if necessary.

* The subscribe form button is disabled until valid payment information is entered. The user is shown realtime feedback before form submit if there are errors with payment information. When the payment information is valid, the user is shown the charge amount and the button is enabled. 
* When valid subscribe form is submitted, the user is shown an overlay with a repeating animation and is informed that their payment is being processed. If the process is successful the user is shown a subscription successful page and given instructions for how to activate their account via email link.
* If there is an error with authorizing user's payment the overlay is removed and the user is shown the specific error message from Stripe beneath payment input. 


Subscribed user:

7. As a subscribed user, I want to be able to browse all stories by the author, so that I can decide which stories I want to read.
8. As a subscribed user, I want to be able to view information about a particular story, so that I can decide whether I want to read the story.
10. As a subscribed user, I want to download a pdf of a full story, so that I can read the full story at my convenience.
11. As a subscribed user, I want to be able to login to the site after subscribing, so that I can access existing and newly published stories.

Site owner:

12. As the site owner, I want to be able to add stories to the site, so that I can publish new stories when I write them and increase the amount of content available to subscribers.
13. As the site owner, I want to be able to edit and delete stories, so that I can make necessary updates and curate the content available.

As any type of user:

14. As a user, I want to naviagate a site that is attractive, well structured and user friendly on all device sizes easily navigate the site and achieve my goals. 
15. As a user, I want to receive feedback messages from the site to inform me if my action was usccessful or an error has occurred, so that I am reassured my interactions are have the desired effect and what to do next if not.

## Manual testing

## Bugs discovered

#### Solved bugs

* form input elements too wide on large devices. fix: set max-width value on containers for all forms on site.
* ambiguous error message for 'activate_user' endpoint. changed to inform that link could be already used, expired or invalid.
* inactive user not being deleted during payment process when payment fails on client so the subscribe page just reloads and the inactive user is not reoved from the database and specific error message is not shown to user. fix: endpoint name corrected in ajax call from subscribe.js function.

#### Unsolved bugs

* django admin change form pdf FileField widget displays a non signed aws s3 url so permission to get object is denied from change form view. This was not fixed as it was taking too much time to properly update the widget used in admin given the project deadline. This bug will only be experienced by superusers and is negligible because user can still view object on the change list page in admin which provides a signed s3 url via application's 'download_story' view.