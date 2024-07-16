import React, {Component} from "react";

const list = [{
    "id": 1,
    "title": "Ertalab Speaking ga borishim kerak",
    "description": "Bugun darsga borolmadim shunga ertalab speaking ga darsga borishim kerak",
    "done": false,
    "deadline": "2024-07-17T08:00:00+05:00"
}, {
    "id": 2,
    "title": "Ertaga smenga boraman",
    "description": "Ertalab smenga xam borishim kerak",
    "done": false,
    "deadline": "2024-07-17T22:00:00+05:00"
}]

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {list};
    }

    render() {
        return (<div>
            {this.state.list.map(item => (<div key={item.id}>
                <h1>{item.title}</h1>
                <p>{item.description}</p>
            </div>))}
        </div>);
    }
}

export default App