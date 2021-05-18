import React from 'react'
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';


const CustomCard = (props) => {
    const cardStyle = { width: "300px", textOverflow: "ellipsis", textAlign: "left", marginBottom: "1em", marginRight: "0.5em", marginLeft: "0.5em" }
    return (
        <Card style={cardStyle}>
            <div style={{ display: "flex", flexDirection: "column", justifyContent: "space-between" }}>
                <CardContent>
                    <Typography style={{ fontSize: "14px" }} color="textSecondary" gutterBottom>
                        {props.specialization}
                    </Typography>
                    <Typography variant="h5" component="h3">
                        {props.title}
                    </Typography>
                    <Typography style={{ marginBottom: "12px" }} color="textSecondary">
                        {props.professor}
                    </Typography>
                    <Typography variant="body2" component="p">
                        {props.keyWords}
                    </Typography>
                </CardContent>
                <CardActions style={{width: "50px"}}>
                    <Button size="small" href={props.url} target="_blank"> Go to thesis URL </Button>
                </CardActions>
            </div>
        </Card>
    )
}

export default CustomCard
