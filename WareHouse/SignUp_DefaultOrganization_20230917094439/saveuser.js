import { pool } from '../../utils/db';
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ message: 'Method Not Allowed' });
    return;
  }
  const { firstName, lastName, email } = req.body;
  try {
    const client = await pool.connect();
    const result = await client.query(
      'INSERT INTO users (first_name, last_name, email) VALUES ($1, $2, $3)',
      [firstName, lastName, email]
    );
    client.release();
    res.status(200).json({ message: 'User details saved successfully!' });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ message: 'An error occurred. Please try again later.' });
  }
}