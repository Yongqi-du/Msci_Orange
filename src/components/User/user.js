import React from 'react';
import { Auth } from 'aws-amplify';

function User() {
  const handleSignOut = async () => {
    try {
      await Auth.signOut();
    } catch (error) {
      console.log('Error signing out:', error);
    }
  };

  return (
    <div className='flex-col'>
      <div className='h4'>User</div>
      <button onClick={handleSignOut}>Sign Out</button>
    </div>
  );
}

export default User;