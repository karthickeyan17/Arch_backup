import { useState } from 'react'
import './App.css'

import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth';
import {useAuthState} from 'react-firebase-hooks/auth' ;
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
const [user] = useAuthState(auth);
function App() {
  return (
    <div>
      <header>
        <h>hello</h>
      </header>
      <section>
        {user ?<ChatRoom /> : <SignIn />}
      </section>
    </div>
  )
}

function SignIn() {
  const signInWithGoogle = () =>{
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }
  return (
    <button onClick={signInWithGoogle}>Sign in with Google</button>
  )
}
function SignOut(){
  return auth.currentUser && (
    <button onClick={()=> auth.SignOut}>Sign Out</button>
  )
}

function ChatRoom() {
  const messagesRef = firestore.collection('messages');
  const query = messagesRef.orderBy('createdAt').limit(25);
  const [messages] = useCollectionData(query,{idField : 'id'});;
  return (
    <>
      <div>
        {messages && messages.map(msg => <ChatMessage key={msg.id} message ={msg}/>)}
      </div>
      <div></div>
    </>
  )
}
function ChatMessage(props){
  const {text,uid} = props.message;
  return <p>{text}</p>
}
export default App
