import React from 'react'
import Button from '@material-ui/core/Button'
import { Link } from "react-router-dom";

const HomeButton = () => {
    const style = {
        position: "absolute",
        left: "2em",
        top: "3em"
    }

    return (
        <Button style={style} variant="contained" color="primary" href="/" size="large" component={Link} to="/"> HOME </Button>
    )
}

export default HomeButton
