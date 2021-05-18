import React from 'react'
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

const ThesisBox = ({i, title, id, mentor}) => {
    const cardStyle = { width: "700px", textAlign: "left", marginBottom: "1em", marginRight: "0.5em", marginLeft: "0.5em"}

    return (
        <Card style={cardStyle}>
            <div style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
                <CardContent style={{width: "600px", display: "flex", flexDirection: "column"}}>
                    <Typography style={{ fontSize: "14px" }} color="textSecondary" gutterBottom>
                        {mentor}
                    </Typography>
                    <div style={{display: "flex", flexDirection: "row"}}>
                        <Typography variant="h5" component="h3" style={{marginRight: "10px"}}>
                            {i+1}.
                        </Typography>
                        <Typography variant="h5" component="h3">
                            {title}
                        </Typography>
                    </div>
                </CardContent>
                <CardActions style={{width: "100px", textAlign: "center"}}>
                    <a style={{textDecoration: "none"}} href={`https://www.idi.ntnu.no/education/oppgaveforslag.php?oid=${id}`} rel="noreferrer" target="_blank"> GO TO THESIS</a>
                    
                </CardActions>
            </div>
        </Card>
    )
}

export default ThesisBox
