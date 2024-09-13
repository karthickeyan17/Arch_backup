import React ,{useRef,useState} from 'react';
import './App.css';

import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

import  {useAuthState} from 'react-firebase-hooks/auth';
import {useCollectionData} from 'react-firebase-hooks/firestore';

firebase.initializeApp({
  apiKey: "AIzaSyBHy2egD07UCHkj_09aHH7XvKbX3ponDZQ",
  authDomain: "chat-app-c88ca.firebaseapp.com",
  projectId: "chat-app-c88ca",
  storageBucket: "chat-app-c88ca.appspot.com",
  messagingSenderId: "579315496761",
  appId: "1:579315496761:web:42d3255cc1cbd53e0b9ae8",
  measurementId: "G-FY6WH12GN4"
})

const auth = firebase.auth();
const firestore = firebase.firestore();
function App() {

  const [user] = useAuthState(auth);

  return (
    <div className="App">
      <header>
        <SignOut />
      </header>

      <section>
        {user ? <ChatRoom /> : <SignIn />}
      </section>

    </div>
  );
}

function SignIn(){
  const signInWithGoogle = () =>{
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }
  return (
  <>
    <button onClick={signInWithGoogle}>signInWithGoogle</button>
  </>
  )
}

function SignOut(){
    return auth.currentUser &&  (
      <button onClick={()=>auth.signOut()}>Sign Out</button>
    )
}
function ChatRoom(){
   const messageRef = firestore.collection('message');
   const q = messageRef.orderBy('time').limit(25);
   const [message] = useCollectionData(q,{idField:'id'}); 
   console.log(message);
   return (
    <>
      {message && message.map(msg => <Chatmessages key={msg.id} message={msg} />)}
      {/* <h>hai</h> */}
      {/* <Chatmessages /> */}
    </>
   )

}
function Chatmessages(props){
  const { text, uid, photoURL } = props.message;
  console.log(text);
  // const messageClass = uid === auth.currentUser.uid ? 'sent' : 'received';

  return (<>
    <div>
      <p>{text}</p>
    </div>
  </>)
}

export default App;


