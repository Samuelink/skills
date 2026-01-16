---
name: housing-eligibility-checker
description: Analyzes second-hand housing purchase eligibility based on user profile. Use this skill when a real estate agent needs to verify if a client is qualified to buy a property (二手房购房资格查询), or when discussing purchase restrictions (限购政策). Supports multi-turn information gathering to determine eligibility.
license: Private
---

# Housing Eligibility Checker

This skill helps real estate agents verify if a potential buyer is eligible to purchase a second-hand property based on local regulations.

## ONE-SHOT USAGE

When the user provides all necessary information in the first prompt, output the eligibility result immediately.

**Required Information**:
1.  **Hukou**: Local or Non-Local?
2.  **Marital Status**: Married or Single?
3.  **Property Count**: How many homes do they currently own in this city?
4.  **Social Security (if Non-Local)**: Do they meet the continuous payment years requirement?

## INTERACTIVE WORKFLOW (Multi-turn)

If the user provides incomplete information, you MUST proactively ask for the missing details. Do not guess.

### Step 1: Analyze Provided Information

Extract the standard profile data from the conversation:
- Resident Status (Hukou)
- Marital Status
- Current Properties

### Step 2: Determine Missing Data

Compare the known info against the requirements in `references/policy_rules.md`.

- If **Non-Local** and **Social Security** status is unknown -> **ASK**: "Does the client have the required years of continuous social security/tax payment?"
- If **Marital Status** is unknown -> **ASK**: "Is the client married or single? This affects the number of properties they can own."
- If **Hukou** is unknown -> **ASK**: "Does the client hold a local Hukou?"

### Step 3: Consult Policy Rules

Read [references/policy_rules.md](references/policy_rules.md) to evaluate the profile.

### Step 4: Output Result

Format the final output clearly:

---
**Purchase Eligibility Check**

- **Client Profile**: [Summary of Hukou, Marriage, Properties, etc.]
- **Result**: ✅ **Eligible** / ❌ **Not Eligible** / ⚠️ **Uncertain**
- **Reason**: [Cite the specific rule from policy_rules.md. E.g., "Local married families can own 2 properties, and they currently own 1."]
- **Next Steps/Advice**: [Optional advice for the agent, e.g., "Prepare typical documents: ID, Marriage Certificate..."]
---
