mandroobi
===
[![Run Status](https://api.shippable.com/projects/59041549cd25170600366419/badge?branch=master)](https://app.shippable.com/github/ivansabik/mandroobi)
[![Coverage Badge](https://api.shippable.com/projects/59041549cd25170600366419/coverageBadge?branch=master)](https://app.shippable.com/github/ivansabik/mandroobi)
[![Lintly](https://lintly.com/gh/ivansabik/mandroobi/badge.svg?1)](https://lintly.com/gh/ivansabik/mandroobi/)

App for preparing budget and forecast Financial Statements (Balance Sheet and Income Statement) based on planning drivers.

### Functionalities

- Add dimension members
- Refresh exchange rates from external provider(s)
- Manually override exchange rate
- Define new top-down allocation
- Plan using manual input values:
  - Input planning values using web interface
  - Input planning values using spreadsheets
  - Input planning values uploading a CSV/spreadsheet
- Plan using planning statistical model (linear regression, weighted average, naïve, etc)
- Plan using custom Python code
- Run allocation to plan top-down
- View audit records

### REST API

The following resources are available:
- Account
- Accounting Period
- Business Unit
- Currency
- Driver
- Scenario

Available methods are GET, PUT, DELETE and PATCH
