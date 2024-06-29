# django's.film-club

## Introduction

django's.film-club is a film review website for film lovers. The aim of the website is to create a space for movie lovers to share the opinions and express their love for the cinema with other film lovers.

Films will forever be a visual medium for humans to tell stories, the role of the admin on the website will be to post film subjects where users will be able to post their reviews under the film subject. New film subjects should be posted weekly by the admin to keep the website relevant and users visiting on a frequent basis.

[Visit the Website Here](https://djangos-film-club-532a7f9d2300.herokuapp.com/)

![Responsive Image]()

## UX - User Experience
* Strategy Plane
* Scope Plane
* Structure Plane
* Skeleton Plane
* Surface Plane


## Strategy Plane
A plan is needed to ensure the purpose of the website meets the needs of site users, the audience and the site owner.

### Target Audience
The target audience can be wide for movie watchers but as this is a digital review platform the audience will have to be competant in using technology but also interested in spending time on movie review forums.

* 18 - 35 year olds
* Film enthusiasts of variety of genres.

### User Stories

#### Catalogue of film subjects - Should have
* As a user, I can view a catalog of film subjects so that I can see past film subjects and view the reviews from other users.

#### Post a review on a film - Must have
* As a user I can type up a review on a film so that I can submit the review on the site for other user's to read.

#### Add films to a genre category - Could have
* As an admin, I can add films to a genre so that users can see the genre a film belongs to as part of the details of a film.

#### Register and login to review and add comments - Must have
* As a visitor, I can register so that I can leave a review on a film and comment on reviews.

#### Delete reviews - Must have
* As a user, I can delete my reviews to remove unwanted reviews.

#### Edit reviews - Must have
- As a user, I can edit my reviews so that I can amend what I have written.

#### Add film to review - Must have
* As an admin, I can add a film subject so that site visitors can see the upcoming film to watch and add reviews.


## Scope Plane
I identified 2 main pages were needed for the website to be able to functon as required;

Film Details page
* A page for each film where a films details can be viewed.
* Reviews can be viewed on the film on the page.
* Only logged in users can leave reviews.

Add new film page
* A page where an admin can only access to add new films.

For the site to fucntion well and a good user experience, the other pages needed were;
* Homepage - This page can contain the catalogus of films
* Login/ register page


## Structure Plane
For the website to be able to fulfill its basic goal to post weekly film subject for users to review, there are 2 models and applications that the site will feed off;
* Movies
* Reviews


### Movies
Only an admin will be able to post films which will contain details of film, this is espacially for those who have not seen the film and this will give them some information before they watch it;

![Movie diagram](media/structure_pl/film_diagram.png)


### Reviews
Only an admin will be able to post films which will contain details of film, this is espacially for those who have not seen the film and this will give them some information before they watch it;

![Movie diagram](media/structure_pl/reviews_diagram.png)


## Skeleton Plane
I have created wireframes of 3 pages (homepage, film_details and post_film) to design the layout of the pages.


### Home page
A user will be introduced to the website with a hero image and a welcome messsage. Below the hero image will be the film listings that have been posted and new films will appear here. The 'film catalogue' button on the hero image will take the user to the bottom of the page. The button at the bottom of the page will appear if there are more than 3 films so users can navigate.

The nav bar on the homepage wireframe is what it will look like for a user that has not logged in. The homepage and logo will always take the user to the homepage, the 'films' link will take a user to the bottom to the catalogue. The links to register and login will give users the option to create an account or login if the user has an account already.

![Homepage wireframe](media/skeleton_pl/homepage wireframe.JPG)


### Film Details
The page will hold film information and image. Below this will display the reviews that have been posted by users of the film and beside there will be a form which can be filled for users to leave their own reviews. Only logged in users can leave a review.

The nav is what will look like for a logged in user, the option for logout is present instead of 'login' and 'register'.

![Homepage wireframe](media/skeleton_pl/film_detail wireframe.JPG)


### Post Film
This page will only be available for an admin user. This can be seen on the navbar the 'Posts' link only appears for admins.

This page is where a new film can be added by filling out the form. This page will also contain a list of films on the website, delete and edit buttons can be added here for admins to either delete or edit the entries.

![Homepage wireframe](media/skeleton_pl/post_film wireframe.JPG)


## Surface Plane


### Colour theme and design



## Features


## Lessons Learned
Not enough user stories