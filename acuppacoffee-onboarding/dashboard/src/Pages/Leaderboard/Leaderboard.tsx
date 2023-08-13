import styles from './Leaderboard.module.scss'
import React from 'react'
import personOne from '../../assets/png/person1.png'
import personTwo from '../../assets/png/person2.png'
import personThree from '../../assets/png/person3.png'
import samantha2 from '../../assets/png/samantha2.png'
import coffee from '../../assets/png/coffee.png'




export default function Leaderboard(){
    return(
        < >
        <main className ={styles.currentLeaderboard}>
            <div className={styles.leaderScoreCard}>
                <section className = {styles.scoresOverview}>
                    <div className = {styles.scoresHeader}>
                        <p className={styles.Title}>Current Leaderboard</p>
                    </div>
                </section>

                <section className ={styles.firstPlace}>
                    <div className ={styles.personImages}>
                        <img className ={styles.personImg} src={personOne} alt ="person one" />
                        <p className ={styles.leaderName}>RJ Cooper</p>
                        <div className={styles.scoreWrapper}>
                        <p className ={styles.leaderScore}>950 pts</p>
                        </div>
                        
                    </div>
                </section>

                <section className ={styles.secondPlace}>
                    <div className ={styles.personImages}>
                        <img className ={styles.personImg} src= {personTwo} alt ="person one" />
                        <p className ={styles.leaderName}>Sam Smith</p>
                        <p className ={styles.leaderScore}>890 pts</p>
                    </div>
                </section>

                <section className ={styles.thirdPlace}>
                    <div className= {styles.personImages}>
                      
                        <img className ={styles.personImg} src= {personThree} alt ="person one" />
                        <p className ={styles.leaderName}>Adele</p>
                        <p className ={styles.leaderScore}>840 pts</p>
                     {/* <button className={styles.coffeeBtn}>
                    <img className={styles.coffee} src={coffee} alt="add" />
                    </button>*/} 
            
                     </div>
                    
                    

                </section>

                <section className = {styles.userScoreOverview}>
                    <div className = {styles.userScoresHeader}>
                        <p className={styles.userScoreTitle}>Your Current Score</p>
                    </div>
                </section>

                <section className ={styles.userPlace}>
                    <div className ={styles.personImages}>
                        <img className ={styles.samantha2} src= {samantha2} alt ="person one" />
                        <p className ={styles.leaderName}>Samantha J</p>
                        <p className ={styles.leaderScore}>740 pts</p>
                         <button className={styles.button} type="button">
                      Play Game
                      </button>
                    </div>
                    
                 
                </section>
            </div>
        </main>
    </>
    );
}