import React from 'react';
import axios from 'axios';
import { Jumbotron, Container } from 'react-bootstrap';
import Videos from './Videos';

class App extends React.Component {
  state = {
    videos: [],
  };

  componentDidMount() {
    axios.get('http://localhost:3000/api/getvideos').then((res) => {
      this.setState({
        videos: res.data,
      });
    });
  }

  render() {
    return (
      <>
        <Jumbotron fluid>
          <Container>
            <h1>Youtube Search API Project</h1>
            <p>This project</p>
          </Container>
        </Jumbotron>
        <Container>
          <Videos data={this.state.videos} />
        </Container>
      </>
    );
  }
}

export default App;
