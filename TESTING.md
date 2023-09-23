# Fixit DRF API: Testing

## Manual testing using Postman

The website [Postman](https://www.postman.com/product/what-is-postman/) was used to make test requests to the API and check that it returned the expected status codes and JSON responses.

### GET
#### Home page '/'
<details>
    <summary>Screenshot</summary>
    <img src="docs/get_requests/get_list_home.png">
</details>

#### Profiles page '/profiles/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_profiles.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_profiles.png">
</details>

#### Posts page '/posts/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_posts.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_posts.png">
</details>

#### comments page '/coments/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_comments.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_comments.png">
</details>

#### Stars page '/stars/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_stars.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_stars.png">
</details>

#### Bookmarks page '/bookmarks/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_bookmarks.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_bookmarks.png">
</details>

#### Post upvotes page '/post-upvotes/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_post-upvotes.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_post-upvotes.png">
</details>

#### Comment upvotes page '/comment-upvotes/'
<details>
    <summary>Screenshot for list</summary>
    <img src="docs/get_requests/get_list_comment-upvotes.png">
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img src="docs/get_requests/get_one_comment-upvotes.png">
</details>


## Automated Testing / Unit tests

Unit tests for all features of the api were built using django rest framework's APITestCase class. All test pass.

### Profile App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/profile_pass.png">
</details>

### Posts App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/posts_pass.png">
</details>

### Comments App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/comments_pass.png">
</details>

### Bookmarks App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/bookmarks_pass.png">
</details>

### Stars App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/profile_pass.png">
</details>

### Post Upvotes App

<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/post-upvotes_pass.png">
</details>

### Comment Upvotes App
<details>
    <summary>Screenshot</summary>
    <img src="docs/unit_tests/comment-upvotes_pass.png">
</details>