import React from 'react'

const SearchBox = ({ handleSearchChange }) => {
    const style = {
        border: "none",
        outline: "none",
        padding: "0.5em",
        width: "12em",
        lineHeight: "30px",
        marginTop: "1em",
        borderRadius: "3px",
        fontSize: "1em"
    }
    return (
        <input
            // className="search"
            style={style}
            type="search"
            placeholder="Search for theses..."
            onChange={handleSearchChange}
        />
    )
}

export default SearchBox
