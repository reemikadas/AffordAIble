# AffordAIble

> **Know what you can afford, before you fall in love with a home.**

**Last updated:** August 15, 2026 at 1:12 AM PDT

## Project overview

AffordAIble is a portfolio project that helps prospective Bay Area homebuyers understand a realistic home-buying budget before beginning their search. The application will combine deterministic financial calculations, current housing-market data, and grounded information about mortgage and down-payment-assistance programs.

The first release will focus on San Jose in Santa Clara County and Fremont in Alameda County. It will provide educational affordability scenarios and potential program matches, not mortgage pre-approval or guaranteed eligibility.

## Current phase: Deterministic calculation foundation

The project currently includes:

- Validated, immutable models for buyer finances, loan scenarios, and housing-cost assumptions
- Front-end and back-end debt-to-income ratio calculations
- Fixed-rate monthly principal-and-interest calculations for 15-year and 30-year mortgages
- Monthly housing-cost estimates covering property tax, homeowners insurance, mortgage insurance, and HOA dues
- A transparent monthly cost breakdown with a calculated total
- 30 passing unit tests covering normal, boundary, and invalid inputs
- Ruff-based code-quality checks

This calculation layer is deliberately independent of any user-interface framework so it can be reused by a future web API and frontend.

## Future phases

### Phase 2: Affordability and cash planning

- Calculate an estimated affordable purchase-price range
- Estimate down payment, closing costs, and recommended cash reserves
- Compare available savings with estimated cash needed
- Return assumptions and calculation explanations with every result

### Phase 3: Bay Area market-data foundation

- Build data pipelines for San Jose and Fremont
- Add current home-value and mortgage-rate observations
- Record source, observation date, retrieval date, and data freshness
- Expand validated coverage to the remaining target cities after the two-city workflow succeeds

### Phase 4: Assistance-program knowledge layer

- Collect and version official federal, California, county, and city program sources
- Store program rules with effective dates and source locations
- Build grounded retrieval with traceable citations
- Evaluate retrieval quality and unsupported-claim risk

### Phase 5: Application orchestration

- Route calculation, market-data, and program-information requests
- Support questions that require multiple capabilities
- Keep all financial arithmetic inside deterministic, tested functions
- Use the language model only to classify or explain grounded results

### Phase 6: Web application and deployment

- Expose the Python calculation layer through a backend API
- Build a responsive web frontend
- Add clear assumptions, data dates, source links, and educational-use disclaimers
- Run end-to-end evaluations and deploy a public portfolio demo

## Important notice

AffordAIble provides educational estimates only. It does not provide mortgage pre-approval, lending, financial, legal, or tax advice. Actual loan terms and program eligibility must be confirmed with an approved lender or housing counselor.
