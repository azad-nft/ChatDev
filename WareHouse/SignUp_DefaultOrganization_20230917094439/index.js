import React, { useState } from 'react';
import InputField from '../components/InputField';
export default function Home() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/saveUser', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ firstName, lastName, email }),
      });
      if (response.ok) {
        alert('User details saved successfully!');
        setFirstName('');
        setLastName('');
        setEmail('');
      } else {
        alert('Failed to save user details.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');
    }
  };
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">User Authentication App</h1>
      <form onSubmit={handleSubmit}>
        <InputField
          label="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <InputField
          label="Last Name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
        <InputField
          label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Save
        </button>
      </form>
    </div>
  );
}