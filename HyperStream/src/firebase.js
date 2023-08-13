import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyA87d_JQOPrRQkP7ZZAnH_tT8sddZwP8Uc",
  authDomain: "backend-aecc3.firebaseapp.com",
  projectId: "backend-aecc3",
  storageBucket: "backend-aecc3.appspot.com",
  messagingSenderId: "934403029357",
  appId: "1:934403029357:web:76f4c5d3b4c12c40cf0264"
};

const app = initializeApp(firebaseConfig);

export const db = getFirestore(app);
