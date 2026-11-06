# QuickConnect frontend

React + TypeScript web client built with Vite. The initial UI shell is mobile-first and uses the QuickConnect palette. Product workflows will be added in later implementation steps.

## Development

Requirements: Node.js 22.12 or newer and npm.

```sh
npm install
cp .env.example .env.local
npm run dev
```

Set `VITE_API_BASE_URL` to the backend API base path. API requests include browser cookies for server-side sessions. Do not add authentication tokens to local storage.

## Commands

- `npm run dev` — start Vite development server.
- `npm run build` — type-check and create the production frontend build.
- `npm run preview` — serve the built frontend locally.
