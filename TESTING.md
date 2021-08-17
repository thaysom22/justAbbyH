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
* If there is an error from Stripe  with authorizing user's payment on the client the overlay is removed and the user is shown the specific error message from Stripe beneath payment input. 
* If there is an invalid input or server error when creating the inactive user and associated subscription in database or when deleting the previously created inactive user (if payment client has failed) then the subscribe page is reloaded with an appropriate error messages displayed.
* If required fields are left blank the standard browser tool tips are displayed and the subscribe form will not submit.

Subscribed user:

7. As a subscribed user, I want to be able to browse all stories by the author, so that I can decide which stories I want to read.

* As above (2).
* Subscribed user is shown download story link when they click on a specific story link

8. As a subscribed user, I want to be able to view information about a particular story, so that I can decide whether I want to read the story.

* Links to all stories are displayed on stories page and when subscribed user clicks on any story they are shown a page for that particular story with reading time, publish date, download story link and description of story.

9. As a subscribed user, I want to download a pdf of a full story, so that I can read the full story at my convenience.

* Each individual story details page has a download link to a pdf document hosted on AWS for the story. This can be downloaded by the user for later use. 
* The link expires after 5 mins so it cannot be shared but the user can click the download story link again to generate a fresh link if they wish to access the story again.

10. As a subscribed user, I want to be able to login to the site after subscribing, so that I can access existing and newly published stories.

* The navigation bar displayed on the homepage and all other pages except subscribe pages has a link to login page where subscribed user can input credentials. 
* Logged in users are shown 'download story' link on individual story pages 

Site owner:

11. As the site owner, I want to be able to add stories to the site, so that I can publish new stories when I write them and increase the amount of content available to subscribers.

* logged in staff status users are shown a link to add story in navigation bar
* add story page has a form where fields for story can be inputted and a submit button to save story to database so it will appear on stories list page.

12. As the site owner, I want to be able to edit and delete stories, so that I can make necessary updates and curate the content available.

* logged in staff status users are shown an edit icon on each individual story detail page linking to edit story page
* edit story page displays a form which is prefilled with current field values from database which the user can update
* form has a submit button to save story changes to database so they will take effect on stories list and details pages
* edit story page has a delete story link to endpoint on server that removes story from database (first triggers a broswer confirm dialoge box)

As any type of user:

13. As a user, I want to naviagate a site that is attractive, well structured and user friendly on all device sizes easily navigate the site and achieve my goals. 

* navigation is laid out clearly and consistently in an familiar way on all device sizes
* color scheme and fonts are consistent across site
* plenty of padding and margins create a comfortable and visually appealing user experience
* where appropriate: layout, spacing, sizing of text and elements on page adjusts for device size
* interactive elements exhibit unobtrusive, familiar and helpful effects

14. As a user, I want to receive feedback messages from the site to inform me if my action was unsuccessful or an error has occurred, so that I am reassured my interactions are have the desired effect and what to do next if not.

* server sends messages to be displayed at top of page whenever an error occurs or a user needs feedback or information about a previous action.
* messages are displayed prominently but unobtrusively at top of page
* messages can be hidden by clicking a dismiss icon or they time out.

## Manual testing

## Bugs discovered

#### Solved bugs

* form input elements too wide on large devices. fix: set max-width value on containers for all forms on site.
* ambiguous error message for 'activate_user' endpoint. changed to inform that link could be already used, expired or invalid.
* inactive user not being deleted during payment process when payment fails on client so the subscribe page just reloads and the inactive user is not reoved from the database and specific error message is not shown to user. fix: endpoint name corrected in ajax call from subscribe.js function.
* Country field and card element placeholder color different to other input elements on non Chrome browsers. Fix: added css to set all same color.

#### Unsolved bugs

* django admin change form pdf FileField widget displays a non signed aws s3 url so permission to get object is denied from change form view. This was not fixed as it was taking too much time to properly update the widget used in admin given the project deadline. This bug will only be experienced by superusers and is negligible because user can still view object on the change list page in admin which provides a signed s3 url via application's 'download_story' view.