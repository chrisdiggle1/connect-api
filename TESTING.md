## Testing and Validation

### Contents

[Code Validation](#code-validation)

[Manual Testing](#manual-testing)

[Automated Testing](#automated-testing)

## Code Validation

## Manual Testing

## Automated Testing

### AttendingList View Tests

| Test name | Result |
| --- | --- |
| test_can_list_attending | Pass |
| test_logged_in_user_can_confirm_attending | Pass |
| test_logged_out_user_cannot_confirm_attending | Pass |

<details>
<summary>AttendingList view test</summary>
<img src="images/attendinglistview-tests.PNG">
</details>

<br>

### AttendingDetail View Tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_attending | Pass |
| test_user_can_delete_own_attending | Pass |
| test_user_cannot_delete_other_users_attending | Pass |

<details>
<summary>AttendingDetail view test</summary>
<img src="images/attendingdetailview-tests.PNG">
</details>

<br>

### CommentList View Tests

| Test name | Result |
| --- | --- |
| test_can_list_comments | Pass |
| test_logged_in_user_can_create_comment | Pass |
| test_logged_out_user_cannot_create_comment | Pass |

<details>
<summary>CommentList view test</summary>
<img src="images/commentlistview-tests.PNG">
</details>

<br>

### CommenDetail View Tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_comment | Pass |
| test_user_can_update_own_comment | Pass |
| test_user_cannot_update_other_users_comment | Pass |
| test_user_can_delete_own_comment | Pass |
| test_user_cannot_delete_other_users_comment | Pass |

<details>
<summary>CommentDetail view test</summary>
<img src="images/commentdetailview-tests.PNG">
</details>

<br>

### EventList View Tests

| Test name | Result |
| --- | --- |
| test_can_list_events | Pass |
| test_logged_in_user_can_create_event | Pass |
| test_logged_out_user_cannot_create_event | Pass |

<details>
<summary>EventList view test</summary>
<img src="images/eventlistview-tests.PNG">
</details>

<br>

### EventDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_event_using_valid_id | Pass |
| test_cannot_retrieve_event_using_invalid_id | Pass |
| test_user_can_update_own_event | Pass |
| test_user_cannot_update_someone_elses_event | Pass |

<details>
<summary>EventList view test</summary>
<img src="images/eventdetailview-tests.PNG">
</details>

<br>

### FollowerList View tests

| Test name | Result |
| --- | --- |
| test_can_list_followers | Pass |
| test_logged_in_user_can_create_follow | Pass |
| test_logged_out_user_cannot_create_follow | Pass |

<details>
<summary>FollowerList view test</summary>
<img src="images/followerlistview-tests.PNG">
</details>

<br>

### FollowerDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_follow | Pass |
| test_user_can_delete_own_follow | Pass |
| test_user_cannot_delete_other_users_follow | Pass |

<details>
<summary>FollowerDetail view test</summary>
<img src="images/followerdetailview-tests.PNG">
</details>

<br>

### InterestedList View tests

| Test name | Result |
| --- | --- |
| test_can_list_interested | Pass |
| test_logged_in_user_can_confirm_interested | Pass |
| test_logged_out_user_cannot_confirm_interested | Pass |

<details>
<summary>InterestedList view test</summary>
<img src="images/interestedlistview-tests.PNG">
</details>

<br>

### InterestedDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_interested | Pass |
| test_user_can_remove_own_interested | Pass |
| test_user_cannot_remove_other_users_interested | Pass |

<details>
<summary>InterestedDetail view test</summary>
<img src="images/interesteddetailview-tests.PNG">
</details>

<br>

### LikesList View tests

| Test name | Result |
| --- | --- |
| test_can_list_likes | Pass |
| test_logged_in_user_can_add_like | Pass |
| test_logged_out_user_cannot_add_like | Pass |

<details>
<summary>LikesList view test</summary>
<img src="images/likelistview-tests.PNG">
</details>

<br>

### LikesDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_like | Pass |
| test_user_can_remove_own_like | Pass |
| test_user_cannot_remove_other_users_like | Pass |

<details>
<summary>LikesDetail view test</summary>
<img src="images/likedetailview-tests.PNG">
</details>

<br>

### ProfilesList View tests

| Test name | Result |
| --- | --- |
| test_can_list_profiles | Pass |
| test_profiles_include_events_count | Pass |
| test_profiles_include_followers_count | Pass |
| test_profiles_include_following_count | Pass |

<details>
<summary>ProfilesList view test</summary>
<img src="images/profilelistview-tests.PNG">
</details>

<br>

### ProfilesDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_profile | Pass |
| test_user_can_update_own_profile | Pass |
| test_user_cannot_update_other_users_profile | Pass |

<details>
<summary>ProfilesDetail view test</summary>
<img src="images/profiledetailview-tests.PNG">
</details>

<br>

### ReviewsList View tests

| Test name | Result |
| --- | --- |
| test_can_list_reviews | Pass |
| test_logged_in_user_can_create_review | Pass |
| test_logged_out_user_cannot_create_review | Pass |

<details>
<summary>ReviewsList view test</summary>
<img src="images/reviewlistview-tests.PNG">
</details>

<br>

### ReviewsDetail View tests

| Test name | Result |
| --- | --- |
| test_can_retrieve_review | Pass |
| test_user_can_update_own_review | Pass |
| test_user_cannot_update_other_users_review | Pass |
| test_user_can_delete_own_review | Pass |
| test_user_cannot_delete_other_users_review | Pass |

<details>
<summary>ReviewsDetail view test</summary>
<img src="images/reviewdetailview-tests.PNG">
</details>

<br>