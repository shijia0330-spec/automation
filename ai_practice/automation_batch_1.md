# Automation Batch 1 Plan

Source:
- `ai_practice/requirements.md`
- `ai_practice/testcase_list.md`

Goal:
- Automate high-priority baseline checks first.

## Selected Cases (Batch 1)

1. `TC-001` (R1) - Product info visible for single item
2. `TC-004` (R2) - Pricing section fields visible
3. `TC-005` (R2) - Grand total calculation correct
4. `TC-008` (R3) - Product name link navigation
5. `TC-011` (R4) - Displayed values match source cart data
6. `TC-013` (R5) - Required pricing shown before place-order action

## Pre-automation Checklist

- [ ] Confirm checkout review URL
- [ ] Confirm stable locators for item card, pricing rows, place-order button
- [ ] Confirm test data setup method (API fixture, DB seed, or mock response)
- [ ] Confirm product details route format for link verification
- [ ] Confirm currency format rule (e.g. `$12.34`)

## Suggested Test File Structure

Create:
- `web_automation/tests/test_checkout_review_batch1.py`

Recommended naming:
- `test_tc_001_product_info_visible_single_item`
- `test_tc_004_pricing_fields_visible`
- `test_tc_005_grand_total_math`
- `test_tc_008_product_name_link_navigation`
- `test_tc_011_ui_matches_source_cart_data`
- `test_tc_013_required_pricing_before_place_order`

## Assertion Targets by Case

### TC-001
- Item card exists
- Thumbnail exists and is visible
- Product name is non-empty and matches expected
- Selected attributes visible
- Unit price visible

### TC-004
- Subtotal row visible
- Estimated tax row visible
- Shipping row visible
- Grand total row visible

### TC-005
- Parse subtotal, tax, shipping, grand total as numbers
- Assert: `grand_total == subtotal + tax + shipping`

### TC-008
- Click product name link
- Assert current URL includes expected product ID or slug

### TC-011
- Compare UI values vs source cart payload:
  - `name`
  - `attributes`
  - `unit_price`

### TC-013
- Before clicking place order:
  - subtotal/tax/shipping/grand total all visible

## Execution Order

1. TC-004 (fast visual check)
2. TC-001
3. TC-013
4. TC-005 (math parse)
5. TC-008 (navigation)
6. TC-011 (source-vs-UI compare)

## Definition of Done (Batch 1)

- [ ] 6 tests automated
- [ ] All pass locally
- [ ] No flaky wait/sleep patterns
- [ ] Tests tagged with case ID in test name
- [ ] Results ready for CI run
