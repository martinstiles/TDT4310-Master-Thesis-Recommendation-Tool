import React from 'react'
import CustomCard from '../summaries/card'
import Button from '@material-ui/core/Button'

const Recommendations = ({ interests, companies, setInterests, setCompanies }) => {
    const containerStyle = {
        marginTop: "1em",
        marginBottom: "2em",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "center",
    }

    const buttonStyle = {
        height: "3em"
    }

    const resetForm = () => {
        setInterests("")
        setCompanies("")
    }

    return (
        <>
            {/*<h2> Here is the top five recommendations based on: </h2>*/}
            <p> <b> Interests: </b> <i> {interests} </i> </p>
            {companies && <p style={{ marginTop: "0" }}> <b> Companies: </b> <i> {companies} </i> </p>}
            <Button style={buttonStyle} variant="contained" color="primary" size="large" onClick={() => resetForm()}> Reset </Button>
            <div style={containerStyle}>
                <CustomCard
                    specialization="Kunstig intelligens"
                    title="Automatic Metadata Generation"
                    professor="Ole Jakob Mengshoel"
                    keyWords="Artificial Intelligence, Machine Learning, Technology, ASR" // Should probably be a list
                />
                <CustomCard
                    specialization="Databaser og søk"
                    title="Automatic music transcription with deep learning"
                    professor="Björn Gamback"
                    keyWords="Music, Automation, Supervised Learning, Piano, LSTM" // Should probably be a list
                />
                <CustomCard
                    specialization="Kunstig intelligens"
                    title="Automatic Metadata Generation"
                    professor="Ole Jakob Mengshoel"
                    keyWords="Artificial Intelligence, Machine Learning, Technology, ASR" // Should probably be a list
                />
                <CustomCard
                    specialization="Databaser og søk"
                    title="Automatic music transcription with deep learning"
                    professor="Björn Gamback"
                    keyWords="Music, Automation, Supervised Learning, Piano, LSTM" // Should probably be a list
                />
                <CustomCard
                    specialization="Kunstig intelligens"
                    title="Automatic Metadata Generation"
                    professor="Ole Jakob Mengshoel"
                    keyWords="Artificial Intelligence, Machine Learning, Technology, ASR" // Should probably be a list
                />
            </div>
        </>
    )
}

export default Recommendations
