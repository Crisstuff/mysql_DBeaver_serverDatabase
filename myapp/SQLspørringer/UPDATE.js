app.put('/users/:id', (req, res) => {
    const { id } = req.params;
    const { name, email, age } = req.body;
    const sql = 'UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?';
    db.query(sql, [name, email, age, id], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'User updated successfully.' });
    });
 });
 