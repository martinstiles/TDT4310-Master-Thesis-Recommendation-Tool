import React from 'react'
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';

const Checkboxes = () => {
    // TODO: Move state up in hierarchy and make it actually change the content of the page
    const [state, setState] = React.useState({
        checkedPU: true,
        checkedDB: true,
        checkedAlg: true,
        checkedAI: true,
    });

    const handleChange = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

    return (
        <FormGroup row>
            <FormControlLabel
                control={
                    <Checkbox
                        style={state.checkedPU ? { color: "" } : { color: 'white' }}
                        checked={state.checkedPU}
                        onChange={handleChange}
                        name="checkedPU"
                        color="primary"
                    />
                }
                label="Programvaresystemer"
            />
            <FormControlLabel
                control={
                    <Checkbox
                        style={state.checkedDB ? { color: "" } : { color: 'white' }}
                        checked={state.checkedDB}
                        onChange={handleChange}
                        name="checkedDB"
                        color="primary"
                    />
                }
                label="Databaser og søk"
            />
            <FormControlLabel
                control={
                    <Checkbox
                        style={state.checkedAlg ? { color: "" } : { color: 'white' }}
                        checked={state.checkedAlg}
                        onChange={handleChange}
                        name="checkedAlg"
                        color="primary"
                    />
                }
                label="Algoritmer og datamaskiner"
            />
            <FormControlLabel
                control={
                    <Checkbox
                        style={state.checkedAI ? { color: "" } : { color: 'white' }}
                        checked={state.checkedAI}
                        onChange={handleChange}
                        name="checkedAI"
                        color="primary"
                    />
                }
                label="Kunstig intelligens"
            />
        </FormGroup>
    )
}

export default Checkboxes
