# syntax=docker/dockerfile:1
FROM node:22-alpine

ENV NODE_ENV=development

WORKDIR /app
RUN chown node:node /app
USER node

# Dependencies first (cached layer).
COPY --chown=node:node package.json package-lock.json ./
RUN npm ci

COPY --chown=node:node . .

EXPOSE 5173

# Dev: Vite dev server with HMR, reachable from outside the container.
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
