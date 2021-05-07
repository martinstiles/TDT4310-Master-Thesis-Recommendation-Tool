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
    const [companies, setCompanies] = useState("")

    return (
        <div style={containerStyle}>
            <HomeButton />
            <a href="/" style={anchorStyle}> <header style={{ fontSize: "4em", marginTop: "0.5em" }}> Thesis Recommender </header> </a>
            {
                interests === ""
                    ?
                    <Form setInterests={setIntersets} setCompanies={setCompanies} />
                    :
                    // Perform query and show it
                    <Recommendations interests={interests} companies={companies} setInterests={setIntersets} setCompanies={setCompanies} />
            }
        </div>
    )
}

export default Recommender
