const express = require('express');
const app = express();

app.use(express.json());

app.post('/', (req, res) => {
  const data = req.body;
  // Do something with the data
  res.send(`Received POST request with data: ${JSON.stringify(data)}`);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
