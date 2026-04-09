#  Test Plan – GroceryMate Webshop

---

##  Analyze the Product

### Objective

**What is the objective?**  
To validate the correct implementation and behavior of newly introduced features (Product Rating System, Age Verification for Alcohol, and Shipping Cost Logic) while ensuring no regression in existing webshop functionalities.

---

### User Base

**Who will the product be used by? Who are your user stakeholders?**

- Customers (primary users purchasing products)
- Registered users (with purchase history)
- Guest users (browsing/searching products)
- Business stakeholders (Product Owners, Marketing, Operations)
- QA & Development teams

---

### Hardware and Software Specifications

#### Hardware Requirements:
- Devices: PCs, laptops, smartphones, tablets
- Specifications: Minimum 4GB RAM, 2GHz processor

#### Software Requirements:
- Operating Systems: Windows, macOS, Android, iOS
- Browsers: Chrome, Firefox, Safari, Edge
- Dependencies:
  - Backend services (authentication, order processing)
  - Payment gateway
  - Cookie/session management (for age verification)

---

### Product Functionality

#### Existing Functionality:
- User registration and login
- Product search, sorting, and category browsing
- Add to favorites
- Add to basket
- Checkout process (billing, shipping, payment)
- Total price calculation

#### New Functionality:

**1. Product Rating System**
- 1–5 star rating
- Optional feedback (max 300 characters)
- Only logged-in users who purchased can rate
- One rating per user per product (editable/deletable)
- Average rating displayed
- Feedback moderation and profanity filtering

**2. Age Verification for Alcohol**
- Modal appears when accessing alcohol-related content
- User must input date of birth (DD/MM/YYYY)
- Users under 18 are denied access and redirected
- Verification stored via cookies (session-based)
- Applies to category, product pages, and direct links

**3. Shipping Cost Changes**
- Free shipping ≥ €50
- €5 fee < €50
- Calculated after discounts, before taxes
- Dynamic updates in cart and checkout
- Edge case: exactly €50 → free shipping

---

## 2. Design the Test Strategy

### Scope of Testing

#### In Scope:
- Product Rating System
- Age Verification logic and enforcement
- Shipping cost calculation and updates
- Integration with checkout flow
- Regression testing of core webshop flows


---

### Type of Testing

- Functional Testing
- UI/UX Testing
- Integration Testing
- Regression Testing
- Negative Testing (invalid inputs, edge cases)
- Exploratory Testing
- Cookie/Session Testing

---

### Risks and Issues

| Risk | Mitigation |
|------|-----------|
| Rating without purchase | Validate backend + UI restrictions |
| Age verification bypass | Test category, search, and direct links |
| Incorrect shipping calculation | Boundary testing (€49.99, €50, €50.01) |
| Cookie/session failure | Cross-browser and session testing |

---

### Test Logistics

- **Test Manager** – QA Lead  
- **QA Engineer** – Functional & regression testing  
- **QA Engineer** – Security & edge-case validation  
- **End User (UAT)** – Usability validation  

---

## 3. Define Test Objectives

### Objectives

- **Functionality:** Ensure all features work according to requirements  
- **GUI:** Validate usability and visual consistency  
- **Performance:** Ensure dynamic updates work correctly  
- **Security:** Prevent unauthorized actions  
- **Usability:** Ensure smooth user flows  

---

### Expected Outcomes

- **Functionality:** Features behave correctly  
- **GUI:** UI is intuitive and responsive  
- **Performance:** Shipping updates instantly  
- **Security:** Restrictions cannot be bypassed  
- **Usability:** Clear and easy user experience  

---

## 4. Define Test Criteria

### Suspension Criteria

- Critical defects block testing
- Test environment unavailable

---

### Exit Criteria

- All test cases executed  
- Run Rate ≥ 95%  
- Pass Rate ≥ 90%  
- No critical/high severity defects open  
- Shipping logic validated  
- Age verification enforced  
- Rating system restrictions validated  
- UAT completed and approved  

---

## 5. Resource Planning

- **Human Resources:**
  - QA Engineers
  - Developers
  - Product Owner
  - UAT participants

- **Hardware:**
  - Desktop, mobile, tablet devices

- **Software:**
  - Browsers: Chrome, Firefox, Safari, Edge
  - OS: Windows, macOS, Android, iOS

- **Infrastructure:**
  - Test environments
  - Test data (users, products, orders)

---

## 6. Plan Test Environment

- **Test Environments:**
  - Real devices and browsers
  - Cookie-enabled environments

- **Environments:**
  - DEV – Development  
  - TEST – QA  
  - ACC – UAT  
  - PROD – Production  

---

## 7. Schedule and Estimation

| Activity | Start Date | End Date | Environment | Responsible | Effort |
|----------|----------|----------|------------|------------|--------|
| Test Planning | 10/04/2026 | 11/04/2026 | All | QA Lead | 8h |
| Test Case Design | 12/04/2026 | 13/04/2026 | All | QA | 16h |
| Functional Testing | 14/04/2026 | 16/04/2026 | TEST | QA | 24h |
| Integration Testing | 17/04/2026 | 18/04/2026 | TEST | QA | 16h |
| Regression Testing | 19/04/2026 | 20/04/2026 | TEST | QA | 16h |
| Exploratory Testing | 21/04/2026 | 21/04/2026 | TEST | QA | 8h |
| UAT | 22/04/2026 | 24/04/2026 | ACC | Users | 16h |
| Production Release | 25/04/2026 | 25/04/2026 | PROD | DevOps | 4h |

---

## 8. Determine Test Deliverables

- Test Plan Document
- Test Cases & Test Scripts
- Test Data
- Test Reports
- Defect Reports
- UAT Sign-off Document

---

##  Notes

This test plan focuses on validating:
- Business-critical logic (pricing, eligibility)
- Security constraints (age verification, access control)
- End-to-end user flows

