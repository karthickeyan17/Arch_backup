import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">hf
    </ul>
    <div>
      </div>
      <h1>project</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>

  )
}

export default App
