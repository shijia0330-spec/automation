# AI Test Requirements (Source of Truth)

Use this file as the single source for AI testcase generation.

## Feature

Checkout Review Page (e-commerce).

## Requirements

- **R1: Product Information Visibility**
  - Every cart/review item must show a thumbnail image.
  - Every item must show the correct product name.
  - Every item must show selected attributes (for example size, color).
  - Every item must show its individual unit price.

- **R2: Pricing Breakdown Clarity**
  - Page must show item subtotal.
  - Page must show estimated taxes.
  - Page must show shipping costs.
  - Page must show the final grand total.
  - Grand total must equal subtotal + taxes + shipping.

- **R3: Actionable Product Links**
  - Product image must be clickable.
  - Product name must be clickable.
  - Clicking image or name must navigate to the correct product details page.

- **R4: Data Accuracy**
  - Displayed product name, attributes, and unit price must match source cart data.
  - Pricing values must use consistent currency formatting.

- **R5: No Surprise Checkout Experience**
  - Required pricing fields must appear before place-order action.
  - Missing pricing fields should be treated as blocking defects.

## Test Coverage Matrix (Fill During Review)

| Requirement ID | Covered Test IDs | Status |
|---|---|---|
| R1 |  | Not reviewed |
| R2 |  | Not reviewed |
| R3 |  | Not reviewed |
| R4 |  | Not reviewed |
| R5 |  | Not reviewed |

## AI Prompt Template (Copy/Paste)

Generate test cases from the checkout review requirements below.

Requirements:
- R1 ...
- R2 ...
- R3 ...
- R4 ...
- R5 ...

Output JSON fields:
test_id, requirement_id, scenario, precondition, steps, test_data, expected_behaviour, type, priority

Constraints:
- include positive, negative, and boundary cases
- no duplicate scenarios
- each requirement must be covered by at least 2 tests
- list uncovered requirements at the end (if any)
