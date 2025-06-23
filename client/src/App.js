// client/src/App.js
import { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetch("/movies")
      .then((r) => r.json())
      .then((data) => {
        console.log("Fetched movies:", data);
        setMovies(data);
      });
  }, []);

  return (
    <div>
      <h1>Movies List</h1>
      <ul>
        {movies.length === 0 ? (
          <li>No movies found</li>
        ) : (
          movies.map((movie) => <li key={movie.id}>{movie.title}</li>)
        )}
      </ul>
    </div>
  );
}

export default App;
