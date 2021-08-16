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

* HTML
* CSS
* JS

#### Note on testing for this project

With more time and experience I would like to write Python unit tests for the code in Django apps for this project aiming for highest coverage as possible. I would also have liked to include Jasmine unit tests for the significantly complex Javascript functions in Stripe.js file.

In the interests of time and to focus my efforts on the areas that the project assessment criteria reward, I decided that unit testing was not a priority for this project submission but should certainly be added in future. Ideally, I would have followed a Test Driven Development (TDD) approach of writing failing tests befoe implementing respective functions: however time did not allow for this project. This is a process I will seek to follow in my future Django devlopement work. 

## User stories testing

## Manual testing

## Bugs discovered

#### Solved bugs

#### Unsolved bugs

* django admin change form pdf FileField widget displays a non signed aws s3 url so permission to get object is denied from change form view. This was not fixed as it was taking too much time to properly update the widget used in admin given the project deadline. This bug will only be experienced by superusers and is negligible because user can still view object on the change list page in admin which provides a signed s3 url via application's 'download_story' view.