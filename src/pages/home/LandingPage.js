import React from 'react'
import styles from '../../App.module.css';

const LandingPage = () => {
  return (
    <div className={styles.LandingPageHeader}>
      <h1>Trick or Trend</h1>
      <h3>Vote for your BOoO!</h3>
      <div className={styles.LandingPageLinks}>
        <div className={styles.Buttons}>
          <a className={styles.Button1} href="/signup">Sign Up</a>
          <a className={styles.Button1} href="/signin">Sign In</a>
          <a className={styles.Button2} href="/feed">Start Voting</a>
        </div>
      </div>
    </div>
  )
}

export default LandingPage