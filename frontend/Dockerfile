FROM node:lts

WORKDIR /usr/src/app

COPY package*.json ./

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]