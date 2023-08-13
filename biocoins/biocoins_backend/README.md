<!-- PROJECT TITLE -->
  <h1 align="center">BioCoins</h1>
 <h2 2 align="center">
    Bringing Clinical Trials To Life
    <br />
    </h2>

## Application Description

application backend

## Table of Contents

<details>
<summary>BioCoins</summary>

- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Running](#running)
- [SQLite Path](#sqlight-path)
- [Data Migration](#data-migration)
- [API](#api)

</details>

## Requirements

- [Node.js](https://nodejs.org/) >= 12.x
- [SQLite](https://www.sqlite.org/index.html)

<br />

## How to run backend server

**Step #1** - Clone the project

```bash
$ git clone https://github.com/agelesspartners/biocoins/tree/main/biocoins_backend
$ cd api-server-nodejs
```

**Step #2** - Install dependencies via NPM or Yarn

```bash
$ npm i
// OR
$ yarn
```

**Step #3** - Run the SQLite migration via TypeORM

```bash
$ npm run typeorm migration:run
// OR
$ yarn typeorm migration:run
```

**Step #4** - Start the API server (development mode)

```bash
$ npm dev
// OR
$ yarn dev
```

**Step #5** - Production Build (files generated in `build` directory)

```bash
$ npm build
// OR
$ yarn build
```

**Step #6** - Start the API server for production (files served from `build/index.js`)

```bash
$ npm start
// OR
$ yarn start
```

The API server will start using the `PORT` specified in `.env` file (default 5000).

<br />

## SQLite Path

The SQLite Path is set in `.env`, as `SQLITE_PATH`

## Database migration

> run migration:

```
$ yarn typeorm migration:run
```

<br />

## API

```
use: ../media/api.postman_collection.json for quick setup with Postman

```

> **Register** - `api/users/register`

```
POST api/users/register
Content-Type: application/json

{
    "username":"test",
    "password":"pass",
    "email":"test@appseed.us"
}
```

<br />

> **Login** - `api/users/login`

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass",
    "email":"test@appseed.us"
}
```

<br />

> **Logout** - `api/users/logout`

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```
