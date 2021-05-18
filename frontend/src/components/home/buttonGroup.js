import React from 'react'
import { Button } from '@material-ui/core';
import { Link } from "react-router-dom";

const ButtonGroup = () => {
    const buttonStyle = { width: "11em", height: "3em", fontSize: "2em", textTransform: "none" }
    const exploreButtonStyle = { ...buttonStyle, marginRight: "1em" , backgroundColor: "#707070"}

    return (
        <div style={{ marginTop: "2em" }}>
            <Button disabled={true} style={exploreButtonStyle} variant="contained" color="primary" component={Link} to="/summaries">
                Summaries
            </Button>
            <Button
                style={buttonStyle} variant="contained" color="primary" component={Link} to="/recommender">
                Recommendations
            </Button>
        </div>
    )
}

export default ButtonGroup
