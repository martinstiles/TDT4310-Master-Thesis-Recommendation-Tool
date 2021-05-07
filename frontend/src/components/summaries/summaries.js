import React, { useState } from 'react'
import CustomCard from './card'
import Checkboxes from './checkboxes'
import SearchBox from './searchBox'
import HomeButton from '../homeButton'

const Summaries = () => {
    const containerStyle = {
        marginTop: "2em",
        marginBottom: "2em",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        width: "70%",
        justifyContent: "center",
    }

    const anchorStyle = {
        color: "white",
        textDecoration: "none"
    }
    const headerStyle = {
        fontSize: "4em",
        marginTop: "0.5em",
        marginBottom: "0.1em",
    }

    const [search, setSearch] = useState("")

    const handleSearchChange = (e) => {
        setSearch(e.target.value)
    }

    return (
        <>
            <HomeButton />
            <a href="/" style={anchorStyle}> <header style={headerStyle}>  Thesis Summaries </header> </a>
            <Checkboxes />
            <SearchBox handleSearchChange={handleSearchChange} />
            <div style={containerStyle}>
                {/* TODO: Perform query and make for loop here (every card) */}
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
                <CustomCard
                    specialization="Databaser og søk"
                    title="Automatic music transcription with deep learning"
                    professor="Björn Gamback"
                    keyWords="Music, Automation, Supervised Learning, Piano, LSTM" // Should probably be a list
                />
            </div>
        </>
    )
}

export default Summaries
