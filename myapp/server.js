const cors = require('cors');
app.use(cors());

const express = require('express_db')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
const mysql = require('mysql');

// Koble til databasen
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'skole12', // Endre passord hvis nødvendig
    database: 'express_db'
});

db.connect(err => {
    if (err) {
        console.error('Could not connect to database:', err);
    } else {
        console.log('Connected to MySQL database.');
    }
});
