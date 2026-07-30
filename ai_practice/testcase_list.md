# Checkout Review Page - Testcase List

Source requirements: `ai_practice/requirements.md` (`R1` to `R5`).

## Testcases

### R1 - Product Information Visibility

**TC-001** (Positive, High)  
Scenario: Single item review details visible  
Precondition: Cart has 1 valid item with name, attributes, price, image  
Steps:  
1) Open checkout review page  
2) Locate item card  
Expected Behaviour: Item shows thumbnail, accurate product name, selected attributes, and unit price.

**TC-002** (Positive, High)  
Scenario: Multiple items show correct details  
Precondition: Cart has 2+ items with different attributes  
Steps:  
1) Open checkout review page  
2) Compare each item with cart source  
Expected Behaviour: Every item displays its own thumbnail, correct name, selected attributes, and unit price.

**TC-003** (Negative, Medium)  
Scenario: Selected attribute missing in source  
Precondition: Cart item has missing selected attribute (for example size)  
Steps:  
1) Open checkout review page  
2) Check affected item block  
Expected Behaviour: UI shows fallback or explicit validation error; attribute is not silently omitted.

### R2 - Pricing Breakdown Clarity

**TC-004** (Positive, High)  
Scenario: Pricing section fields visible  
Precondition: Cart has valid subtotal, tax, shipping values  
Steps:  
1) Open checkout review page  
2) Locate pricing section  
Expected Behaviour: Subtotal, estimated tax, shipping, and grand total are all visible clearly.

**TC-005** (Positive, High)  
Scenario: Grand total calculation is correct  
Precondition: Known pricing values are available (for example subtotal 100, tax 6, shipping 4)  
Steps:  
1) Open checkout review page  
2) Read all pricing rows  
3) Compute expected total  
Expected Behaviour: Displayed grand total equals subtotal + tax + shipping.

**TC-006** (Boundary, Medium)  
Scenario: Free shipping display and math  
Precondition: Shipping value is 0.00  
Steps:  
1) Open checkout review page  
2) Read shipping and grand total  
Expected Behaviour: Shipping shows `0.00` or `Free`, and grand total math remains correct.

**TC-007** (Boundary, Medium)  
Scenario: Zero tax display and math  
Precondition: Tax value is 0.00  
Steps:  
1) Open checkout review page  
2) Read tax and grand total  
Expected Behaviour: Tax row is visible with zero value and grand total still matches formula.

### R3 - Actionable Product Links

**TC-008** (Positive, High)  
Scenario: Product name link navigation  
Precondition: At least 1 review item exists with valid product URL  
Steps:  
1) Click product name  
2) Observe landing page  
Expected Behaviour: User lands on the matching product details page for that item.

**TC-009** (Positive, High)  
Scenario: Product image link navigation  
Precondition: At least 1 review item exists with valid product URL  
Steps:  
1) Click product image thumbnail  
2) Observe landing page  
Expected Behaviour: User lands on the matching product details page for that item.

**TC-010** (Negative, Medium)  
Scenario: Incorrect link target detection  
Precondition: Test environment has intentionally mismatched link target  
Steps:  
1) Click product name or image  
2) Compare landed product ID with source item  
Expected Behaviour: Test fails and flags defect when landed product does not match clicked item.

### R4 - Data Accuracy

**TC-011** (Positive, High)  
Scenario: Displayed data matches cart source  
Precondition: Source cart payload is available for comparison  
Steps:  
1) Open checkout review page  
2) Compare UI name/attributes/unit price with source  
Expected Behaviour: UI values exactly match source cart data for each item.

**TC-012** (Boundary, Medium)  
Scenario: Currency format consistency  
Precondition: Prices include decimal values  
Steps:  
1) Open checkout review page  
2) Verify all price strings  
Expected Behaviour: All prices follow consistent currency formatting (for example `$12.34`).

**TC-015** (Negative, High)  
Scenario: Product name missing from source  
Precondition: Cart item has null/empty product name  
Steps:  
1) Open checkout review page  
2) Locate affected item  
Expected Behaviour: UI does not show blank name; fallback text appears and checkout is blocked as defect.

**TC-016** (Negative, High)  
Scenario: Unit price missing from source  
Precondition: Cart item has null/empty unit price  
Steps:  
1) Open checkout review page  
2) Locate affected item and pricing section  
Expected Behaviour: UI shows explicit error/fallback and prevents checkout until valid unit price exists.

### R5 - No Surprise Checkout Experience

**TC-013** (Positive, High)  
Scenario: Required pricing shown before order action  
Precondition: User is on checkout review before place-order click  
Steps:  
1) Open checkout review page  
2) Inspect page before clicking place order  
Expected Behaviour: Required pricing fields are visible before place-order action is possible.

**TC-014** (Negative, High)  
Scenario: Missing pricing field blocks checkout  
Precondition: One required pricing field is intentionally removed  
Steps:  
1) Open checkout review page  
2) Attempt place-order flow  
Expected Behaviour: Checkout progression is blocked or explicit blocking error is shown.

## Coverage Summary

- R1 covered by: `TC-001`, `TC-002`, `TC-003`
- R2 covered by: `TC-004`, `TC-005`, `TC-006`, `TC-007`
- R3 covered by: `TC-008`, `TC-009`, `TC-010`
- R4 covered by: `TC-011`, `TC-012`, `TC-015`, `TC-016`
- R5 covered by: `TC-013`, `TC-014`

## Suggested First Automation Batch

Start with these 6 for quick value:

- `TC-001` (R1)
- `TC-004` (R2)
- `TC-005` (R2)
- `TC-008` (R3)
- `TC-011` (R4)
- `TC-013` (R5)
