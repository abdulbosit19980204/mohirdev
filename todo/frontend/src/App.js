import React, {Component} from "react";
import axios from 'axios'

class App extends Component {
    state = {
        todos: []
    };

    //yangi
    componentDidMount() {
        this.getTodo();
    }

    getTodo() {
        axios
            .get('http://localhost:8000/api/v1/')
            .then(res => {
                this.setState({todos: res.data});
            })
            .catch(err => {
                console.log()
            })
    }

    render() {
        return (<div>
            {this.state.todos.map(item => (<div key={item.id}>
                <h1>{item.title}</h1>
                <p>{item.description}</p>
            </div>))}
        </div>);
    }
}

export default App