# Fixit - Django Rest Framework Backend

Developed by Jeremy Simons

[Link to live API](https://fixit-drf-api-b3b58b2bc39c.herokuapp.com/)

## Introduction

This is the backend for the forum application Fixit: a community of DIY enthusiasts to support one another.

This documentation will detail the features available via the API, the design, endpoints, testing and instructions for forking the project with your own postgres database. 

## Contents

* [Project Goals](#project-goals)<br>
    * [For the user](#for-the-user)
    * [For the site owner](#for-the-site-owner)
* [User Experience](#user-experience)<br>
    * [Target audience](#target-audience)
    * [User requirements](#user-requirements)
    * [User Manual](#user-manual)
    * [User Stories](#user-stories)
* [Agile Workflow](#agile-workflow)
* [Technical Design](#technical-design)
    * [Data Models](#data-models)
    * [Endpoints](#endpoints)
    * [Database Schema](#database-schema)
* [Features](#features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
    * [Database](#database)
    * [Heroku deployment](#heroku-deployment)
    * [Forking GitHub Repository](#forking-github-repository)
    * [Cloning GitHub Repository](#cloning-github-repository)
* [Testing](#testing)
* [Validation](#validation)
* [Bugs](#bugs)
* [Credits](#credits)

## Project goals

### For new users
* to sign up to a community of DIY / fix-it-yourself enthusiasts.
* Interact with other users who are able to help me with my own DIY problems

### For existing users
* To interact with other users and get help with my own DIY problems, or help others with theirs.
* To gain recognition for the help I render to other users.

## User Experience

### User stories.

The following user stories reflect the actions a site admin might want to perform on the database.

#### Authentication
* As a new user I want to sign up and create a new account so I can use the site.
* As an existing user I want to log in as an existing user so that I can carry on following the threads that I saved.
* As an authenticated user I want to sign out of my account so that I can securely leave the site.

#### Navigation
* As an authenticated user I want to be directed to my homepage feed so that I can see what the latest posts are.
* As an authenticated user I want to easily navigate back to the home page feed so that I can return to the latest posts.
* As an authenticated user I want to easily navigate to a page showing the trending / most up-voted posts on the site.
* As an authenticated user I want to easily navigate to my profile so I can view it / edit it / see my own posts
* As an authenticated user I want to easily navigate to the signout option so I can leave the site without hassle.

#### Interaction
* As an authenticated user I want to create a new post on the site so that I can ask my specific question to the community.
* As an authenticated user I want to edit my post so that I can amend my query/photo.
* As an authenticated user I want to delete my post so that I can remove my content from the site.
* As an authenticated user I want to be able to upload images as part of my post so that I can illustrate my point.
* As an authenticated user I want to access a page of my posts so far so that I can keep track of the interactions I have had on the site.
* As an authenticated user I want to upvote helpful posts that other people have made.
* As an authenticated user I want to comment on other people’s posts to help them with their query.
* As an authenticated user I want to edit my comment so that I can amend/clarify what I said.
* As an authenticated user I want to delete my comment so I can remove what I no longer say on the site.
* As an authenticated user I want to upvote other people’s helpful comments.
* As an authenticated user I want to give a ‘star’ to users who make helpful contributions to the site.

#### Feed
* As an authenticated user I want to be able to see the most up-voted posts on the site so I can keep up with what is popular
* As an authenticated user I want to see the posts that I have voted for so that I can keep track of posts I like/found helpful.
* As an authenticated user I want to view the most ‘starred’ users so that I can see the contributions of helpful users.

#### Profiles
* As an authenticated user I want to edit my profile so that other users can find out more about me.
* As an authenticated user I want to be able to view other users’ profiles and posts so that I can comment on their posts.

## Agile workflow

An agile methodology was employed for this project. Epics were created and each user story was assigned to an epic. Development of the project was organised into iterations where certain features were implemented to their completion before reviewing the backlog and re-assigning tasks for the next iteration.

This was achieved and tracked using the github issues/projects/kanban board features.

### User stories

User stories and bug reports were uploaded to the project using Github issues templates. User stories were ranked with one of the following labels:

* Must have
* Should have
* Could have
* Wont have (decision made that the feature is not needed and improving other features is higher priority with remaining time)

These categories were used to prioritise the workload.

### Epics

5 epics were created using Github milestones and the user stories (uploaded as issues in the project).

<img src="docs/epics1.png" alt="a screenshot of the project epics made using GitHub Milestones">
<img src="docs/epics2.png" alt="a screenshot of the project epics made using GitHub Milestones">

### Kanban board

GitHub Kanban boards were used to track the progress of development:

<img src="docs/kanban.png" alt="a screenshot of the project kanban board">

## Technical Design

### Data Models

* Django models were used to represent the tables specified in the technical design of the backend.
* Data points are represented as attributes of the model (inheriting from django's model class).
* For this project, all tables' primary keys are the default django ids for object instances.

#### User model

* This was made using the django allauth library. This library handles all authentication out of the box. From the user it takes a username, email and password.

#### Profile model
* This represents users' profile data in the database
* The status attribute is used to filter profiles so that users can find and 'star' profiles of users who are likley to help them out on the forum.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | profile_owner | User | on_delete=models.CASCADE, null=True, |
|  | bio | text | |
|  | profile_pic | ImageField | upload_to='images/', default="..." |
|  | created_at | DateTime | auto_now_add=True |
|  | updated_at | DateTime | auto_now_add=True |
|  | status | char | max_length=300, choices=CHOICES |

#### Post model
* This represents users' post data in the database
* The category attribute is used to filter posts by content type so that users can view content specific to electronics or bikes etc.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | author | User | on_delete=models.CASCADE, null=True, |
|  | content | text | |
|  | image | ImageField | upload_to='images/', default="..." |
|  | created_at | DateTime | auto_now_add=True |
|  | updated_at | DateTime | auto_now_add=True |
|  | category | char | max_length=300, choices=CHOICES |

#### Comment model
* This represents users' comment data in the database.
* Contains both post and user as foreign keys.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | author | User | on_delete=models.CASCADE, null=True, |
| fk | post | Post | on_delete=models.CASCADE, null=True, |
|  | content | textfield | blank=False |
|  | created_at | DateTime | auto_now_add=True |
|  | updated_at | DateTime | auto_now_add=True |

#### Star, Bookmark, Post upvote, Comment upvote models.
* These models represent user interactions with other users' content and the data models for each are essentially the same.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | owner | User | on_delete=models.CASCADE, null=True, |
| fk | post | Post | on_delete=models.CASCADE, null=True, |
|  | created_at | DateTime | auto_now_add=True |

### Endpoints

#### List and create instances
* List all profiles: ../profiles/
* List all posts: ../posts/
* List all comments: ../comments/
* List all bookmarks: ../bookmarks/
* List all stars: ../stars/
* List all post-upvotes: ../post-upvotes/
* List all comment-upvotes: ../comment-upvotes/

#### Retrieve, update and delete instances
* access single profile: ../profiles/primary-key
* access single post: ../post/primary-key
* access single comment: ../comment/primary-key
* access single star: ../star/primary-key
* access single bookmark: ../bookmark/primary-key
* access single post-upvote: ../post-upvote/primary-key
* access single comment-upvote: ../comment-upvote/primary-key


### Database Schema

Below is an entity relationship diagram for the project. It details how the models detailed above interact with one another.
<details>
    <summary>Screenshot</summary>
    <img src="docs/db_schema.png" alt="database schema diagram">
</details>

## Features

### Ideas for future development
* Messaging system could be implemented to allow users to interact in greater depth without making the comment feed less helpful for other users.
* Increase the options for types of posts on the site to cover more areas of DIY.

## Technologies Used

## Deployment & Local Development

## Testing

## Validation

## Bugs

## Credits