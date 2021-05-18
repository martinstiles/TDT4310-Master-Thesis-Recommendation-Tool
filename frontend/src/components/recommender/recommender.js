import React, { useState } from 'react'
import Form from './form'
import Recommendations from './recommendations'
import HomeButton from '../homeButton'

const Recommender = () => {
    const containerStyle = {
        marginTop: "2em",
        marginBottom: "2em",
        display: "flex",
        flexDirection: "column",
        width: "70%",
        justifyContent: "center",
        alignItems: "center"
    }

    const anchorStyle = {
        color: "white",
        textDecoration: "none"
    }

    const [interests, setIntersets] = useState("")
    const [n, setN] = useState(10)
    const [lang, setLang] = useState("en")

    return (
        <div style={containerStyle}>
            <HomeButton />
            <a href="/" style={anchorStyle}> <header style={{ fontSize: "4em", marginTop: "0.5em" }}> Thesis Recommender </header> </a>
            {
                interests === ""
                    ?
                    <Form setInterests={setIntersets} setN={setN} setLang={setLang} />
                    :
                    <Recommendations interests={interests} n={n} lang={lang} setInterests={setIntersets} />
            }
        </div>
    )
}

export default Recommender
