import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import MenuItem from '@material-ui/core/MenuItem';

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
    const [n, setN] = useState(10)
    const [lang, setLang] = useState("en")
    const [noQuery, setNoQuery] = useState(false)


    const onClick = () => {
        props.setInterests(interests)
        props.setN(n)
        props.setLang(lang)
    }

    const handleDropdownChange = (event) => {
        setN(event.target.value)
    }

    const handleRadioChange = (event) => {
        setLang(event.target.value)
    }

    return (
        <>
            <p style={{ fontStyle: "italic" }}> We need to know your intersts to show you recommendations </p>
            <div style={{ width: "40%" }}>
                <div style={container}>
                    <h3> Interests* (seperated with space) </h3>
                    <TextField style={textFieldStyle} id="outlined-basic" placeholder="NLP Blockchain environment football" variant="outlined"
                        onChange={(e) => setInterests(e.target.value)}
                    />

                    <div style={{marginTop: "3em", marginBottom: "3em"}}>
                        <h3> Number of recommendations </h3>
                        <TextField
                        style={{backgroundColor: "white", borderRadius: "5px", width: "50px", padding: "10px"}}
                        select
                        value={n}
                        onChange={handleDropdownChange}
                        >
                        {[5, 10, 15, 20].map((option) => (
                            <MenuItem key={option} value={option}>
                            {option}
                            </MenuItem>
                        ))}
                        </TextField>
                    </div>

                    <h3> Language </h3>
                    <RadioGroup aria-label="quiz" name="quiz" value={lang} onChange={handleRadioChange} style={{diplsay: "flex", flexDirection: "row"}}>
                        <FormControlLabel value="en" control={<Radio style={{color: "white"}} />} label="English" />
                        <FormControlLabel value="no" control={<Radio style={{color: "white"}} />} label="Norwegian" />
                    </RadioGroup>

                    <div style={{ textAlign: "center" }}>
                        <Button style={buttonStyle} variant="contained" color="primary" size="large" onClick={onClick}> See my recommendations </Button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Form
