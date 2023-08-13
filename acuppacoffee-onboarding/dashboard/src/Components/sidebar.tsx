import React from 'react'
import styles from './Sidebar.module.scss'
import samanthaImg from '../assets/png/samantha.png'
import { Link, useLocation } from "react-router-dom";

const sidebarNavLinks = ["profile", "leaderboard", "buy coffee", "start a game", "settings" ]

export default function Sidebar() {
    const location = useLocation();
    return <>
        <aside className={styles.sidebar}>
            <div className={styles.sidebarContent}>
              
                <div className={styles.profileDetails}>
                <div className = {styles.sidebarTitle}>
                         <h2>Welcome</h2>
                    </div>
                    <div className={styles.profileImageDiv}>
                        <img className={styles.samanthaImg} src ={samanthaImg} alt="samantha"/>
                        
                    </div>
                    <p className ={styles.userName}>Samantha J</p>
                    <p className ={styles.userEmail}>samatha@company.com</p>
                </div>

                <nav className={styles.sidebarNav}>
                    <ul>
                    {sidebarNavLinks.map((sidebarNavLink) => (
                <li className={styles.sidebarNavItem} key={sidebarNavLink}>
                  <Link
                    className={
                      location.pathname === `/${sidebarNavLink}`
                        ? styles.sidebarNavLinkActive
                        : styles.sidebarNavLink
                    }
                    to={`/${sidebarNavLink}`}
                  >
                    {sidebarNavLink.charAt(0).toUpperCase() +
                      sidebarNavLink.slice(1)}
                  </Link>
                </li>
              ))}
                       
                    </ul>
                </nav>
            </div>
        </aside>

    </>
}

 
