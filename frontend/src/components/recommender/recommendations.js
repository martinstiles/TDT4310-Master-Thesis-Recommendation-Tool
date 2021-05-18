import React, {useState, useEffect} from 'react'
import ThesisBox from './thesisBox'
import Button from '@material-ui/core/Button'

const Recommendations = ({ interests, n, lang, setInterests }) => {
    const containerStyle = {
        marginTop: "1em",
        marginBottom: "2em",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "center",
    }

    const buttonStyle = {
        height: "3em",
        marginBottom: "1em"
    }

    const [response, setResponse] = useState([])

    const getRecommendations = async () => {
        // const url = `http://134.209.206.60:3000/` // --> for testing
        const url = `http://134.209.206.60:3000/recommender?query=${interests}&lang=${lang}&n=${n}`
        return fetch(url, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'}
        }).then(res => res.json())
    }

    useEffect(() => {
        let mounted = true;
        getRecommendations()
            .then(recommendations => {
            if(mounted) {
                setResponse(recommendations.data)
            }
            })
        return () => mounted = false;
        }, [])



    const resetForm = () => {
        setInterests("")
        // setResponse([])
    }

    return (
        <>
            <p> <b> Interests: </b> <i> {interests} </i> </p>
            <Button style={buttonStyle} variant="contained" color="primary" size="large" onClick={() => resetForm()}> Reset interests </Button>
            {response.length === 0
            ?
            <h1> Loading ... </h1>
            :
            <div style={containerStyle}>
                {response.map((obj, index) => <ThesisBox key={index} i={index} title={obj.title} id={obj.id} mentor={obj.mentor} />)}
            </div>
            }
        </>
    )
}

export default Recommendations
