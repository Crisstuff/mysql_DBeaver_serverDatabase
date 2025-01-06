const express = require('express');
const app = express();
const port = 3000;

// Definer en GET-endepunkt
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start serveren
app.listen(port, () => {
  console.log(`Serveren kjører på http://localhost:${port}`);
});
