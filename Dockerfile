FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

RUN git clone https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques /app/docs
RUN npm install -g docsify-cli
COPY patch.py /app
RUN python3 patch.py

ADD https://cdn.jsdelivr.net/npm/docsify/themes/vue.css /app/docs/vue.css
ADD https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/sidebar.min.css /app/docs/sidebar.min.css

ADD https://unpkg.com/docsify-plugin-flexible-alerts /app/docs/alert.js
ADD https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js /app/docs/search.min.js
ADD https://cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js /app/docs/docsify.min.js
ADD https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js /app/docs/docsify-sidebar-collapse.min.js

COPY index.html /app/docs/index.html
COPY package.json /app

RUN touch /app/docs/.nojekyll
RUN cp /app/docs/SUMMARY.md /app/docs/_sidebar.md

EXPOSE 3000 
CMD ["npx", "docsify", "serve", "docs"]

