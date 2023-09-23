# Fixit DRF API: Testing

## Manual testing using Postman

The website [Postman](https://www.postman.com/product/what-is-postman/) was used to make test requests to the API and check that it returned the expected status codes and JSON responses.

### GET
#### Home page '/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

#### Profiles page '/profiles/'
<details>
    <summary>Screenshot for list</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### Posts page '/posts/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### comments page '/coments/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### Stars page '/stars/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### Bookmarks page '/bookmarks/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### Post upvotes page '/post-upvotes/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>

#### Comment upvotes page '/comment-upvotes/'
<details>
    <summary>Screenshot</summary>
    <img>
</details>

<details>
    <summary>Screenshot for individual</summary>
    <img>
</details>



## Automated Testing / Unit tests

Unit tests for all features of the api were built using django rest framework's APITestCase class. All test pass.