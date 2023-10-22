import React from 'react'

const LandingPage = () => {
  return (
    <div className='LandingPageHeader'>
      <h1>Trick or Trend</h1>
      <h2>Vote for your BOoO!</h2>
      <div className='LandingPageLinks'>
        <a href="/signup">Sign Up</a><br />
        <a href="/signin">Sign In</a><br />
        <a href="/vote">Start Voting</a>
      </div>
    </div>
  )
}

export default LandingPage