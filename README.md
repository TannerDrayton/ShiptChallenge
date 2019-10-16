# ShiptChallenge

## ***1) Login page***
### Description: A registered user be able to successfuly log into their shipt account.
### Pre-Condition: User must be a registered member with a valid username and password.
### Assumption: User is using a supported browser.
### Test steps: 
            1) Navigate to shop.shipt.com/login.
            2) In the "EMAIL" field, enter the email of the registered user.
            3) In the "PASSWORD" field, enter the password of the registered user.
            4) Click the "LOG IN" button.
Expected result: network log returns status as 200 and user's home page is displayed. 

## ***2) Why You Buggin***
### A/B. When user logs into shop.shipt.com there is an arrow element on the right side of the display.
![](./shipt_home_normal.png)
### When the window width is reduced below 768 pixels, the arrow dissapear.
![](./shipt_home_broken.png)
### C. If this is bug goes unfixed then users will not be able to scroll through the horizontal product lists. The arrow should be avaliable as long as the user is on a non-mobile browser.
### D. To report this issue I would provide screen shots and a description on how to replicate the bug.
### E. I would rate this bug a 4, because it does inhibit full user functionality, however it is not likely to be replicated by users.