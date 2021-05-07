import React from 'react'
import { Button } from '@material-ui/core';
import { Link } from "react-router-dom";

const ButtonGroup = () => {
    // const history = useHistory();
    const buttonStyle = { width: "11em", height: "3em", fontSize: "2em", textTransform: "none" }
    const exploreButtonStyle = { ...buttonStyle, marginRight: "1em" }

    return (
        <div style={{ marginTop: "2em" }}>
            <Button style={exploreButtonStyle} variant="contained" color="primary" component={Link} to="/summaries">
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
