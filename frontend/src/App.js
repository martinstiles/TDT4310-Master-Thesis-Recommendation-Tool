import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Home from './components/home/home'
import Summaries from './components/summaries/summaries'
import Recommender from './components/recommender/recommender'

function App() {
  return (
    <Router>

      <div className="App">
        <Switch>
          <Route path="/summaries">
            <Summaries />
          </Route>
          <Route path="/recommender">
            <Recommender />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
