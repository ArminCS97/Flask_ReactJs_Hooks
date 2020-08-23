import React from "react";
import List from "semantic-ui-react/dist/commonjs/elements/List";
import Header from "semantic-ui-react/dist/commonjs/elements/Header";
import Rating from "semantic-ui-react/dist/commonjs/modules/Rating";

export const Movies = ({ movies }) =>{ // this component just takes a movie and shows its details
    // it does not care from where the movie come from
    return(
        <List>
            Below you can find the list of Movies:
            {movies.map( mo => {
                return (
                    <List.Item key={mo.title}>
                        <br/>
                        <br/>
                        <br/>
                        <br/>
                        <Header> {mo.title} </Header>
                        <Rating rating={mo.rating} maxRating={20} disabled> </Rating>
                    </List.Item>
                )
            })}
        </List>
    );
};