import React from 'react';
import { useEffect } from 'react';
import Wrapper from './Wrapper';

const Products = () => {

  useEffect(() => {
    const getProducts = async () => {
      const response = await fetch('http://172.18.0.1:8000/api/products');
      const data = await response.json();

      console.log(data);
    }
    getProducts();
  }, []);  

  return (
    <Wrapper>
      <div className="table-responsive">
        <table className="table table-striped table-sm">
          <thead>
            <tr>
              <th>#</th>
              <th>Header</th>
              <th>Header</th>
              <th>Header</th>
              <th>Header</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1,001</td>
              <td>Lorem</td>
              <td>ipsum</td>
              <td>dolor</td>
              <td>sit</td>
            </tr>
          </tbody>
        </table>
      </div>
    </Wrapper>
  );
};

export default Products;
