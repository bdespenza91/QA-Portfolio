Test Execution Report — GroceryMate

Application: GroceryMate
URL: https://grocerymate.masterschool.com/

Tester: Barry Despenza
Date: April 14, 2026
Environment: Chrome (latest), macOS

Feature 1: Product Rating System

Scenario 1: Valid Rating Submission

User Story:
As a logged-in user who purchased a product, I want to submit a rating so that I can share feedback

| Step# | Action                        | Expected Outcome               | Actual Outcome   | OK/NOK | URL | Link to Issue |
| ----- | ----------------------------- | ------------------------------ | ---------------- | ------ | --- | ------------- |
| 1     | Log in                        | User logged in                 | Login successful | OK     |     |               |
| 2     | Navigate to purchased product | Product page loads             | Dont work        | NOK    |     |  [#1](https://github.com/bdespenza91/example-portfolio/issues/1)             |
| 3     | Select 5-star rating          | Rating selected                | Dont work        | NOK    |     |  [#2](https://github.com/bdespenza91/example-portfolio/issues/2)             |
| 4     | Enter feedback (100 chars)    | Feedback accepted              | No feedback      | NOK    |     |  [#3](https://github.com/bdespenza91/example-portfolio/issues/3)             |
| 5     | Submit rating                 | Rating displayed under product | Not displayed    | NOK    |     |  [#8](https://github.com/bdespenza91/example-portfolio/issues/8)            |

Scenario 2: Rating Without Purchase

User Story:
As a user, I should not be able to rate products I haven’t purchased.

| Step# | Action               | Expected Outcome        | Actual Outcome | OK/NOK | URL | Link to Issue |
| ----- | -------------------- | ----------------------- | -------------- | ------ | --- | ------------- |
| 1     | Log in (no purchase) | User logged in          | OK             | OK     |     |               |
| 2     | Navigate to product  | Product loads           | OK             | OK     |     |               |
| 3     | Submit rating        | Error message displayed | OK             | OK     |     |               |

Scenario 3: Feedback Character Limit

User Story:
As a user, I want feedback length to be limited to ensure proper display.

| Step# | Action                       | Expected Outcome        | Actual Outcome              | OK/NOK | URL | Link to Issue      
| ----- | ---------------------------- | ----------------------- | --------------------------- | ------ | --- | -------------      
| 1     | Enter 300-character feedback | Accepted                | Accepted                    | OK     |     |                    
| 2     | Enter 301-character feedback | Error message displayed | Accepted without validation | NOK    | [#3](https://github.com/bdespenza91/example-portfolio/issues/3)     

Scenario 4: Empty Feedback Submission

User Story:
As a user, I should be able to submit a rating without feedback if optional.

| Step# | Action                         | Expected Outcome | Actual Outcome   | OK/NOK | URL | Link to Issue |
| ----- | ------------------------------ | ---------------- | ---------------- | ------ | --- | ------------- |
| 1     | Submit rating without feedback | Rating submitted | Unsubmitted      | NOK    |     |   [#4](https://github.com/bdespenza91/example-portfolio/issues/4)            |

Feature 2: Age Verification for Alcohol

Scenario 6: Access Alcohol Category

User Story:
As a user, I should verify my age before accessing alcohol products.

| Step# | Action                       | Expected Outcome               | Actual Outcome | OK/NOK | URL | Link to Issue |
| ----- | ---------------------------- | ------------------------------ | -------------- | ------ | --- | ------------- |
| 1     | Navigate to alcohol category | Age verification modal appears | No modal shown | NOK    |     |               |

Scenario 7: Valid Age Access (18+)

User Story:
As a user 18+, I should access alcohol products.

| Step# | Action                         | Expected Outcome | Actual Outcome | OK/NOK | URL | Link to Issue |
| ----- | ------------------------------ | ---------------- | -------------- | ------ | --- | ------------- |
| 1     | Enter DOB = (Today - 17 years) | Access denied    | Access granted | NOK    |     | 🔗 Bug #2      |

Scenario 9: Invalid DOB Input

User Story:
As a user, I should receive validation errors for invalid DOB.

| Step# | Action                   | Expected Outcome    | Actual Outcome | OK/NOK | URL | Link to Issue |
| ----- | ------------------------ | ------------------- | -------------- | ------ | --- | ------------- |
| 1     | Enter DOB = "99/99/9999" | Error message shown | Accepted       | NOK    |     | 🔗 Bug #3     |

Feature 3: Shipping Cost Changes

Scenario 10: Free Shipping Threshold (€50)

User Story:
As a user, I want free shipping when my cart reaches €20.

| Step# | Action                 | Expected Outcome      | Actual Outcome             | OK/NOK | URL | Link to Issue |
| ----- | ---------------------- | --------------------- | -------------------------- | ------ | --- | ------------- |
| 1     | Add items totaling €50 | Free shipping applied | Applied                    | OK     |     |               |

Scenario 11: Below Threshold (€20)

User Story:
As a user, I should pay shipping below €50.

| Step# | Action                    | Expected Outcome        | Actual Outcome      | OK/NOK | URL | Link to Issue |
| ----- | ------------------------- | ----------------------- | ------------------- | ------ | --- | ------------- |
| 1     | Add items totaling €49.99 | €5 shipping fee applied | Correct fee applied | OK     |     |               |

Scenario 12: Dynamic Shipping Updates

User Story:
As a user, I want shipping cost to update dynamically.

| Step# | Action               | Expected Outcome | Actual Outcome | OK/NOK | URL | Link to Issue |
| ----- | -------------------- | ---------------- | -------------- | ------ | --- | ------------- |
| 1     | Add item (€20)       | €5 shipping      | Correct        | OK     |     |               |
| 2     | Add item (total €55) | Free shipping    | Still shows €5 | NOK    |     | 🔗 Bug #4     |

Scenario 13: Discount Impact on Shipping

User Story:
As a user, shipping should update after discounts.

| Step# | Action               | Expected Outcome     | Actual Outcome      | OK/NOK | URL | Link to Issue |
| ----- | -------------------- | -------------------- | ------------------- | ------ | --- | ------------- |
| 1     | Cart = €55           | Free shipping        | OK                  | OK     |     |               |
| 2     | Apply discount → €45 | Shipping fee applied | Still free shipping | NOK    |     | 🔗 Bug #5    |

Scenario 14: Empty Cart Behavior

User Story:
As a user, I should not see shipping cost when cart is empty.

| Step# | Action           | Expected Outcome | Actual Outcome           | OK/NOK | URL | Link to Issue |
| ----- | ---------------- | ---------------- | ------------------------ | ------ | --- | ------------- |
| 1     | Remove all items | No shipping cost | Shipping still displayed | OK     |     |               |
