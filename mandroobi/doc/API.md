<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

	- [Account](#account)
			- [PUT http://localhost:5000/account/10000](#put-httplocalhost5000account10000)
			- [GET http://localhost:5000/account/10000](#get-httplocalhost5000account10000)
			- [DELETE http://localhost:5000/account/10000](#delete-httplocalhost5000account10000)
			- [PATCH http://localhost:5000/account/10000](#patch-httplocalhost5000account10000)
	- [Accounting Period](#accounting-period)
			- [PUT http://localhost:5000/accounting_period/20000101](#put-httplocalhost5000accountingperiod20000101)
			- [GET http://localhost:5000/accounting_period/20000101](#get-httplocalhost5000accountingperiod20000101)
			- [DELETE http://localhost:5000/accounting_period/20000101](#delete-httplocalhost5000accountingperiod20000101)
			- [PATCH http://localhost:5000/accounting_period/20000101](#patch-httplocalhost5000accountingperiod20000101)
	- [Business Unit](#business-unit)
			- [PUT](#put)
			- [GET](#get)
			- [DELETE](#delete)
			- [PATCH](#patch)
	- [Currency](#currency)
			- [PUT](#put)
			- [GET](#get)
			- [DELETE](#delete)
			- [PATCH](#patch)
	- [Driver](#driver)
			- [PUT](#put)
			- [GET](#get)
			- [DELETE](#delete)
			- [PATCH](#patch)
	- [Scenario](#scenario)
			- [PUT](#put)
			- [GET](#get)
			- [DELETE](#delete)
			- [PATCH](#patch)

<!-- /TOC -->

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

Will return:

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

Will return:

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

Will return:

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

```
curl -X PATCH \
  http://localhost:5000/accounting_period/20000101 \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 30e3b16a-e65b-ec85-34dc-d0f97afd1e96' \
  -d '{
	"description": "January of 2001"
}'
```

Will return:

```javascript
{
  "date": {
    "date": null,
    "day": null,
    "description": "January of 2001",
    "id": "20000101",
    "month": 1,
    "quarter": 1,
    "year": 2000
  },
  "message": "20000101 id updated",
  "success": true
}
```


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
