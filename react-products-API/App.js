import axios from "axios";
import React from "react";
import { Button, Table } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
const baseURL = "http://127.0.0.1:8000/api";

export default function App() {
  // const [product, setProduct] = React.useState([]);
  const [products, setProducts] = React.useState([]);



  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setProducts(response.data);
    });
  }, []);

  if (!products){
    return null;
  } else {

    return (
      
      <Table striped bordered hover>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Description</th>
        </tr>
      </thead>
    <tbody>
    {products.map((product, index) => {
    return (
          <tr>
                    <td> {product.name}</td>
                    <td>{product.price}</td>
                    <td>{product.description}</td>
                    <td className="buttons">
                        <button className="d-inline btn-primary" >
                            Update
                        </button>
                        <button className="d-inline mx-3 btn-danger" >
                            Delete
                        </button>
                        
                    </td>
                  </tr>
        );
      })}
      </tbody>
      </Table>
      
      

    )
  }

}