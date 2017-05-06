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

## Account

#### PUT http://localhost:5000/account/10000

```
curl -X PUT \
  http://localhost:5000/account/10000 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"description": "Cash & Banks",
	"parent_id": "",
	"type": "asset"
}'
```

Will return:

```javascript
{
  "data": {
    "description": "Cash & Banks",
    "id": "10000",
    "parent_id": "",
    "type": "asset"
  },
  "message": "10000 id created",
  "success": true
}
```

#### GET http://localhost:5000/account/10000

```
curl -X GET \
  http://localhost:5000/account/10000 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"description": "Cash & Banks",
	"parent_id": "",
	"type": "asset"
}'
```

Will return:

```javascript
{
  "description": "Cash & Banks",
  "id": "10000",
  "parent_id": "",
  "type": "asset"
}
```
#### DELETE http://localhost:5000/account/10000

```
curl -X DELETE \
  http://localhost:5000/account/10000 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"description": "Cash & Banks",
	"parent_id": "",
	"type": "asset"
}'
```

Will return:

```javascript
{
  "description": "Cash & Banks",
  "id": "10000",
  "parent_id": "",
  "type": "asset"
}
```

#### PATCH http://localhost:5000/account/10000

```
curl -X PATCH \
  http://localhost:5000/account/10000 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"description": "Petty Cash"
}'
```

Will return:

```javascript
{
  "date": {
    "description": "Petty Cash",
    "id": "10000",
    "parent_id": null,
    "type": null
  },
  "message": "10000 id updated",
  "success": true
}
```

## Accounting Period

#### PUT http://localhost:5000/accounting_period/20000101
```
curl -X PUT \
  http://localhost:5000/accounting_period/20000101 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"description": "Jan 2001",
	"parent_id": "",
	"month": 1,
	"year": 2000
}'
```

```javascript
{
  "data": {
    "date": null,
    "day": null,
    "description": "Jan 2001",
    "id": "20000101",
    "month": 1,
    "quarter": 1,
    "year": 2000
  },
  "message": "20000101 id created",
  "success": true
}
```
#### GET http://localhost:5000/accounting_period/20000101

```
curl -X GET \
  http://localhost:5000/accounting_period/20000101 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 7c21caf2-5ab3-cf71-6256-d39d24eb20ca' \
  -d '{
	"description": "Jan 2001",
	"parent_id": "",
	"month": 1,
	"year": 2000
}'
```

```javascript
{
  "date": null,
  "day": null,
  "description": "Jan 2001",
  "id": "20000101",
  "month": 1,
  "quarter": 1,
  "year": 2000
}
```
#### DELETE http://localhost:5000/accounting_period/20000101

```
curl -X DELETE \
  http://localhost:5000/accounting_period/20000101 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 1a45f614-cc38-b9cb-a12f-32f1dc9dcbfe' \
  -d '{
	"description": "Jan 2001",
	"parent_id": "",
	"month": 1,
	"year": 2000
}'
```

```javascript
{
  "data": {
    "date": null,
    "day": null,
    "description": "Jan 2001",
    "id": "20000101",
    "month": 1,
    "quarter": 1,
    "year": 2000
  },
  "message": "20000101 id deleted",
  "success": true
}
```

#### PATCH http://localhost:5000/accounting_period/20000101

## Business Unit

#### PUT
#### GET
#### DELETE
#### PATCH

## Currency

#### PUT
#### GET
#### DELETE
#### PATCH

## Driver

#### PUT
#### GET
#### DELETE
#### PATCH

## Scenario

#### PUT
#### GET
#### DELETE
#### PATCH
