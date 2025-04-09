const express = require('express');
const cors = require('cors');
const pool = require('./db');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/register', async (req, res) => {
  const { email, password } = req.body;
  const [rows] = await pool.execute('INSERT INTO users (email, password) VALUES (?, ?)', [email, password]);
  res.json({ message: 'User registered successfully', id: rows.insertId });
});

app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const [rows] = await pool.execute('SELECT * FROM users WHERE email = ? AND password = ?', [email, password]);

  if (rows.length > 0) {
    res.json({ message: 'Login successful' });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});

app.listen(3000, () => {
  console.log('Backend listening on port 3000');
});
