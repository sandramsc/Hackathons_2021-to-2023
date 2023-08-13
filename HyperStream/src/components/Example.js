import "../App.css";
import React, { useState, useEffect } from 'react';
import { collection, addDoc, getDocs } from "firebase/firestore";
import {db} from '../firebase';


 
 
const Example = () => {
    const [example, setExample] = useState("");
    const [examples, setExamples] = useState([]);
 
    const addExample = async (e) => {
        e.preventDefault();  
       
        try {
            const docRef = await addDoc(collection(db, "examples"), {
              example: example,    
            });
            console.log("Document written with ID: ", docRef.id);
          } catch (e) {
            console.error("Error adding document: ", e);
          }
    }
 
    const fetchPost = async () => {
       
        await getDocs(collection(db, "examples"))
            .then((querySnapshot)=>{              
                const newData = querySnapshot.docs
                    .map((doc) => ({...doc.data(), id:doc.id }));
                setExamples(newData);                
                console.log(examples, newData);
            })
       
    }
   
    useEffect(()=>{
        fetchPost();
    }, [])
 
 
    return (
        <section className="example-container">
            <div className="example">
                <h1 className="header">
                    Example
                </h1>
   
                <div>
   
                    <div>
                        <input
                            type="text"
                            placeholder="This is an example"
                            onChange={(e)=>setExample(e.target.value)}
                        />
                    </div>
   
                    <div className="btn-container">
                        <button
                            type="submit"
                            className="btn"
                            onClick={addExample}
                        >
                            Submit
                        </button>
                    </div>
   
                </div>
   
                <div className="example-content">
                    {
                        examples?.map((example,i)=>(
                            <p key={i}>
                                {example.example}
                            </p>
                        ))
                    }
                </div>
            </div>
        </section>
    )
}
 
export default Example