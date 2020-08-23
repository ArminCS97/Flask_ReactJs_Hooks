import React, {useState} from "react";
import Form from "semantic-ui-react/dist/commonjs/collections/Form";
import Input from "semantic-ui-react/dist/commonjs/elements/Input";
import Rating from "semantic-ui-react/dist/commonjs/modules/Rating";
import {Button} from "semantic-ui-react";

export const MovieForm = ({ onNewMovie })=>{
    const [title, setTitle ] = useState('');
    const [rating, setRating] = useState('');

    return(
      <Form>
        <Form.Field>
          <Input placeholder={'movie title'}
                 value={title}
                 onChange={e => setTitle(e.target.value)}/>
        </Form.Field>
        <Form.Field>
          <Rating icon={'star'}
                  rating={rating}
                  maxRating={20}
                  onRate={(_, data) => {
                    setRating(data.rating);
                    console.log(data)
                  }}/>
        </Form.Field>
        <Form.Field>
          <Button onClick={async () => {
            const movie = {title, rating};
            // we add response to the DB
            const response = await fetch('/add_movies', {
              method: 'POST',
              headers: {
                'Content-type': 'application/json'
              },
              body: JSON.stringify(movie)
            });
            // Now we update our UI too
            if (response.ok) { // updating our UI
              console.log('response worked perfectly');
              onNewMovie(movie);
              setRating(1); // clearing rating after submitting
              setTitle('');
            }
          }}>
            Submit
          </Button>
        </Form.Field>
      </Form>
    );
};
