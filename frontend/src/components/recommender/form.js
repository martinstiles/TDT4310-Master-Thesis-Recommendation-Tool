import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'

const Form = (props) => {
    const container = {
        textAlign: "left"
    }

    const textFieldStyle = {
        backgroundColor: "white",
        borderRadius: "5px",
        width: "100%"
    }

    const buttonStyle = {
        marginTop: "3em",
        height: "4em"
    }

    const [interests, setInterests] = useState("")
    const [companies, setCompanies] = useState("")


    const onClick = () => {
        props.setInterests(interests)
        props.setCompanies(companies)
    }

    return (
        <>
            <p style={{ fontStyle: "italic" }}> We need to get some information about your preferences before we can show you recommendations </p>
            <div style={{ width: "40%" }}>
                <div style={container}>
                    <h3> *Interests <i>(seperated with comma)</i> </h3>
                    <TextField style={textFieldStyle} id="outlined-basic" placeholder="AI, NLP, music, football, ..." variant="outlined"
                        onChange={(e) => setInterests(e.target.value)}
                    />
                    <h3> Companies </h3>
                    <TextField style={textFieldStyle} id="outlined-basic" placeholder="Kahoot, NRK, ..." variant="outlined"
                        onChange={(e) => setCompanies(e.target.value)}
                    />
                    <div style={{ textAlign: "center" }}>
                        <Button style={buttonStyle} variant="contained" color="primary" size="large" onClick={onClick}> See my recommendations </Button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Form
