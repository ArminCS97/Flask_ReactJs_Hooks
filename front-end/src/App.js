import React, {useEffect, useState} from 'react';
import './App.css';
import { Movies } from "./components/Movies";
import {MovieForm} from "./components/MovieForm";
import {Container} from "semantic-ui-react";

function App() {
  const [movies1, setMovies] = useState([]);

  useEffect( ()=>{
    fetch('/movies').then(response => response.json().then(data =>{
      setMovies(data.movies); // important to have data.movies
      console.log(data);
      })
    );
  }, []);

  return(
    <div className="App">
      <Container style={{marginTop: 60}}>
        <MovieForm onNewMovie={movie2 => setMovies(currentMovies => [movie2 ,...currentMovies])}/>
        <Movies movies={movies1}/>
      </Container>
    </div>
  );
}

export default App;

{/*<MovieForm onNewMovie={movie2 => setMovies(currentMovies => [...currentMovies, movie2])}/>*/}
{/*... means that we want to keep currentMovies and add movie2 to it*/}